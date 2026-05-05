def build_shotlist_prompt(topic, tone, style):
    return f"""
Create a short-form video shot list.

Input:
Topic: {topic}
Tone: {tone}

Creator Context:
- Style: {style["style"]}
- Audience: {style["audience"]}
- Elements: {", ".join(style["signature_elements"])}

Rules:
- Max 6 shots
- Each shot = one line
- Keep it slightly descriptive but concise
- Focus on actions and visuals (not explanations)
- Use reels-style shooting (quick cuts, POV, handheld)
- Avoid long descriptions or storytelling
- Keep each line under 15 words
- Ensure variety in actions across shots

Output Rules:
- One shot per line
- No numbering
- No extra text before or after
"""