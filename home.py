import os,sys,time,re,requests,json
from requests import post
from time import sleep

def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def suc(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def suc1(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
os.system("clear")
intro("""
\033[1;31m██╗░░██╗░█████╗░███╗░░░███╗███████╗░░░░░░██╗██████╗░
\033[1;31m██║░░██║██╔══██╗████╗░████║██╔════╝░░░░░░██║██╔══██╗
\033[1;31m███████║██║░░██║██╔████╔██║█████╗░░█████╗██║██║░░██║
\033[1;37m██╔══██║██║░░██║██║╚██╔╝██║██╔══╝░░╚════╝██║██║░░██║
\033[1;37m██║░░██║╚█████╔╝██║░╚═╝░██║███████╗░░░░░░██║██████╔╝
\033[1;37m╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░░░░╚═╝╚═════╝░
\033[1;31m════════════════════════════════════════════════
\033[1;37m{\033[1;31m•\033[1;37m} \033[1;37mAuthor  :  \033[1;37mMr.C4N 404
\033[1;37m{\033[1;31m•\033[1;37m} \033[1;37mYoutube :  \033[1;37mCANDRA-NM
\033[1;37m{\033[1;31m•\033[1;37m} \033[1;37mGithub  :  \033[1;37mhttps://github.com/B4N9C4N
\033[1;31m════════════════════════════════════════════════""")

suc("\033[1;37m{\033[1;31m•\033[1;37m} \033[1;37mMohon tunggu...")
time.sleep(4)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
sleep(1)
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
os.system('termux-reload-settings')
no = input("\033[1;37m{\033[1;31m•\033[1;37m} \033[1;37mENTER UNTUK MELIHAT HASIL")
os.system('login')




