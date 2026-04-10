# Qtile Theme Refactor Design

## Goal

重构 Qtile 配置，将颜色变量化、组件抽象化、按键绑定共用化，使主题切换更简单高效。

## Current State

- 5 个主题：`Cozy`、`Carbon`、`Everforest`、`Natura`、`Sakura`
- 每个主题包含完整 `config.py`（约 450 行）
- 主题间差异：仅颜色值不同，结构完全一致
- 按键绑定 95 条，Carbon/Everforest 多 2 条 Alt+Tab 绑定

## Architecture

```
.config/qtile/
├── config.py          # 主配置（颜色来自主题字典）
├── themes/
│   ├── __init__.py   # 主题加载逻辑
│   ├── cozy.py       # 颜色配置字典
│   ├── carbon.py
│   ├── everforest.py
│   ├── natura.py
│   └── sakura.py
└── theme_switcher    # 切换脚本
```

## Design

### 1. 主题配置结构

每个主题文件导出颜色字典：

```python
# themes/cozy.py
COLORS = {
    # Bar 背景色
    "bar_bg": "#282738",
    "bar_bg_alt": "#353446",

    # 强调色（用于文字、图标、active 状态）
    "accent": "#CAA9E0",

    # GroupBox 特定
    "group_active": "#CAA9E0",
    "group_block_highlight": "#91B1F0",
    "group_highlight": "#353446",

    # 文字色
    "text": "#CAA9E0",
    "text_dim": "#4B427E",

    # 系统托盘/边框
    "border": "#282738",

    # 布局边框
    "layout_border_focus": "#3b4252",
    "layout_border_normal": "#3b4252",
}
```

### 2. 主题加载逻辑

```python
# themes/__init__.py
import os

def get_current_theme():
    theme_file = os.path.expanduser("~/.config/qtile/.current_theme")
    if os.path.exists(theme_file):
        with open(theme_file) as f:
            theme_name = f.read().strip()
    else:
        theme_name = "cozy"  # 默认主题

    # 动态导入主题模块
    from importlib import import_module
    return import_module(f"themes.{theme_name}").COLORS
```

### 3. 组件工厂函数

封装重复的 widget 创建逻辑：

```python
# widgets.py
def make_groupbox(theme):
    return widget.GroupBox(
        font="JetBrainsMono Nerd Font",
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
```

### 4. 按键绑定共用化

以 Carbon/Everforest 的完整绑定为准（95 条），独立文件：

```python
# keys.py
BASE_KEYS = [
    # 布局导航
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # ... 更多按键
    # Alt+Tab 窗口切换（从 Carbon 补充）
    Key(["mod1"], "Tab", lazy.group.next_window(), desc="Cycle to next window"),
    Key(["mod1", "shift"], "Tab", lazy.group.prev_window(), desc="Cycle to previous window"),
]

# Group 切换按键动态生成
groups = [Group(f"{i + 1}", label="") for i in range(8)]
for i in groups:
    BASE_KEYS.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])
```

### 5. 主配置结构

```python
# config.py
from themes import get_current_theme

THEME = get_current_theme()
from keys import BASE_KEYS
from widgets import make_bar_widgets

keys = BASE_KEYS

layouts = [
    layout.Bsp(**THEME["layout"]),
    layout.Columns(**THEME["layout"]),
    layout.Floating(**THEME["layout"]),
    layout.Max(**THEME["layout"]),
]

screens = [
    Screen(top=bar.Bar(make_bar_widgets(THEME), 30, ...)),
]

floating_layout = layout.Floating(
    border_focus=THEME["colors"]["layout_border_focus"],
    border_normal=THEME["colors"]["layout_border_normal"],
    ...
)
```

### 6. 主题切换脚本

```bash
#!/bin/bash
# config/rofi/scripts/theme_switcher
THEME_NAME=$(ls ~/.config/qtile/themes/ | head -n ...)
echo "$THEME_NAME" > ~/.config/qtile/.current_theme
wal -i ~/Wallpaper/your_wallpaper.jpg
qtile cmd-obj -o cmd -f restart
```

## 验证方式

1. **语法检查**：`python3 -c "import config"`
2. **热重载**：`qtile cmd-obj -o cmd -f reload_config`
3. **视觉验证**：观察 bar 颜色、字体、widget 排列是否正确

## 实现顺序

1. 提取主题颜色到独立文件
2. 创建 `themes/__init__.py` 加载逻辑
3. 提取按键绑定到 `keys.py`
4. 创建 widget 工厂函数到 `widgets.py`
5. 重写 `config.py` 使用上述模块
6. 更新 theme_switcher 脚本
7. 逐主题验证（Cozy → Carbon → Everforest → Natura → Sakura）

## 约束

- 不改变 widget 的排列顺序（保持与当前一致）
- 不改变布局配置（layouts 列表保持不变）
- 不改变 bar 的 margin、border_width 等几何参数
- 仅将硬编码颜色替换为变量引用
