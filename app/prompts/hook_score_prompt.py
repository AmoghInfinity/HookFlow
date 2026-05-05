def build_hook_score_prompt(topic, hooks):
    return f"""
You are a viral content expert.

Evaluate these hooks for short-form content.

Criteria:
- Scroll-stopping power
- Curiosity gap
- Emotional trigger
- Clarity
- Alignment with proven viral patterns
- Hook must be supported by content (no misleading claims)
- Prefer believable but intriguing hooks

Topic: {topic}

Hooks:
{hooks}

Task:
- Rank the hooks from best to worst
- Return ONLY the best hook (no explanation)
"""