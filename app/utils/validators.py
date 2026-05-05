def validate_hooks(hooks: list):
    if not hooks or len(hooks) < 2:
        return False

    for hook in hooks:
        if len(hook.split()) > 12:
            return False

    return True


def validate_script(script: str):
    if not script:
        return False

    lines = script.split("\n")
    scenes = [line for line in lines if line.lower().startswith("scene")]

    if len(scenes) < 4 or len(scenes) > 6:
        return False

    return True


def validate_hashtags(hashtags: list):
    if not hashtags or len(hashtags) != 10:
        return False

    for tag in hashtags:
        if not tag.startswith("#"):
            return False

    return True


def validate_shotlist(shots: list):
    if not shots or len(shots) > 6:
        return False

    return True