#!/usr/bin/python3.6

#  ██████                           ██ ██   ██   ██      ██ ██    ██
# ░█░░░░██                         ░██░░   ░██  ░██     ░██░░    ░░
# ░█   ░██   ██████   ███████      ░██ ██ ██████░██     ░██ ██    ██  ██████
# ░██████   ░░░░░░██ ░░██░░░██  ██████░██░░░██░ ░██████████░██   ░██ ██░░░░██
# ░█░░░░ ██  ███████  ░██  ░██ ██░░░██░██  ░██  ░██░░░░░░██░██   ░██░██   ░██
# ░█    ░██ ██░░░░██  ░██  ░██░██  ░██░██  ░██  ░██     ░██░██ ██░██░██   ░██
# ░███████ ░░████████ ███  ░██░░██████░██  ░░██ ░██     ░██░██░░███ ░░██████
# ░░░░░░░   ░░░░░░░░ ░░░   ░░  ░░░░░░ ░░    ░░  ░░      ░░ ░░  ░░░   ░░░░░░
#
#                                          ██
#                                         ░██
#      █████  ██████  ██████   ███     ██ ░██  █████  ██████
#     ██░░░██░░██░░█ ░░░░░░██ ░░██  █ ░██ ░██ ██░░░██░░██░░█
#    ░██  ░░  ░██ ░   ███████  ░██ ███░██ ░██░███████ ░██ ░
#  ██░██   ██ ░██    ██░░░░██  ░████░████ ░██░██░░░░  ░██
# ░██░░█████ ░███   ░░████████ ███░ ░░░██ ███░░██████░███
# ░░  ░░░░░  ░░░     ░░░░░░░░ ░░░    ░░░ ░░░  ░░░░░░ ░░░

# author : BanditHijo
# source : https://github.com/bandithijo/dotfiles

import os

# Deklarasi Variabel Directory
mainDir   = '~/git/dotfiles'
etcDir    = '~/git/dotfiles/etc'
usrDir    = '~/git/dotfiles/usr'
configDir = '~/git/dotfiles/.config'
localDir  = '~/git/dotfiles/.local'
urxvtDir  = '~/git/dotfiles/.urxvt'
vimDir    = '~/git/dotfiles/.vim'
imageDir  = '~/git/dotfiles/images'

# Proces Copy to GitHub Directory
os.system(f'''
# -----------------------------------------------------------------------------
##### Make main Directory
# -----------------------------------------------------------------------------
mkdir -p {mainDir}
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From $HOME Directory
# -----------------------------------------------------------------------------
cp ~/.gtkrc-2.0 {mainDir}
cp ~/.profile {mainDir}
cp ~/.tmux.conf {mainDir}
cp ~/.vimrc {mainDir}
cp ~/.Xresources {mainDir}
cp ~/.xinitrc {mainDir}
cp ~/.zshrc {mainDir}
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From /etc Directory
# -----------------------------------------------------------------------------
mkdir -p {etcDir}/lightdm
cp /etc/lightdm/lightdm.conf {etcDir}/lightdm
cp /etc/lightdm/slick-greeter.conf {etcDir}/lightdm

mkdir -p {etcDir}/pam.d
cp /etc/pam.d/i3lock {etcDir}/pam.d
cp /etc/pam.d/login {etcDir}/pam.d
cp /etc/pam.d/polkit-1 {etcDir}/pam.d
cp /etc/pam.d/sudo {etcDir}/pam.d

mkdir -p {etcDir}/X11/xorg.conf.d
cp /etc/X11/xorg.conf.d/20-intel.conf {etcDir}/X11/xorg.conf.d
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From /usr Directory
# -----------------------------------------------------------------------------
mkdir -p {usrDir}/lib/libreoffice/program
sudo cp /usr/lib/libreoffice/program/intro.png {usrDir}/lib/libreoffice/program
sudo cp /usr/lib/libreoffice/program/sofficerc {usrDir}/lib/libreoffice/program
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .config Directory
# -----------------------------------------------------------------------------
mkdir -p {configDir}

cp ~/.config/user-dirs.dirs {configDir}
cp ~/.config/user-dirs.conf {configDir}

cp -r ~/.config/compton {configDir}
cp -r ~/.config/dunst {configDir}
cp -r ~/.config/i3 {configDir}
cp -r ~/.config/rofi-power {configDir}
cp -r ~/.config/nvim {configDir}
cp -r ~/.config/rofi {configDir}
cp -r ~/.config/urxvt {configDir}

mkdir -p {configDir}/gtk-3.0
cp ~/.config/gtk-3.0/bookmarks {configDir}/gtk-3.0
cp ~/.config/gtk-3.0/settings.ini {configDir}/gtk-3.0
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .conky Directory
# -----------------------------------------------------------------------------
cp -r ~/.conky {mainDir}
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .local Directory
# -----------------------------------------------------------------------------
mkdir -p {localDir}/bin
cp ~/.local/bin/rofi-power {localDir}/bin
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .vim Directory
# -----------------------------------------------------------------------------
mkdir -p {vimDir}
cp -r ~/.vim/autoload {vimDir}

mkdir -p {vimDir}/colors
cp ~/.vim/colors/Monokai-Bandit.vim {vimDir}/colors
cp ~/.vim/colors/solarized-bandit.vim {vimDir}/colors
cp ~/.vim/colors/Tomorrow-Night-Bandit.vim {vimDir}/colors
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From bumblebee-status Directory
# -----------------------------------------------------------------------------
mkdir -p {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/brightness.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/title.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/pulseaudio.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/nic.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/memory.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/sensors.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/battery0.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/battery1.py {configDir}/bumblebee-status/bumblebee/modules
cp ~/.config/bumblebee-status/bumblebee/modules/profile.py {configDir}/bumblebee-status/bumblebee/modules

mkdir -p {configDir}/bumblebee-status/themes
cp ~/.config/bumblebee-status/themes/gruvbox-powerline-bandit-solarized.json {configDir}/bumblebee-status/themes

mkdir -p {configDir}/bumblebee-status/themes/icons
cp ~/.config/bumblebee-status/themes/icons/awesome-fonts-bandit.json {configDir}/bumblebee-status/themes/icons
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Update List of arch Packages
# -----------------------------------------------------------------------------
pacman -Qqe > .listapp
# -----------------------------------------------------------------------------
''')


# Print Output ----------------------------------------------------------------
print('CRAWLING PROCESS COMPLETED !!')

