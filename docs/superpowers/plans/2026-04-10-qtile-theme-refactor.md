# Qtile Theme Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 重构 Qtile 配置，将颜色变量化、组件抽象化、按键绑定共用化，使主题切换更简单高效。

**Architecture:** 主题颜色提取到 `themes/*.py` 独立文件，主配置通过 `get_current_theme()` 加载；widget 创建封装为工厂函数；按键绑定统一为 `keys.py` 中的 `BASE_KEYS` 列表。

**Tech Stack:** Python (Qtile libqtile), bash (theme_switcher)

---

## File Structure

```
.config/qtile/
├── config.py              # 修改：重构为使用 themes/keys/widgets 模块
├── keys.py                # 新建：共用按键绑定
├── widgets.py             # 新建：widget 工厂函数
├── themes/
│   ├── __init__.py       # 新建：主题加载逻辑
│   ├── cozy.py           # 新建：从 Cozy 提取颜色
│   ├── carbon.py         # 新建：从 Carbon 提取颜色
│   ├── everforest.py     # 新建：从 Everforest 提取颜色
│   ├── natura.py         # 新建：从 Natura 提取颜色
│   └── sakura.py         # 新建：从 Sakura 提取颜色
└── rofi/scripts/theme_switcher  # 修改：简化为写 .current_theme
```

---

## Task 1: 创建 themes 目录结构和 Cozy 主题

**Files:**
- Create: `.config/qtile/themes/__init__.py`
- Create: `.config/qtile/themes/cozy.py`

**Steps:**

- [ ] **Step 1: Create themes directory**

```bash
mkdir -p .config/qtile/themes
```

- [ ] **Step 2: Create themes/__init__.py with loading logic**

```python
# themes/__init__.py
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
```

- [ ] **Step 3: Create themes/cozy.py with extracted colors**

```python
# themes/cozy.py
COLORS = {
    # Bar backgrounds
    "bar_bg": "#282738",
    "bar_bg_alt": "#353446",

    # Accent color
    "accent": "#CAA9E0",

    # GroupBox
    "group_active": "#CAA9E0",
    "group_block_highlight": "#91B1F0",
    "group_highlight": "#353446",

    # Text colors
    "text": "#CAA9E0",
    "text_dim": "#4B427E",

    # Borders
    "border": "#282738",
    "layout_border_focus": "#3b4252",
    "layout_border_normal": "#3b4252",
}

SIZES = {
    "groupbox": 24,
}

FONT = "JetBrainsMono Nerd Font"
FONT_BOLD = "JetBrainsMono Nerd Font Bold"

LAYOUT = {
    "border_width": 0,
    "margin": 9,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}
```

- [ ] **Step 4: Commit**

```bash
git add .config/qtile/themes/__init__.py .config/qtile/themes/cozy.py
git commit -m "feat(qtile): create themes module with cozy theme"
```

---

## Task 2: 提取其他 4 个主题颜色

**Files:**
- Create: `.config/qtile/themes/carbon.py`
- Create: `.config/qtile/themes/everforest.py`
- Create: `.config/qtile/themes/natura.py`
- Create: `.config/qtile/themes/sakura.py`

**Steps:**

- [ ] **Step 1: Create themes/carbon.py from Themes/Carbon/.config/qtile/config.py**

```python
# themes/carbon.py
# Colors extracted from Carbon theme (grayscale)
COLORS = {
    "bar_bg": "#333333",
    "bar_bg_alt": "#CCCCCC",
    "accent": "#555555",
    "group_active": "#555555",
    "group_block_highlight": "#333333",
    "group_highlight": "#CCCCCC",
    "text": "#CCCCCC",
    "text_dim": "#474747",
    "border": "#CCCCCC",
    "layout_border_focus": "#3b4252",
    "layout_border_normal": "#3b4252",
}

SIZES = {
    "groupbox": 24,
}

FONT = "JetBrainsMono Nerd Font"
FONT_BOLD = "JetBrainsMono Nerd Font Bold"

LAYOUT = {
    "border_width": 0,
    "margin": 9,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}
```

- [ ] **Step 2: Create themes/everforest.py**

