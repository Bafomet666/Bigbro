from utils import COLORS

import random
import os

# -*- coding: utf-8 -*-
# dev by bafomet

BANNER1 = fr"""
 {COLORS.GNSL}Тайна это безопасность, а безопасность это победа {COLORS.FIOL}
   _______   __                  _______                            
  |       \ |  \                |       \ 
  | $$$$$$$\ \$$  ______        | $$$$$$$\  ______    ______ 
  | $$__/ $$|  \ /      \       | $$__/ $$ /      \  /      \ 
  | $$    $$| $$|  $$$$$$\      | $$    $$|  $$$$$$\|  $$$$$$\
  | $$$$$$$\| $$| $$  | $$      | $$$$$$$\| $$   \$$| $$  | $$
  | $$__/ $$| $$| $$__| $$      | $$__/ $$| $$      | $$__/ $$
  | $$    $$| $$ \$$    $$      | $$    $$| $$       \$$    $$
   \$$$$$$$  \$$ _\$$$$$$$       \$$$$$$$  \$$        \$$$$$$
                |  \__| $$ 
                 \$$    $$
                   \$$$$$$ """


def show_banner(*, clear=False):
    if clear:
        os.system("clear")
    banner = random.SystemRandom().choice([BANNER1])
    print(banner)


if __name__ == "__main__":
    show_banner()
