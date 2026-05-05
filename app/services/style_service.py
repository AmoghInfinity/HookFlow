from app.config.style_config import STYLE_PRESETS


def get_style(style_name: str):
    return STYLE_PRESETS.get(style_name.lower(), STYLE_PRESETS["default"])