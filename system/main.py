#PyThOS init script

from sys import argv
from colorama import init, Style, Fore, Back, deinit
import boot
import core
import pyFlask
import pyHelp
import pyShell
from os import system
from time import sleep

shell = ""
init()

if len(argv) == 1:
    shell = ""

elif len(argv) == 2:
    shell = argv[1]


#Boot initialization
system("@cls||clear")
boot.bootInit()
sleep(2)
system("@cls||clear")

#Start messages
print(Fore.WHITE + "[" + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]" + " Boot splash completed")

if shell == "":
    print(Fore.WHITE + "[" + Fore.YELLOW + "WARNING" + Fore.WHITE + "]" + " \"SHELL\" not set, defaulting to bash" + Fore.RESET)



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
            
