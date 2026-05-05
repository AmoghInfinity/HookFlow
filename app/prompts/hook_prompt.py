from app.config.trend_config import TREND_PATTERNS


def build_hook_prompt(topic, platform, tone, style):
    return f"""
You are a viral short-form content expert.

Generate a small set of high-performing hooks.

Context:
- Platform: {platform}
- Tone: {tone}
- Style direction: {style["style"]}
- Audience: {style["audience"]}

Trend Context:
Some high-performing hook patterns include:
{", ".join(TREND_PATTERNS[:5])}

Rules:
- Generate a few (around 3) hooks
- Each hook must be under 10 words
- Hooks must be diverse in style (avoid repeating patterns)
- Use a mix of curiosity, relatability, or strong statements
- Hooks may loosely follow high-performing patterns, but must stay original
- Avoid copying patterns directly
- Avoid unrealistic or misleading claims
- Avoid generic phrases like:
  - "Get ready for..."
  - "Did you know..."
- Even for aesthetic styles, hooks must still create curiosity or tension

Quality Criteria:
- Scroll-stopping
- Clear and specific
- Emotionally engaging

Topic: {topic}

Output Rules:
- Return only hooks
- One per line
- No numbering
- No quotes
- No explanations
"""