# -*- coding:utf-8 -*-
import os
import sys
#
# etre administrateur
if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

header = """
  ------------------
< \033[1;36mPaquet à Installer!!\033[1;36m >
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

os.system('apt-get install python-pip')
os.system('apt-get install python3.5')
os.system('easy_install pip')
import pip
os.system('pip install email')
os.system('pip install smtplib')
os.system('pip install zipfile')
os.system('pip install glob')
os.system('pip install shutil')
install = os.system("apt-get update && apt-get install -y build-essential git")
pip.main(["install", "email", "zipfile", "glob", "shutil"])