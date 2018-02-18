#!/usr/bin/python3.6

# author : BanditHijo
# source : https://github.com/bandithijo/dotfiles

import os

# Deklarasi Variabel Directory
mainDir   = '~/GitHub/dotfiles'
etcDir    = '~/GitHub/dotfiles/etc'
configDir = '~/GitHub/dotfiles/.config'
vimDir    = '~/GitHub/dotfiles/.vim'
urxvtDir  = '~/GitHub/dotfiles/.urxvt'
wallpDir  = '~/GitHub/dotfiles/wallpaper'

# Proces Copy to GitHub Directory
os.system(f'''
# Make main Directory --------------------------------------------------------
mkdir -p {mainDir}
# ----------------------------------------------------------------------------

# From $HOME Directory -------------------------------------------------------
cp ~/.gtkrc-2.0 {mainDir}
cp ~/.profile {mainDir}
cp ~/.tmux.conf {mainDir}
cp ~/.vimrc {mainDir}
cp ~/.Xresources {mainDir}
cp ~/.xinitrc {mainDir}
cp ~/.zshrc {mainDir}
# ----------------------------------------------------------------------------

# From /etc Directory --------------------------------------------------------
mkdir -p {etcDir}/lightdm
cp /etc/lightdm/lightdm.conf {etcDir}/lightdm
cp /etc/lightdm/slick-greeter.conf {etcDir}/lightdm

mkdir -p {etcDir}/pam.d
cp /etc/pam.d/i3lock {etcDir}/pam.d
cp /etc/pam.d/polkit-1 {etcDir}/pam.d
cp /etc/pam.d/sudo {etcDir}/pam.d

mkdir -p {etcDir}/X11/xorg.conf.d
cp /etc/X11/xorg.conf.d/20-intel.conf {etcDir}/X11/xorg.conf.d
# ----------------------------------------------------------------------------

# From .config Directory -----------------------------------------------------
mkdir -p {configDir}/gtk-3.0
cp ~/.config/gtk-3.0/settings.ini {configDir}/gtk-3.0

mkdir -p {configDir}/i3
cp ~/.config/i3/compton.conf {configDir}/i3
cp ~/.config/i3/config {configDir}/i3
cp ~/.config/i3/dunstrc {configDir}/i3

cp -r ~/.config/nvim {configDir}

cp ~/.config/user-dirs.dirs {configDir}
# ----------------------------------------------------------------------------

# From .conky Directory ------------------------------------------------------
cp -r ~/.conky {mainDir}
# ----------------------------------------------------------------------------

# From .vim Directory --------------------------------------------------------
mkdir -p {vimDir}
cp -r ~/.vim/autoload {vimDir}

mkdir -p {vimDir}/colors
cp ~/.vim/colors/Monokai-Bandit.vim {vimDir}/colors
cp ~/.vim/colors/solarized-bandit.vim {vimDir}/colors
cp ~/.vim/colors/Tomorrow-Night-Bandit.vim {vimDir}/colors
# ----------------------------------------------------------------------------

# From .urxvt Directory ------------------------------------------------------
mkdir -p {urxvtDir}
cp -r ~/.urxvt/ext {urxvtDir}
# ----------------------------------------------------------------------------

# From bumblebee-status Directory --------------------------------------------
mkdir -p {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/brightness.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/title.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/pulseaudio.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/nic.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/memory.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/sensors.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/battery0.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/battery1.py {configDir}/i3/bumblebee-status/bumblebee/modules
cp ~/.config/i3/bumblebee-status/bumblebee/modules/profile.py {configDir}/i3/bumblebee-status/bumblebee/modules

mkdir -p {configDir}/i3/bumblebee-status/themes
cp ~/.config/i3/bumblebee-status/themes/gruvbox-powerline-bandit-solarized.json {configDir}/i3/bumblebee-status/themes

mkdir -p {configDir}/i3/bumblebee-status/themes/icons
cp ~/.config/i3/bumblebee-status/themes/icons/awesome-fonts-bandit.json {configDir}/i3/bumblebee-status/themes/icons
# ----------------------------------------------------------------------------

# From Wallpaper -------------------------------------------------------------
#mkdir -p {wallpDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11.xcf {wallpDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11.png {wallpDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11L.png {wallpDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11LL.png {wallpDir}
# ----------------------------------------------------------------------------

# Update List of arch Packages ------------------------------------------------
pacman -Qqe > .listapp
# ----------------------------------------------------------------------------
''')


# Print Output ----------------------------------------------------------------
print('PROCESS COMPLETED !!')

