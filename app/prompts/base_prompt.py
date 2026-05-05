def build_prompt(topic, platform, tone, duration):
    return f"""
You are a viral content creator.

Generate a complete social media content pack.

INPUT:
Topic: {topic}
Platform: {platform}
Tone: {tone}
Duration: {duration} seconds

OUTPUT FORMAT:

Hook:
<one powerful opening line>

Script:
<scene-wise breakdown>

Caption:
<engaging caption>

Hashtags:
<relevant hashtags>

Shot List:
<camera angles and scenes>

Make it highly engaging and platform-optimized.
"""