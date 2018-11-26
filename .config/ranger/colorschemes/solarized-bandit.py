# Joseph Tannhuber <sepp.tannhuber@yahoo.de>, 2013
# Solarized like colorscheme, similar to solarized-dircolors
# from https://github.com/seebi/dircolors-solarized.
# This is a modification of Roman Zimbelmann's default colorscheme.
# This software is distributed under the terms of the GNU GPL version 3.

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Solarized(ColorScheme):
    progress_bar_color = yellow

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            fg = 244
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                fg = 235
                bg = red
            if context.border:
                fg = 0
            if context.media:
                if context.image:
                    # fg = 136
                    fg = 33
                else:
                    fg = 166
            if context.container:
                fg = 61
            if context.directory:
                # fg = 33
                fg = yellow
            elif context.executable and not \
                    any((context.media, context.container,
                        context.fifo, context.socket)):
                fg = 64
                attr |= bold
            if context.socket:
                fg = 136
                bg = 230
                attr |= bold
            if context.fifo:
                fg = 136
                bg = 230
                attr |= bold
            if context.device:
                fg = 244
                bg = 230
                attr |= bold
            if context.link:
                fg = context.good and 37 or 160
                bg = context.bad and 235
                attr |= bold
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (red, magenta):
                    fg = white
                else:
                    fg = red
            if not context.selected and (context.cut or context.copied):
                fg = 234
                attr |= bold
            if context.main_column:
                if context.selected:
                    fg = red
                    bg = 0
                    attr |= bold
                if context.marked:
                    attr |= bold
                    # bg = 237
                    bg = yellow
                    fg = 0
            if context.badinfo:
                if attr & reverse:
                    bg = yellow
                else:
                    fg = yellow

        elif context.in_titlebar:
            # attr |= bold
            if context.hostname:
                # fg = context.bad and 160 or 93
                fg = yellow
                # bg = context.bad and 235
                bg = 0
            elif context.directory:
                # fg = 33
                fg = red
            elif context.tab:
                # fg = 33 if context.good else default
                fg = yellow if context.good else default
                bg = default
            elif context.link:
                fg = 33

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = yellow
                elif context.bad:
                    fg = red
            if context.marked:
                attr |= bold | reverse
                fg = 237
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = 160
                    bg = 235
            if context.loaded:
                fg = 0
                bg = self.progress_bar_color

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 93

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    fg = 0
                    bg = self.progress_bar_color

        return fg, bg, attr
