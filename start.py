import os
from utils import COLORS
from utils.ban import page_20

def clear_screen():
    os.system("clear")

def osintsan():
    clear_screen()
    os.system("printf '\033]2;Меню 🧙🏻‍♂️ \a'")
    print(page_20)
    while True:
        choice = None
        while True:
            try:
                user_input = input(
                    f"{COLORS.REDL}  └──> {COLORS.FIOL}Bafomёd production ──>{COLORS.GNSL} Введите номер опции: {COLORS.WHSL}")
                print(f'\n')
            except KeyboardInterrupt:
                return

            if len(user_input) == 0:
                break

            try:
                choice = int(user_input)
            except ValueError:
                print(f"{COLORS.REDL}Неверный ввод!{COLORS.ENDL}")
            else:
                break

        if choice is None:
            continue

        if choice == 1:
            from menu1 import loc
            loc()

        elif choice == 2:
            from menu2 import location
            location()

        elif choice == 3:
            from utils.killing import kill
            kill()
            
        elif choice == 4:
            print('  Полная версия в клиенте OSINT-SAN PRO, https://t.me/osint_san_framework \n')
            
osintsan()
