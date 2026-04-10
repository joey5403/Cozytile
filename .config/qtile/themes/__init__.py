import os
from importlib import import_module


def get_current_theme():
    """Load theme from ~/.config/qtile/.current_theme file."""
    theme_file = os.path.expanduser("~/.config/qtile/.current_theme")
    if os.path.exists(theme_file):
        with open(theme_file) as f:
            theme_name = f.read().strip()
    else:
        theme_name = "cozy"

    theme_module = import_module(f"themes.{theme_name}")
    return theme_module.COLORS