```python
# themes/everforest.py
# Colors extracted from Everforest theme (green-tinted)
COLORS = {
    "bar_bg": "#232A2E",
    "bar_bg_alt": "#343F44",
    "accent": "#86918A",
    "group_active": "#86918A",
    "group_block_highlight": "#D3C6AA",
    "group_highlight": "#4B427E",
    "text": "#86918A",
    "text_dim": "#4B427E",
    "border": "#232A2E",
    "layout_border_focus": "#3b4252",
    "layout_border_normal": "#3b4252",
}

SIZES = {
    "groupbox": 24,
}

FONT = "JetBrainsMono Nerd Font"
FONT_BOLD = "JetBrainsMono Nerd Font Bold"

LAYOUT = {
    "border_width": 0,
    "margin": 9,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}
```

- [ ] **Step 3: Create themes/natura.py**

```python
# themes/natura.py
# Colors extracted from Natura theme (earth tones)
COLORS = {
    "bar_bg": "#0F1212",
    "bar_bg_alt": "#202222",
    "accent": "#607767",
    "group_active": "#607767",
    "group_block_highlight": "#B2BEBC",
    "group_highlight": "#202222",
    "text": "#607767",
    "text_dim": "#4B427E",
    "border": "#0F1212",
    "layout_border_focus": "#3b4252",
    "layout_border_normal": "#3b4252",
}

SIZES = {
    "groupbox": 24,
}

FONT = "JetBrainsMono Nerd Font"
FONT_BOLD = "JetBrainsMono Nerd Font Bold"

LAYOUT = {
    "border_width": 0,
    "margin": 9,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}
```

- [ ] **Step 4: Create themes/sakura.py**

```python
# themes/sakura.py
# Colors extracted from Sakura theme (pink/purple)
COLORS = {
    "bar_bg": "#282738",
    "bar_bg_alt": "#353446",
    "accent": "#E5B9C6",
    "group_active": "#E5B9C6",
    "group_block_highlight": "#CFB3E5",
    "group_highlight": "#4B427E",
    "text": "#E5B9C6",
    "text_dim": "#4B427E",
    "border": "#282738",
    "layout_border_focus": "#3b4252",
    "layout_border_normal": "#3b4252",
}

SIZES = {
    "groupbox": 23,  # Sakura uses fontsize=23 for groupbox
}

FONT = "JetBrainsMono Nerd Font"
FONT_BOLD = "JetBrainsMono Nerd Font Bold"

LAYOUT = {
    "border_width": 0,
    "margin": 9,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}
```

- [ ] **Step 5: Commit**

```bash
git add .config/qtile/themes/carbon.py .config/qtile/themes/everforest.py .config/qtile/themes/natura.py .config/qtile/themes/sakura.py
git commit -m "feat(qtile): add carbon, everforest, natura, sakura themes"
```

---

## Task 3: 创建 keys.py 共用按键绑定

**Files:**
- Create: `.config/qtile/keys.py`

**Steps:**

- [ ] **Step 1: Create keys.py with all keybindings from Carbon (95 keys)**

```python
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
```

- [ ] **Step 2: Append group switch keys after imports**

```python
# 在 keys.py 末尾添加（需要 Group 导入）
# from libqtile.config import Group
# groups = [Group(f"{i + 1}", label="") for i in range(8)]
# for i in groups:
#     BASE_KEYS.extend([
#         Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
#     ])
```

Note: Group keys 需要在 config.py 中生成，因为 Group 需要在 keys.py 之后才能引用。

- [ ] **Step 3: Commit**

```bash
git add .config/qtile/keys.py
git commit -m "feat(qtile): extract keybindings to keys.py"
```

---

## Task 4: 创建 widgets.py widget 工厂函数

**Files:**
- Create: `.config/qtile/widgets.py`

**Steps:**

- [ ] **Step 1: Create widgets.py with factory functions**

