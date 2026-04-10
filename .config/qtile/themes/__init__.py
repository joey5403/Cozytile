import os
from importlib import import_module

ALLOWED_THEMES = {"cozy", "carbon", "everforest", "natura", "sakura"}
DEFAULT_THEME = "cozy"


def get_current_theme():
    """Load theme from ~/.config/qtile/.current_theme file."""
    theme_file = os.path.expanduser("~/.config/qtile/.current_theme")
    theme_name = DEFAULT_THEME

    if os.path.exists(theme_file):
        try:
            with open(theme_file, encoding="utf-8") as f:
                theme_name = f.read().strip()
        except (OSError, IOError):
            theme_name = DEFAULT_THEME

    # Validate theme name to prevent module injection
    if theme_name not in ALLOWED_THEMES:
        theme_name = DEFAULT_THEME

    try:
        theme_module = import_module(f"themes.{theme_name}")
    except (ModuleNotFoundError, ImportError):
        # Fallback to default theme
        theme_module = import_module(f"themes.{DEFAULT_THEME}")

    # Return a merged dict so config.py can access theme["colors"], theme["layout"], etc.
    return {
        "colors": theme_module.COLORS,
        "layout": getattr(theme_module, "LAYOUT", {}),
        "sizes": getattr(theme_module, "SIZES", {}),
        "font": getattr(theme_module, "FONT", "sans"),
        "font_bold": getattr(theme_module, "font_bold", "sans"),
    }
