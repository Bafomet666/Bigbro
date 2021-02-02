# Big Bro 5.0
## Это OSINT инструмент, для поиска людей, перешедших по ссылке, радиус разброса местоположения 1-10 метров, зависит от расположения человека.

 Обновил 18 декабря, 2020г
 
![alt tag](https://github.com/Bafomet666/screen/blob/main/6.5.png)​

Сделано для https://t.me/hacknocrime

# Установка

## Kali Linux * Parrot OS

git clone https://github.com/Bafomet666/Bigbro

  Далее вам нужно распоковать нужную версию.

  cd /Bigbro-main

  sudo python3 bigbro.py -t manual -k start.kml
  
  ngrok запусти еще в соседнем окне

## Termux.

git clone https://github.com/Bafomet666/Bigbro

  Далее вам нужно распоковать нужную версию.

  cd /Bigbro-main

  chmod 777 termux_install.sh

 ./install.sh

python3 bigbro.py -t manual -k start.kml

Специально для termux, если вы не можете установить ngrok нормально, вот вам быстрая установка без заморочек. https://github.com/Bafomet666/Fast-ngrok

# Зависимости

![alt tag](https://camo.githubusercontent.com/d4d0378438eebbdfdf98948d518a47cb34bd241b3c836aaae47255a64f2c3bbe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e372532422d627269676874677265656e)

![alt tag](https://camo.githubusercontent.com/26043b6db7e2aee509448570c835702e9cd39397b53b18ac86b2b11090d08c26/68747470733a2f2f63646e2e737667706f726e2e636f6d2f6c6f676f732f707974686f6e2e737667)

Скачайте и установите ngrok https://ngrok.com/download

  Далее запустите ngrok в сторонем окне командой sudo ./ngrok http 8080

Удачного деанона друзья...
