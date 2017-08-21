# -*- coding:utf-8 -*-
import os, sys
#
# etre administrateur
if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

header = """
  ------------------
< \033[1;36mTrity Installer!!\033[1;36m >
  ------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\

                 ||-----||
                 ||     ||
"""

print(header)
print("\033[1;36mOperating Systems Available:\033[1;36m ")
print("\n--------------------------")
print("(1) Kali Linux / Ubuntu / Raspbian")
print("--------------------------\n")

option = input("\033[0m[>] Select Operating System: \033[0m")

if option == "1":
    print("\033[1;33m[*] Loading...\033[0m")
    os.system('apt-get install python3.5')
    os.system('easy_install pip3')
    import pip
    os.system('sudo apt-get install libjpeg-dev libfreetype6 zlib1g-dev')
    os.system('pip install email')
    os.system('pip install smtplib')
    os.system('pip install zipfile')
    os.system('pip install glob')
    os.system('pip install shutil')
    install = os.system("apt-get update && apt-get install -y build-essential git")
    os.system('apt-get install sendemail')
    print("\033[1;32m[!] Fin des Installations  [!]\033[0m")
    sys.exit()
else:
    print ("Oups! Quelque chose s'est mal passé!")