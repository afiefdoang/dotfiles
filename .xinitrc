#!/usr/bin/env bash

#[[ -f ~/.Xresources ]] && xrdb -merge "${HOME}/.Xresources"

# initialize X resource database (if file ~/.Xresources is present on the system)
#xrdb -load ~/.Xresources

# Start GNOME Keyring
#eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh)
#export SSH_AUTH_SOCK

# Launch i3 window manager
#eval $(dbus-launch --sh-syntax)
#export XDG_CURRENT_DESKTOP=GNOME
#exec i3
#exec dbus-launch gnome-session

## Executed by startx (run your window manager from here)
xrdb -load ~/.Xresources

if [ -d /etc/X11/xinit/xinitrc.d  ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f"  ] && . "$f"
  done
  unset f
fi

# exec startfluxbox
# exec enlightenment_start
# exec awesome
exec i3
# exec dwm
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
