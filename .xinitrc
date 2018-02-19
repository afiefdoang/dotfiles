#!/usr/bin/env bash

[[ -f ~/.Xresources ]] && xrdb -merge "${HOME}/.Xresources"

# initialize X resource database (if file ~/.Xresources is present on the system)
xrdb -load ~/.Xresources

# Start GNOME Keyring
dbus-update-activation-environment --systemd DISPLAY
eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

# Launch i3 window manager
eval $(dbus-launch --sh-syntax)
export XDG_CURRENT_DESKTOP=GNOME
exec i3
exec dbus-launch gnome-session

