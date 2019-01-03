#!/usr/bin/env bash


# Start GNOME Keyring
dbus-update-activation-environment --systemd DISPLAY
eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

# Launch i3 window manager
#eval $(dbus-launch --sh-syntax)
#export XDG_CURRENT_DESKTOP=GNOME
#exec i3
#exec dbus-launch gnome-session

## Executed by startx (run your window manager from here)
xrdb -load ~/.Xresources
xset +fp /usr/share/fonts/local
xset fp rehash

if [ -d /etc/X11/xinit/xinitrc.d  ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f"  ] && . "$f"
  done
  unset f
fi

# Clipmenu change from dmenu to rofi
# (sudah dihandle oleh .profile karena saya menggunakan lightdm)
#export CM_LAUNCHER=rofi
#export CM_DIR=/tmp/clipmenu


# Ranger
# (sudah dihandle oleh .profile karena saya menggunakan lightdm)
#ranger() {
#    if [ -z "$RANGER_LEVEL" ]; then
#        /usr/bin/ranger "$@"
#    else
#        exit
#    fi
#}

# exec startfluxbox
# exec enlightenment_start
# exec awesome
# exec i3
# exec sway
exec /usr/local/bin/dwm
# exec mate-session
# exec xmonad
# exec startlxqt
# exec startlxde
# exec bspwm
# exec gnome-session
# exec gnome-session --session=gnome-classic
# exec startkde
# exec startxfce4
# exec openbox-session
# exec cinnamon-session
# exec pekwm
# exec catwm
# exec startede
# exec icewm-session
# exec jwm
# exec monsterwm
# exec notion
