# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Cozytile is an Arch Linux "rice" (desktop configuration/dotfiles) built around Qtile window manager. It automates installation of a full desktop environment including compositor, terminal, launcher, shell, notifications, file manager, display manager, and audio visualization.

## Common Commands

### Installation
```sh
./install.sh
```
The installer is interactive and handles:
1. Device type selection (laptop/PC) - patches Qtile config for battery vs network widgets
2. AUR helper setup (yay/paru)
3. All dependencies and fonts
4. GPU driver selection (Intel/AMD/NVIDIA)
5. Shell configuration
6. Theme installation
7. Wallpaper color cache preloading with pywal

### Manual Deployment
```sh
# Install dependencies (Arch Linux)
paru -S --needed qtile python-psutil pywal-git qt5-graphicaleffects dunst starship mpd ncmpcpp playerctl brightnessctl alacritty pfetch htop flameshot thunar roficlip rofi ranger cava neovim vim feh qt6-5compat qt6-declarative qt6-svg pipewire pipewire-pulse pamixer ttf-jetbrains-mono-nerd ttf-hack-nerd ttf-font-awesome ttf-firacode-nerd ttf-icomoon-feather

# Copy configs
cp -ra .config/* ~/.config/
cp -ra Wallpaper ~/
cp -ra Themes ~/

# Preload wallpaper cache
wal -i ~/Wallpaper/Aesthetic2.png
```

## Architecture

### Config Structure
```
.config/
├── qtile/config.py      # Main Qtile config (window manager)
├── rofi/                # App launcher, powermenu, theme switcher
├── dunst/               # Notification daemon
├── alacritty/           # Terminal config (TOML)
├── cava/                # Audio visualizer
├── starship.toml        # Shell prompt
├── spicetify/           # Spotify theme
├── fontconfig/fonts.conf
└── nvim/lua/            # Neovim config (chadrc theme system)
Themes/                  # Extra theme configs
Wallpaper/               # Wallpapers for pywal
```

### Key Configs
- **Qtile** (`.config/qtile/config.py`): Window manager with BSP/Columns/Floating/Max layouts, 8 workspaces, keyboard-driven navigation using vim-like bindings (h/j/k/l with mod=super)
- **Rofi** (`.config/rofi/scripts/`): Launcher, powermenu, and theme switcher scripts
- **Dynamic theming**: pywal extracts colors from wallpaper and themes the entire system

### Device-Specific Patching
The installer uses Python regex to swap battery widget (laptop) with network widget (PC) across all config.py files. The patterns it looks for:
- Battery widget: `widget.Battery(format="{percent:2.0%}")`
- Net widget: `widget.Net(format=' {up}{up_suffix}  {down}{down_suffix}')`