```python
# widgets.py
from libqtile import widget
from libqtile.lazy import lazy


def search():
    from libqtile import qtile
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/launcher")


def power():
    from libqtile import qtile
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


def make_groupbox(theme):
    return widget.GroupBox(
        font=theme["font"],
        fontsize=theme["sizes"]["groupbox"],
        borderwidth=3,
        highlight_method="block",
        active=theme["colors"]["group_active"],
        block_highlight_text_color=theme["colors"]["group_block_highlight"],
        highlight_color=theme["colors"]["group_highlight"],
        inactive=theme["colors"]["bar_bg"],
        foreground=theme["colors"]["text_dim"],
        background=theme["colors"]["bar_bg_alt"],
        this_current_screen_border=theme["colors"]["bar_bg_alt"],
        this_screen_border=theme["colors"]["bar_bg_alt"],
        other_current_screen_border=theme["colors"]["bar_bg_alt"],
        other_screen_border=theme["colors"]["bar_bg_alt"],
        urgent_border=theme["colors"]["bar_bg_alt"],
        rounded=True,
        disable_drag=True,
    )


def make_text_icon(text, background, foreground, fontsize=13, mouse_callback=None):
    kwargs = {
        "text": text,
        "font": "Font Awesome 6 Free Solid",
        "fontsize": fontsize,
        "background": background,
        "foreground": foreground,
        "padding": 3,
    }
    if mouse_callback:
        kwargs["mouse_callbacks"] = {"Button1": mouse_callback}
    return widget.TextBox(**kwargs)


def make_bar_widgets(theme):
    """Build the widget list for the top bar."""
    c = theme["colors"]
    sz = theme["sizes"]

    return [
        widget.Spacer(length=15, background=c["bar_bg"]),

        # Launch icon
        widget.Image(
            filename="~/.config/qtile/Assets/launch_Icon.png",
            margin=2,
            background=c["bar_bg"],
            mouse_callbacks={"Button1": power},
        ),

        # Separator
        widget.Image(filename="~/.config/qtile/Assets/6.png"),

        # Group box
        widget.Spacer(length=8, background=c["bar_bg_alt"]),
        make_groupbox(theme),

        widget.Spacer(length=8, background=c["bar_bg_alt"]),
        widget.Image(filename="~/.config/qtile/Assets/1.png"),

        # Current layout icon
        widget.CurrentLayout(
            mode="icon",
            custom_icon_paths=["~/.config/qtile/Assets/layout"],
            background=c["bar_bg_alt"],
            scale=0.50,
        ),

        widget.Image(filename="~/.config/qtile/Assets/5.png"),

        # Search
        make_text_icon(" ", c["bar_bg"], c["accent"], mouse_callback=search),
        widget.TextBox(
            fmt="Search",
            background=c["bar_bg"],
            font=theme["font_bold"],
            fontsize=13,
            foreground=c["accent"],
            mouse_callbacks={"Button1": search},
        ),

        widget.Image(filename="~/.config/qtile/Assets/4.png"),

        # Window name
        widget.WindowName(
            background=c["bar_bg_alt"],
            font=theme["font_bold"],
            fontsize=13,
            empty_group_string="Desktop",
            max_chars=130,
            foreground=c["accent"],
        ),

        widget.Image(filename="~/.config/qtile/Assets/3.png"),

        # Systray
        widget.Systray(background=c["bar_bg"], fontsize=2),
        widget.TextBox(text=" ", background=c["bar_bg"]),

        # Memory
        widget.Image(filename="~/.config/qtile/Assets/6.png", background=c["bar_bg_alt"]),
        make_text_icon("", c["bar_bg_alt"], c["accent"]),
        widget.Memory(
            background=c["bar_bg_alt"],
            format="{MemUsed: .0f}{mm}",
            foreground=c["accent"],
            font=theme["font_bold"],
            fontsize=13,
            update_interval=5,
        ),

        widget.Image(filename="~/.config/qtile/Assets/2.png"),
        widget.Spacer(length=8, background=c["bar_bg_alt"]),

        # Battery
        make_text_icon(" ", c["bar_bg_alt"], c["accent"]),
        widget.Battery(
            font=theme["font_bold"],
            fontsize=13,
            background=c["bar_bg_alt"],
            foreground=c["accent"],
            format="{percent:2.0%}",
        ),

        widget.Image(filename="~/.config/qtile/Assets/2.png"),
        widget.Spacer(length=8, background=c["bar_bg_alt"]),

        # Volume
        make_text_icon(" ", c["bar_bg_alt"], c["accent"]),
        widget.Volume(
            font=theme["font_bold"],
            fontsize=13,
            background=c["bar_bg_alt"],
            foreground=c["accent"],
            mute_command="pamixer --toggle-mute",
            volume_up_command="pamixer -i 5",
            volume_down_command="pamixer -d 5",
            get_volume_command="pamixer --get-volume-human",
            update_interval=0.2,
            unmute_format="{volume}%",
            mute_format="M",
        ),

        widget.Image(filename="~/.config/qtile/Assets/5.png", background=c["bar_bg_alt"]),

        # Clock
        make_text_icon(" ", c["bar_bg"], c["accent"]),
        widget.Clock(
            format="%I:%M %p",
            background=c["bar_bg"],
            foreground=c["accent"],
            font=theme["font_bold"],
            fontsize=13,
        ),

        widget.Spacer(length=18, background=c["bar_bg"]),
    ]
```

