# Big Bro 5.0 and 6.5 
# Это OSINT инструмент, для поиска людей перешедших по ссылке, радиус разброса местоположения 1-10 метров, зависит от расположение человека.

 Обновил 18 декабря, 2020г
 
![alt tag](https://github.com/Bafomet666/screen/blob/main/6.5.png)​

Сделано для https://t.me/hacknocrime

Общее число сайтов 20. В премиум версии 40, за подробной информацией писать Telegram https://t.me/satana666mx.

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

Скачайте и установите ngrok [ https://ngrok.com/download ]

  Далее запустите ngrok в сторонем окне командой sudo ngrok http 8080


# Запуск

  Kali linux / Parrot os:   sudo python3 bigbro.py -t manual -k start.kml

  Termux:                   python3 bigbro.py -t manual -k start.kml

Удачного деанона друзья...
