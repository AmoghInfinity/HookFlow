def build_caption_prompt(topic, tone, style):
    return f"""
You are a social media content creator.

Write a highly engaging caption.

Input:
Topic: {topic}
Tone: {tone}

Creator Context:
- Tone: {style["tone"]}
- Style: {style["style"]}
- Audience: {style["audience"]}
- Elements: {", ".join(style["signature_elements"])}

Trend Context:
Short-form captions often:
- Start with curiosity or bold statements
- Use relatable or emotional language
- Keep attention in the first line

Rules:
- Make it feel personal and conversational
- Start with a hook-style opening line
- Include a subtle call-to-action
- Keep it concise (2–3 lines max)
- Keep sentences short and punchy
- Avoid generic motivational phrases
- Avoid long storytelling sentences

Output:
Return only the caption text.
"""