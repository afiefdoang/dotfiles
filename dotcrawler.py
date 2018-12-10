#!/usr/bin/env python

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
mainDir = '~/git/dotfiles'
etcDir = '~/git/dotfiles/etc'
usrDir = '~/git/dotfiles/usr'
configDir = '~/git/dotfiles/.config'
irssiDir = '~/git/dotfiles/.irssi'
localDir = '~/git/dotfiles/.local'
vimDir = '~/git/dotfiles/.vim'
ohMyZshDir = '~/git/dotfiles/.oh-my-zsh'
imageDir = '~/git/dotfiles/images'

# Proces Copy to GitHub Directory
os.system(f'''
# -----------------------------------------------------------------------------
##### Create main Directory
# -----------------------------------------------------------------------------
mkdir -p {mainDir}

echo '[ DONE ] Create main directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Content from $HOME Directory
# -----------------------------------------------------------------------------
cp ~/.gtkrc-2.0 {mainDir}
cp ~/.mailcap {mainDir}
cp ~/.ncpamixer.conf {mainDir}
cp ~/.profile {mainDir}
cp ~/.tmux.conf {mainDir}
cp ~/.vimrc {mainDir}
cp ~/.xinitrc {mainDir}
cp ~/.Xmodmap {mainDir}
cp ~/.Xresources {mainDir}
cp ~/.zshrc {mainDir}

echo '[ DONE ] Copy dotfiles from /home user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Content from /etc Directory
# -----------------------------------------------------------------------------
# LIGHTDM
mkdir -p {etcDir}/lightdm
cp /etc/lightdm/lightdm.conf {etcDir}/lightdm
cp /etc/lightdm/slick-greeter.conf {etcDir}/lightdm

# PAM
mkdir -p {etcDir}/pam.d
cp /etc/pam.d/i3lock {etcDir}/pam.d
cp /etc/pam.d/login {etcDir}/pam.d
cp /etc/pam.d/polkit-1 {etcDir}/pam.d
cp /etc/pam.d/sudo {etcDir}/pam.d

# X11
mkdir -p {etcDir}/X11/xorg.conf.d
cp /etc/X11/xorg.conf.d/20-intel.conf {etcDir}/X11/xorg.conf.d

echo '[ DONE ] Copy dotfiles from /etc directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Content from .config Directory
# -----------------------------------------------------------------------------
mkdir -p {configDir}

cp -r ~/.config/compton {configDir}
cp -r ~/.config/i3 {configDir}
cp -r ~/.config/ncmpcpp {configDir}
cp -r ~/.config/nvim {configDir}
cp -r ~/.config/newsboat {configDir}
cp -r ~/.config/rofi {configDir}
cp -r ~/.config/rofi-power {configDir}
cp -r ~/.config/termite {configDir}
cp -r ~/.config/urxvt {configDir}
cp -r ~/.config/urxvtconfig {configDir}

cp ~/.config/gtkrc {configDir}
cp ~/.config/gtkrc-2.0 {configDir}
cp ~/.config/mimeapps.list {configDir}
cp ~/.config/user-dirs.conf {configDir}
cp ~/.config/user-dirs.dirs {configDir}
cp ~/.config/user-dirs.locale {configDir}

# CONKY
mkdir -p {configDir}/conky
cp -r ~/.config/conky/conkyrc {configDir}conky

# DUNST
mkdir -p {configDir}/dunst
cp ~/.config/dunst/dunstrc-dark {configDir}/dunst
cp ~/.config/dunst/dunstrc-light {configDir}/dunst

# GTK3
#mkdir -p {configDir}/gtk-3.0
#cp ~/.config/gtk-3.0/bookmarks {configDir}/gtk-3.0
#cp ~/.config/gtk-3.0/settings.ini {configDir}/gtk-3.0

# MPD
mkdir -p {configDir}/mpd
cp ~/.config/mpd/mpd.conf {configDir}/mpd

# MPV
mkdir -p {configDir}/mpv
cp ~/.config/mpv/mpv.conf {configDir}/mpv
cp ~/.config/mpv/input.conf {configDir}/mpv

# MUTT
mkdir -p {configDir}/mutt
cp ~/.config/mutt/mutt-colors-solarized/mutt-colors-solarized-dark-16.muttrc \
{configDir}/mutt
cp ~/.config/mutt/muttrc {configDir}/mutt

# POLYBAR
mkdir -p {configDir}/polybar
cp ~/.config/polybar/config-dark {configDir}/polybar
cp ~/.config/polybar/config-light {configDir}/polybar
cp ~/.config/polybar/launch.sh {configDir}/polybar

# RANGER
mkdir -p {configDir}/ranger
cp -r ~/.config/ranger/colorschemes {configDir}/ranger
cp ~/.config/ranger/commands.py {configDir}/ranger
cp ~/.config/ranger/commands_full.py {configDir}/ranger
cp ~/.config/ranger/rc.conf {configDir}/ranger
cp ~/.config/ranger/rifle.conf {configDir}/ranger
cp ~/.config/ranger/scope.sh {configDir}/ranger

echo '[ DONE ] Copy dotfiles from ~/.config user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Content from .local Directory
# -----------------------------------------------------------------------------
mkdir -p {localDir}/bin
cp ~/.local/bin/lock-dark {localDir}/bin
cp ~/.local/bin/lock-light {localDir}/bin
cp ~/.local/bin/rofi-power {localDir}/bin
cp ~/.local/bin/postbanner {localDir}/bin

# APPLICATION DESKTOP CONFIG FILES
mkdir -p {localDir}/share
cp -r ~/.local/share/applications {localDir}/share

echo '[ DONE ] Copy dotfiles from ~/.local user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Content from .vim Directory
# -----------------------------------------------------------------------------
mkdir -p {vimDir}
cp -r ~/.vim/autoload {vimDir}

mkdir -p {vimDir}/colors
cp ~/.vim/colors/solarized-bandit.vim {vimDir}/colors

mkdir -p {vimDir}/plugged/vim-airline-themes/autoload/airline/themes
cp ~/.vim/plugged/vim-airline-themes/autoload/airline/themes/solarized_bandit.\
vim {vimDir}/plugged/vim-airline-themes/autoload/airline/themes

echo '[ DONE ] Copy dotfiles from ~/.vim user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Content from .oh-my-zsh Directory
# -----------------------------------------------------------------------------
mkdir -p {ohMyZshDir}/themes
cp ~/.oh-my-zsh/themes/avit-bandit.zsh-theme {ohMyZshDir}/themes
cp ~/.oh-my-zsh/themes/bureau-bandit.zsh-theme {ohMyZshDir}/themes

echo '[ DONE ] Copy dotfiles from ~/.oh-my-zsh user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Content from .irssi
# -----------------------------------------------------------------------------
mkdir -p {irssiDir}/scripts/autorun
cp ~/.irssi/scripts/autorun/notify.pl {irssiDir}/scripts/autorun
cp ~/.irssi/scripts/nicklist-portable.pl {irssiDir}/scripts
cp ~/.irssi/scripts/notify.pl {irssiDir}/scripts

mkdir -p {irssiDir}
cp ~/.irssi/config {irssiDir}
cp ~/.irssi/solarized-bandit.theme {irssiDir}

echo '[ DONE ] Copy dotfiles from ~/.irssi user directory'
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Update List of arch Packages
# -----------------------------------------------------------------------------
pacman -Qqe > .listapp
# -----------------------------------------------------------------------------
''')


# Print Output ----------------------------------------------------------------
print(f'''
d8888b.  .d88b.  d8b   db d88888b db
88  `8D .8P  Y8. 888o  88 88'     88
88   88 88    88 88V8o 88 88ooooo YP
88   88 88    88 88 V8o88 88~~~~~
88  .8D `8b  d8' 88  V888 88.     db
Y8888D'  `Y88P'  VP   V8P Y88888P YP
''')
print('\n>> CRAWLING PROCESS COMPLETED !!')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
