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
imageDir  = '~/GitHub/dotfiles/images'
usrDir    = '~/GitHub/dotfiles/usr'

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
##### From .config Directory
# -----------------------------------------------------------------------------
mkdir -p {configDir}

cp ~/.config/user-dirs.dirs {configDir}
cp ~/.config/user-dirs.conf {configDir}

cp -r ~/.config/compton {configDir}
cp -r ~/.config/dunst {configDir}
cp -r ~/.config/i3 {configDir}
cp -r ~/.config/nvim {configDir}
cp -r ~/.config/rofi {configDir}

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
##### From .urxvt Directory
# -----------------------------------------------------------------------------
mkdir -p {urxvtDir}
cp -r ~/.urxvt/ext {urxvtDir}
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
##### From Wallpaper
# -----------------------------------------------------------------------------
#mkdir -p {imageDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11.xcf {imageDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11.png {imageDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11L.png {imageDir}
#cp ~/pix/Wallpapers/archWallpaper/Arch-Wallpaper-11LL.png {imageDir}
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### From /usr Directory
# -----------------------------------------------------------------------------
mkdir -p {usrDir}/lib/libreoffice/program
sudo cp /usr/lib/libreoffice/program/intro.png {imageDir}
sudo cp /usr/lib/libreoffice/program/sofficerc {usrDir}/lib/libreoffice/program
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
##### Update List of arch Packages
# -----------------------------------------------------------------------------
pacman -Qqe > .listapp
# -----------------------------------------------------------------------------
''')


# Print Output ----------------------------------------------------------------
print('CRAWLING PROCESS COMPLETED !!')

