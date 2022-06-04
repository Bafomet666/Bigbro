
from utils import COLORS
from pyngrok import ngrok
import subprocess
import os
import time


def kill():
    ngrok.kill()
    os.system('rm -rf __pycache__')
    os.system('rm -rf module/__pycache__')
    os.system('rm -rf utils/__pycache__')
    print(f' {COLORS.FIOL}Благодарим вас за использование !!!{COLORS.WHSL} Вы прекрасны.\n')
    time.sleep(0.5)
    subprocess.call('pkill -9 php', shell=True)
    subprocess.call('pkill -9 -f start.py', shell=True)
