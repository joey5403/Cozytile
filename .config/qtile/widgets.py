# widgets.py
from libqtile import widget


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
