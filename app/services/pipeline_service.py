from app.services.llm_service import generate_content
from app.prompts.hook_prompt import build_hook_prompt
from app.prompts.script_prompt import build_script_prompt
from app.prompts.caption_prompt import build_caption_prompt
from app.prompts.hashtag_prompt import build_hashtag_prompt
from app.prompts.shotlist_prompt import build_shotlist_prompt
from app.prompts.hook_score_prompt import build_hook_score_prompt
from app.services.style_service import get_style

from app.utils.validators import (
    validate_hooks,
    validate_script,
    validate_hashtags,
    validate_shotlist
)

from app.utils.logger import get_logger

logger = get_logger("pipeline")


# ----------------------------
# Retry Helper
# ----------------------------

def generate_with_retry(prompt, max_retries=2):
    for attempt in range(max_retries):
        result = generate_content(prompt)

        if result and result.strip():
            return result

        logger.warning(f"Retrying generation (attempt {attempt + 1})")

    logger.error("Generation failed after retries")
    return None


# ----------------------------
# Helper Functions
# ----------------------------

def clean_hooks(hooks_text: str):
    lines = hooks_text.split("\n")
    cleaned = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "." in line:
            parts = line.split(".", 1)
            if parts[0].isdigit():
                line = parts[1].strip()

        line = line.strip().strip('"').strip("'")

        if line:
            cleaned.append(line)

    return cleaned


def clean_hashtags(text: str):
    lines = text.split("\n")
    hashtags = []

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            hashtags.append(line)

    return hashtags


def clean_shotlist(text: str):
    lines = text.split("\n")
    shots = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.lower().startswith("here"):
            continue

        shots.append(line)

    return shots[:6]


# ----------------------------
# Main Pipeline
# ----------------------------

def generate_full_content(request):

    logger.info(f"Start generation | topic={request.topic} | style={request.style}")

    style = get_style(request.style)

    # ----------------------------
    # 1. Hooks
    # ----------------------------

    hooks_text = generate_with_retry(
        build_hook_prompt(request.topic, request.platform, request.tone, style)
    )

    hooks_list = clean_hooks(hooks_text or "")

    if not validate_hooks(hooks_list):
        logger.warning("Hook validation failed. Using fallback.")
        hooks_list = [f"{request.topic} you can't ignore"]

    logger.info(f"Hooks: {hooks_list}")

    # Hook scoring
    if hooks_list:
        hooks_str = "\n".join(hooks_list)

        best_hook = generate_with_retry(
            build_hook_score_prompt(request.topic, hooks_str)
        )

        best_hook = (best_hook or "").strip().strip('"').strip("'")

        selected_hook = None
        for hook in hooks_list:
            if best_hook.lower() in hook.lower():
                selected_hook = hook
                break

        if not selected_hook:
            logger.warning("Hook scoring mismatch. Using first hook.")
            selected_hook = hooks_list[0]
    else:
        selected_hook = f"{request.topic} you can't ignore"

    logger.info(f"Selected hook: {selected_hook}")

    # ----------------------------
    # 2. Script
    # ----------------------------

    script = generate_with_retry(
        build_script_prompt(
            request.topic,
            selected_hook,
            request.tone,
            request.duration,
            style
        )
    )

    if not validate_script(script or ""):
        logger.warning("Script validation failed. Using fallback.")
        script = f"Scene 1 (0-3s): {selected_hook}"

    # ----------------------------
    # 3. Caption
    # ----------------------------

    caption = generate_with_retry(
        build_caption_prompt(request.topic, request.tone, style)
    )

    if not caption:
        logger.warning("Caption generation failed. Using fallback.")
        caption = f"{request.topic} — you need to see this."

    # ----------------------------
    # 4. Hashtags
    # ----------------------------

    hashtags_raw = generate_with_retry(
        build_hashtag_prompt(request.topic)
    )

    hashtags = clean_hashtags(hashtags_raw or "")

    if not validate_hashtags(hashtags):
        logger.warning("Hashtag validation failed. Using fallback.")
        hashtags = [
            f"#{request.topic.replace(' ', '')}",
            "#trending",
            "#viral"
        ]

    # ----------------------------
    # 5. Shot List
    # ----------------------------

    shotlist_raw = generate_with_retry(
        build_shotlist_prompt(request.topic, request.tone, style)
    )

    shotlist = clean_shotlist(shotlist_raw or "")

    if not validate_shotlist(shotlist):
        logger.warning("Shotlist validation failed. Using fallback.")
        shotlist = [f"Simple shot for {request.topic}"]

    logger.info("Generation completed successfully")

    # ----------------------------
    # Final Output
    # ----------------------------

    return {
        "hook_options": hooks_list,
        "selected_hook": selected_hook,
        "script": script,
        "caption": caption,
        "hashtags": hashtags,
        "shot_list": shotlist
    }