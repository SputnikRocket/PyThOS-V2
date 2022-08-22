#PyThOS init script

from sys import argv
from colorama import init, Style, Fore, Back, deinit
import boot
import core
import pyFlask
import pyHelp
import pyShell
from subprocess import call
from time import sleep

shell = ""
distro = ""
init()

if len(argv) == 1:
    shell = ""
    distro = ""

elif len(argv) == 2:
    distro = argv[1]

elif len(argv) == 3:
    distro = argv[1]
    shell = argv[2]



#Boot initialization
call("clear")
boot.bootInit()
sleep(2)
call("clear")

#Start messages
print(Fore.WHITE + "[" + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]" + " Boot splash completed")
if distro == "":
    print(Fore.WHITE + "[" + Fore.YELLOW + "WARNING" + Fore.WHITE + "]" + " \"DISTRO\" not set, some features disabled")

if shell == "":
    print(Fore.WHITE + "[" + Fore.YELLOW + "WARNING" + Fore.WHITE + "]" + " \"SHELL\" not set, defaulting to bash" + Fore.RESET)



while True:
    promt = input(pyShell.shellStyle(shell))
    
