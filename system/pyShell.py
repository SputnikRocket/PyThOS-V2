#PyThOS shell and related stuff

from colorama import init, Fore, Back, Style, deinit
from subprocess import call
from time import sleep
import core

init()

bashstyle = (Fore.RED + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "PyThOS:/# " + Fore.RESET)

zshstyle = (Fore.WHITE + "PyThOS# " + Fore.RESET)

shstyle = (Fore.WHITE + "# " + Fore.RESET)

cshstyle = (Fore.WHITE + "# " + Fore.RESET)

fishstyle = (Fore.RED + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "PyThOS" + Fore.RED + "/" + Fore.WHITE + " # " + Fore.RESET)

#Shell style init
def shellStyle(SHELL):
    if SHELL == "bash":
        return bashstyle

    elif SHELL == "zsh":
        return zshstyle

    elif SHELL == "sh":
        return shstyle

    elif SHELL == "csh":
        return cshstyle
    
    elif SHELL == "fish":
        return fishstyle

    elif SHELL not in ["bash","zsh","sh","csh","fish"]:
        return bashstyle            

#The shell and PyThOS program launcher commands
def shellCmd(command):
    if command == "exit":
        core.exitConfirm()

    elif command == "clear":
        core.cls()

    elif command == "counter":
        core.counter()

    elif command == "yuptime":
        core.yuptime()

    elif command not in ["exit","clear","counter","yuptime"]:
        core.cnf(command)
