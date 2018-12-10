# ARCH LINUX INSTALATION ON THINKPAD X61 DOCUMENTATION

root@archiso# wifi-menu
root@archiso# ping -c 5 archlinux.org
root@archiso# timedatectl set-ntp true
root@archiso# timedatectl set-timezone Asia/Makassar
root@archiso# timedatectl status
root@archiso# fdisk /dev/sda
root@archiso# mkfs.ext4 /dev/sda2
root@archiso# mount /dev/sda2 /mnt
root@archiso# pacstrap /mnt base base-devel
root@archiso# genfstab -U /mnt >> /mnt/etc/fstab
root@archiso# cat /mnt/etc/fstab
root@archiso# arch-chroot /mnt

[root@archiso]# ln -sf /usr/share/zoneinfo/Asia/Makassar /etc/localtime
[root@archiso]# hwclock --systohc
[root@archiso]# vi /etc/locale.gen
en_US.UTF-8 UTF-8
[root@archiso]# locale-gen
[root@archiso]# vi /etc/locale.conf
LANG=en_US.UTF-8
[root@archiso]# vi /etc/hostname
BanditHijo-X61
[root@archiso]# vi /ets/hosts
127.0.0.1	localhost
::1		localhost
127.0.1.1	BanditHijo-X61  BanditHijo-X61
[root@archiso]# mkinitcpio -p linux
[root@archiso]# pacman -S grub
[root@archiso]# grub-install --target=i386-pc /dev/sda
[root@archiso]# pacman -S intel-ucode
[root@archiso]# grub-mkconfig -o /boot/grub/grub.cfg
[root@archiso]# vi /boot/grub/grub.cfg
hapus quiet pada kernel parameter

[root@archiso]# pacman -S xfce4 xfce4-goodies

[root@archiso]# pacman -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings light-locker
[root@archiso]# systemctl enable lightdm.service
[root@archiso]# vi /etc/lightdm/lightdm-gtk-greeter.conf
[greeter]
theme-name = Adwaita
icon-theme-name = Adwaita
font-name = Cantarell 10
background = #376594
indicators = ~host;~spacer;~clock;~spacer;~session;~a11y;~power
clock-format = %A %d %B, %H:%M
hide-user-image = true
position = 25%,start 50%,center
user-background = false
[root@archiso]# pacman -S networkmanager network-manager-applet wpa_supplicant wpa_actiond dialog bluez dnsmasq modemmanager
[root@archiso]# systemctl enable NetworkManager.service

[root@archiso]# passwd
[root@archiso]# groupadd sudo
[root@archiso]# useradd -m -g users -G sudo,storage,wheel,power bandithijo
[root@archiso]# passwd bandithijo
[root@archiso]# nano /etc/sudoers
%sudo    ALL=(ALL) ALL
[root@archiso]# exit
root@archiso# umount -R /mnt
root@archiso# reboot

[bandithijo@BanditHijo-X61]$ sudo pacman -S neovim python2-neovim python-neovim xclip python-setuptools python-pip mpdecimal tk git gnome-keyring openssh openvpn x11-ssh-askpass easy-rsa asp rsync customizepkg cheese libreoffice-still gimp inkscape firefox chromium neomutt gvfs gparted gnome-disk-utility f2fs-tools exfat-utils ntfs-3g udftools gpart mtools gcolor2 gpick xf86-video-intel xf86-input-libinput vulkan-intel xarchiver arj cpio lha lrzip lz4 lzip lzop p7zip unarj unrar unzip zip ttf-liberation tlp acpi_call ethtool lsb-release smartmontools tp_smapi x86_energy_perf_policy bluez blueman dnsmasq net-tools pulseaudio-bluetooth pavucontrol telegram-desktop qt5-svg postgresql mariadb unixodbc freetds qt5ct lxsession samba gnome-calculator evince geany geany-plugin rxvt-unicode rxvt-unicode-terminfo urxvt-perls qemu glances atop iftop gtop cronie nodejs python-django python-virtualenv python2-virtualenv tcpdump aircrack-ng bind-tools encfs traceroute gnome-nettool nmon john wireshark-gtk wireshark-cli wireshark-common brasero cowpatty john putty fzf transmission-gtk lastpass-cli newsboat pamixer powertop gnome-logs gnome-power-manager gnome-system-log gnome-system-monitor gnome-usage baobab dconf-editor file-roller gucharmap gvfs-afc gvfs-mtp gvfs-smb simple-scan soundconverter geogebra dconf-editor uget lolcat tmux hexchat klavaro mysql-workbench mongodb modemmanager mupdf ranger pdfmod system-config-printer foomatic-db foomatic-db-nonfree-ppds foomatic-db-ppds gnome-color-manager gutenprint print-manager ipcalc opera opera-ffmpeg-codec bleachbit hardinfo hwinfo lshw qt5-styleplugins breeze breeze-gtk breeze-icons breeze-kde4 arandr htop strace thinkfinger eastytag audacious mpc mpd ncmpcpp feh w3m xautolock i3-gaps i3blocks i3lock i3status ttf-freefont urxvt-perls perl-gd perl-goo-canvas irssi bdf-unifont figlet perl-anyevent-i3 perl-async-interrupt perl-ev perl-guard perl-net-ssleay xorg-fonts-misc elinks ffmpegthumbnailer odt2txt highlight exfat-utils xdotool trash-cli gpicview code xdotool trash-cli ntp nmap mtpfs


[bandithijo@BanditHijo-X61]$ sudo ln -s /usr/bin/nvim /usr/bin/vim

[bandithijo@BanditHijo-X61]$ sudo vim /etc/pacman.conf
[multilib]
Include = /etc/pacman.d/mirrorlist
[bandithijo@BanditHijo-X61]$ sudo pacman -Syu

[bandithijo@BanditHijo-X61]$ git clone https://aur.archlinux.org/yay.git
[bandithijo@BanditHijo-X61]$ cd yay
[bandithijo@BanditHijo-X61]$ makepkg -si

[bandithijo@BanditHijo-X61]$ pikaur -S mugshot google-chrome ncpamixer aurvote aic94xx-firmware wd719x-firmware gotop-bin jekyll downgrade vokoscreen ffmulticonverter spotify shutter perl-goo-canvas goovancas1 light-locker-settings lightdm-flexiserver lightdm-slick-greeter uget-integration toilet key-mon kbbi-qt mongodb-compass emma masterpdfeditor powerstat-git flameshot vis ttf-unifont j4-dmenu-desktop figlet-fonts toilet-fonts termdown python-pyfiglet rts5227-dkms scrcpy

## Home Encryption