- [ ] **Step 2: Commit**

```bash
git add .config/qtile/widgets.py
git commit -m "feat(qtile): extract widgets to factory functions"
```

---

## Task 5: 重写 config.py

**Files:**
- Modify: `.config/qtile/config.py`

**Steps:**

- [ ] **Step 1: Create new config.py using the modules**

```python
# config.py
from libqtile import bar, hook, layout, qtile, widget
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
dgroups_app_rules = []
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

import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser(".config/qtile/autostart_once.sh")])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
```

- [ ] **Step 2: Commit**

```bash
git add .config/qtile/config.py
git commit -m "refactor(qtile): use themes/keys/widgets modules"
```

---

## Task 6: 更新 theme_switcher 脚本

**Files:**
- Modify: `.config/rofi/scripts/theme_switcher`

**Steps:**

- [ ] **Step 1: Update theme_switcher to write .current_theme file**

```bash
#!/bin/bash
# theme_switcher - Interactive theme switcher for Qtile

THEMES_DIR="$HOME/.config/qtile/themes"
CONFIG_FILE="$HOME/.config/qtile/.current_theme"

# Get list of available themes
mapfile -t THEMES < <(ls "$THEMES_DIR"/*.py 2>/dev/null | xargs -n1 basename | sed 's/\.py$//' | grep -v __init__)

if [ ${#THEMES[@]} -eq 0 ]; then
    echo "No themes found in $THEMES_DIR"
    exit 1
fi

# Use rofi to select theme
SELECTED=$(printf '%s\n' "${THEMES[@]}" | rofi -dmenu -p "Select Theme" -theme ~/.config/rofi/config.rasi)

if [ -z "$SELECTED" ]; then
    exit 0
fi

# Write current theme
echo "$SELECTED" > "$CONFIG_FILE"

# Restart Qtile to apply
qtile cmd-obj -o cmd -f restart
```

- [ ] **Step 2: Commit**

```bash
git add .config/rofi/scripts/theme_switcher
git commit -m "refactor(qtile): theme_switcher writes .current_theme"
```

---

## Task 7: 验证配置

**Steps:**

- [ ] **Step 1: Syntax check**

```bash
python3 -c "import sys; sys.path.insert(0, '$HOME/.config/qtile'); import config"
```

- [ ] **Step 2: Reload config in Qtile**

```bash
qtile cmd-obj -o cmd -f reload_config
```

- [ ] **Step 3: Visual verification - check bar colors match theme**

- [ ] **Step 4: Commit remaining changes if any**

---

## Spec Coverage Check

- [x] 颜色变量化 → themes/*.py 每个主题导出 COLORS 字典
- [x] 组件抽象化 → widgets.py 工厂函数 make_groupbox, make_bar_widgets
- [x] 按键绑定共用化 → keys.py BASE_KEYS
- [x] 主题切换流程 → theme_switcher 写 .current_theme
- [x] 不改变 widget 顺序
- [x] 不改变布局配置
- [x] 不改变 bar margin/border_width
