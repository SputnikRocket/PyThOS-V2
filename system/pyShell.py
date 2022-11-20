#PyThOS shell and related stuff

from colorama import init, Fore, Back, Style, deinit
from subprocess import call
from time import sleep
import core

init()

#Shell style definition
def shellStyle(SHELL):
    if SHELL == "bash":
        return (Fore.RED + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "PyThOS:/# " + Fore.RESET)

    elif SHELL == "zsh":
        return (Fore.WHITE + "PyThOS# " + Fore.RESET)

    elif SHELL == "sh":
        return (Fore.WHITE + "# " + Fore.RESET)

    elif SHELL == "csh":
        return (Fore.WHITE + "# " + Fore.RESET)
    
    elif SHELL == "fish":
        return (Fore.RED + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "PyThOS" + Fore.RED + "/" + Fore.White + " # " + Fore.RESET)

    elif SHELL not in ["bash","zsh","sh","csh","fish"]:
        return (Fore.RED + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "PyThOS:/# " + Fore.RESET)            

#The shell and PyThOS program launcher commands
def shellCmd(command):
    if command == "exit":
        core.exitConfirm()

    elif command == "clear":
        core.cls()

    elif command == "counter":
        core.counter()

    elif command not in ["exit","clear","counter"]:
        core.cnf(command)
