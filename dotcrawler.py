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
#
# author : BanditHijo
# source : https://github.com/bandithijo/dotfiles
#
# Copyright (C) 2018 BanditHijo
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see http://www.gnu.org/licenses/.


import os

# Deklarasi Variabel Directory
mainDir   = '~/git/dotfiles'
etcDir    = '~/git/dotfiles/etc'
usrDir    = '~/git/dotfiles/usr'
configDir = '~/git/dotfiles/.config'
localDir  = '~/git/dotfiles/.local'
urxvtDir  = '~/git/dotfiles/.urxvt'
vimDir    = '~/git/dotfiles/.vim'
ohMyZshDir= '~/git/dotfiles/.oh-my-zsh'
imageDir  = '~/git/dotfiles/images'

# Proces Copy to GitHub Directory
os.system(f'''
# -----------------------------------------------------------------------------
##### Make main Directory
# -----------------------------------------------------------------------------
mkdir -p {mainDir}

echo '[ DONE ] Make main directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From $HOME Directory
# -----------------------------------------------------------------------------
cp ~/.gtkrc-2.0 {mainDir}
cp ~/.profile {mainDir}
cp ~/.tmux.conf {mainDir}
cp ~/.mailcap {mainDir}
cp ~/.muttrc {mainDir}
cp ~/.vimrc {mainDir}
cp ~/.Xresources {mainDir}
cp ~/.xinitrc {mainDir}
cp ~/.zshrc {mainDir}

echo '[ DONE ] Copy dotfiles from /home user directory'
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

echo '[ DONE ] Copy dotfiles from /etc directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From /usr Directory
# -----------------------------------------------------------------------------
#mkdir -p {usrDir}/lib/libreoffice/program
#sudo cp /usr/lib/libreoffice/program/intro.png {usrDir}/lib/libreoffice/program
#sudo cp /usr/lib/libreoffice/program/sofficerc {usrDir}/lib/libreoffice/program

#echo '[ DONE ] Copy dotfiles from /usr directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .config Directory
# -----------------------------------------------------------------------------
mkdir -p {configDir}

cp -r ~/.config/compton {configDir}
cp -r ~/.config/dunst {configDir}
cp -r ~/.config/i3 {configDir}
cp -r ~/.config/rofi-power {configDir}
cp -r ~/.config/nvim {configDir}
cp -r ~/.config/rofi {configDir}
cp -r ~/.config/urxvt {configDir}
cp -r ~/.config/xfce4 {configDir}

#cp ~/.config/user-dirs.dirs {configDir}
#cp ~/.config/user-dirs.conf {configDir}

#mkdir -p {configDir}/gtk-3.0
#cp ~/.config/gtk-3.0/bookmarks {configDir}/gtk-3.0
#cp ~/.config/gtk-3.0/settings.ini {configDir}/gtk-3.0

mkdir -p {configDir}/mpv
cp ~/.config/mpv/mpv.conf {configDir}/mpv
cp ~/.config/mpv/input.conf {configDir}/mpv

mkdir -p {configDir}/mutt
cp ~/.config/mutt/account.com.gmail.bandithijo {configDir}/mutt

echo '[ DONE ] Copy dotfiles from ~/.config user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .conky Directory
# -----------------------------------------------------------------------------
cp -r ~/.conky {mainDir}

echo '[ DONE ] Copy dotfiles from ~/.conky user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .local Directory
# -----------------------------------------------------------------------------
mkdir -p {localDir}/bin
cp ~/.local/bin/rofi-power {localDir}/bin

echo '[ DONE ] Copy dotfiles from ~/.local user directory'
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

mkdir -p {vimDir}/plugged/vim-airline-themes/autoload/airline/themes
cp ~/.vim/plugged/vim-airline-themes/autoload/airline/themes/solarized_bandit.vim {vimDir}/plugged/vim-airline-themes/autoload/airline/themes

echo '[ DONE ] Copy dotfiles from ~/.vim user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From .oh-my-zsh Directory
# -----------------------------------------------------------------------------
mkdir -p {ohMyZshDir}/themes
cp ~/.oh-my-zsh/themes/avit-bandit.zsh-theme {ohMyZshDir}/themes
cp ~/.oh-my-zsh/themes/bureau-bandit.zsh-theme {ohMyZshDir}/themes

echo '[ DONE ] Copy dotfiles from ~/.oh-my-zsh user directory'
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
cp ~/.config/bumblebee-status/themes/gruvbox-powerline-bandit-black.json {configDir}/bumblebee-status/themes
cp ~/.config/bumblebee-status/themes/gruvbox-powerline-bandit-blue.json {configDir}/bumblebee-status/themes
cp ~/.config/bumblebee-status/themes/gruvbox-powerline-bandit-blue-nosymbol.json {configDir}/bumblebee-status/themes
cp ~/.config/bumblebee-status/themes/gruvbox-powerline-bandit-solarized.json {configDir}/bumblebee-status/themes

mkdir -p {configDir}/bumblebee-status/themes/icons
cp ~/.config/bumblebee-status/themes/icons/awesome-fonts-bandit.json {configDir}/bumblebee-status/themes/icons
cp ~/.config/bumblebee-status/themes/icons/awesome-fonts-bandit-nosymbol.json {configDir}/bumblebee-status/themes/icons

echo '[ DONE ] Copy dotfiles from ~/.config/bumblebee-status user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Update List of arch Packages
# -----------------------------------------------------------------------------
pacman -Qqe > .listapp
# -----------------------------------------------------------------------------
''')


# Print Output ----------------------------------------------------------------
print('\n>> CRAWLING PROCESS COMPLETED !!')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
