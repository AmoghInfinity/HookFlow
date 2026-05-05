def build_hashtag_prompt(topic):
    return f"""
You are a social media growth expert.

Generate EXACTLY 10 hashtags for short-form content.

Rules:
- All hashtags must be relevant to the topic
- Mix:
  - short hashtags (1-2 words)
  - medium hashtags (2-3 words)
  - long-tail hashtags (specific phrases)
- Avoid generic tags like #content, #reels, #viral
- Avoid repeating the same words
- Keep them realistic and commonly used
- Do NOT create overly long or unnatural hashtags

Topic: {topic}

Output Rules:
- Return ONLY hashtags
- One hashtag per line
- Each must start with '#'
- No numbering, no explanation
"""