[ "$XDG_CURRENT_DESKTOP" = "KDE" ] || [ "$XDG_CURRENT_DESKTOP" = "GNOME" ] || export QT_QPA_PLATFORMTHEME="qt5ct"

export ANDROID_EMULATOR_USE_SYSTEM_LIBS=1
export FONTCONFIG_PATH=/etc/fonts
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_SCREEN_SCALE_FACTORS=1
export QT_SCALE_FACTOR=1

# URXVT Environment
export TERM=rxvt-unicode
alias xterm="urxvt"

# TimeZone
#TZ='Asia/Jakarta'; export TZ
TZ='Asia/Makassar'; export TZ
