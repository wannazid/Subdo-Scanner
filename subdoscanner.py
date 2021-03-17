#subdo scanner by wan5550
import requests
import json
from colorama import Fore, Back, Style
import time
import os

hijau = Fore.GREEN
merah = Fore.RED
biru = Fore.BLUE
tai = Fore.YELLOW
cyan = Fore.CYAN
time.sleep(2)

def bersih_bersih():
	   linuxwan = "clear"
	   windowswan = "cls"
	   os.system([linuxwan,windowswan][os.name == "nt"])
bersih_bersih()

def author_dong():
       print(hijau+'[+] Subdomain Scanner Tools')
       print(Style.RESET_ALL)
       print(merah+'[+] Author : Wan5550')
       print(Style.RESET_ALL)
       print(biru+'[+] How To Use : url.com')
       print(Style.RESET_ALL)
       print(tai+'[+] Github : github.com/wannazid')
       print(Style.RESET_ALL)
       print(cyan+'========================================')
       print(Style.RESET_ALL)
author_dong()

url_target = input(str("[~] Masukan URl Target : "))
api = requests.get("http://jamet1337.ml/api/subdo.php?url="+url_target)
print(hijau+'Loading Scan Subdo'+':',url_target)
print(Style.RESET_ALL)
time.sleep(2.50)
uwu = (json.loads(api.content)['hasil'])
print(uwu)
print(Style.RESET_ALL)
print(cyan+'~#: Hasil Telah Disimpan Subdomain Scanner.txt')
print(Style.RESET_ALL)
savefile = open('Hasil Subdomain Scanner.txt', 'a').write('http://'+uwu+'\n')
