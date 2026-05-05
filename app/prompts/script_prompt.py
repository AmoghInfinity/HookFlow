def build_script_prompt(topic, hook, tone, duration, style):
    return f"""
You are a short-form content creator for platforms like Instagram Reels and YouTube Shorts.

Create a HIGH-ENGAGEMENT video script.

Input:
Topic: {topic}
Hook: {hook}
Tone: {tone}
Duration: {duration}s

Creator Context:
- Tone: {style["tone"]}
- Style: {style["style"]}
- Audience: {style["audience"]}
- Elements: {", ".join(style["signature_elements"])}

Strict Rules:
- Start EXACTLY with the hook
- Total scenes: 4 to 6 (decide based on duration)
- Each scene must be ONE short line (no paragraphs)
- Each line must be under 12 words
- Use fast pacing
- Add pattern interrupts (cuts, zooms, text overlays)
- Avoid explanations, focus on visuals + actions
- Make it feel like a reel, not a tutorial
- Use format: (start-end)s without extra parentheses placement errors
- Ensure no overlap and smooth progression

Structure Guideline (do NOT label explicitly):
Hook → Setup → Build → Twist → Payoff → CTA

Output Format:
- Each scene on a new line
- Prefix each line with: Scene <number> (<time range>):
- Ensure time ranges progress logically and fit within {duration}s
- Do NOT add any extra text before or after the scenes
"""