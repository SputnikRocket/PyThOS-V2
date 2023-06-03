#PyThOS init script

from sys import argv
from colorama import init, Style, Fore, Back, deinit
import boot
import core
import pyFlask
import pyHelp
import pyShell
from os import system
import os.path
from time import sleep

<<<<<<< HEAD
=======
"""This checks if rc file exists, 
if not creates with default values"""
>>>>>>> 52b8509 (fixed rc, implemented shell theme in rc, more commenting)
rcExists = os.path.exists("py.rc")
if rcExists == False:
    rc = open("py.rc", "w")
    rc.writelines("""splash=True
dmesg=True
bash
""")
    rc.close()

<<<<<<< HEAD
=======
#Read rc file and set PyThOS config
>>>>>>> 52b8509 (fixed rc, implemented shell theme in rc, more commenting)
rc = open("py.rc", "r")
rcConf = rc.readlines()
bootEnable = rcConf[0]
dmesgEnable = rcConf[1]
shellPreset = rcConf[2]
rc.close()

#Manual shell style parameter
shell = ""
init()

if len(argv) == 1:
    shell = ""

elif len(argv) == 2:
    shell = argv[1]


#Boot initialization
if  bootEnable == "splash=True":
    core.cls()
    boot.bootInit()
    sleep(2)
    core.cls()
if bootEnable == "splash=False":
    core.cls()

#Start messages
if dmesgEnable == "dmesg=True":
    print(Fore.WHITE + "[" + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]" + " Boot splash completed")

    if shell == "":
<<<<<<< HEAD
        print(Fore.WHITE + "[" + Fore.YELLOW + "WARNING" + Fore.WHITE + "]" + " \"SHELL\" not set, defaulting to" + shellPreset + Fore.RESET)

=======
        print(Fore.WHITE + "[" + Fore.YELLOW + "WARNING" + Fore.WHITE + "]" + " \"SHELL\" not set, defaulting to " + shellPreset + Fore.RESET)
elif dmesgEnable == "dmesg=False":
    core.cls()
>>>>>>> 52b8509 (fixed rc, implemented shell theme in rc, more commenting)


#Shell startup
while True:
    try:
        command = input(pyShell.shellStyle(shell))
        pyShell.shellCmd(command)

    except KeyboardInterrupt:

        try:
            pyShell.shellCmd("exit")

        except KeyboardInterrupt:
            print("Goodbye!")
            exit()
            
