# keys.py
from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

BASE_KEYS = [
    #  D E F A U L T - 布局导航
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # 窗口移动
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # 窗口缩放
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),

    # Qtile 控制
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Rofi 脚本
    Key([mod], "r", lazy.spawn("sh -c ~/.config/rofi/scripts/launcher"), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc="powermenu"),
    Key([mod], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/theme_switcher"), desc="theme_switcher"),

    # 媒体键 - 音量
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc="Volume Up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc="volume down"),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc="Volume Mute"),

    # 媒体键 - 播放
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="playerctl"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="playerctl"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="playerctl"),

    # 亮度键
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc="brightness UP"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc="brightness Down"),

    # 自定义应用
    Key([mod], "e", lazy.spawn("thunar"), desc="file manager"),
    Key([mod], "v", lazy.spawn("roficlip"), desc="clipboard"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Screenshot"),

    # Alt+Tab 窗口切换（从 Carbon 补充）
    Key(["mod1"], "Tab", lazy.group.next_window(), desc="Cycle to next window"),
    Key(["mod1", "shift"], "Tab", lazy.group.prev_window(), desc="Cycle to previous window"),
]
