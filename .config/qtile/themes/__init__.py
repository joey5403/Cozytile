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
        return theme_module.COLORS
    except (ModuleNotFoundError, ImportError, AttributeError):
        # Fallback to default theme
        default_module = import_module(f"themes.{DEFAULT_THEME}")
        return default_module.COLORS
