# config.py
import os
import subprocess
from libqtile import bar, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from themes import get_current_theme
from keys import BASE_KEYS
from widgets import make_bar_widgets

THEME = get_current_theme()

mod = "mod4"
terminal = "alacritty"

# Generate group switch keys
groups = [Group(f"{i + 1}", label="") for i in range(8)]
for i in groups:
    BASE_KEYS.extend([
        Key(
            [mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc=f"Switch to group {i.name}",
        ),
        Key(
            [mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc=f"Switch to & move focused window to group {i.name}",
        ),
    ])

keys = BASE_KEYS

layouts = [
    layout.Bsp(**THEME["layout"], fair=False, border_on_single=True),
    layout.Columns(**THEME["layout"], border_on_single=True, num_columns=2, split=False),
    layout.Floating(**THEME["layout"]),
    layout.Max(**THEME["layout"]),
]

widget_defaults = dict(font="sans", fontsize=12, padding=3)
extension_defaults = [widget_defaults.copy()]

screens = [
    Screen(
        top=bar.Bar(
            make_bar_widgets(THEME),
            30,
            border_color=THEME["colors"]["border"],
            border_width=[0, 0, 0, 0],
            margin=[15, 60, 6, 60],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules: list = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=THEME["colors"]["layout_border_focus"],
    border_normal=THEME["colors"]["layout_border_normal"],
    border_width=0,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
)


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser(".config/qtile/autostart_once.sh")
    if os.path.exists(script):
        subprocess.call([script])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
