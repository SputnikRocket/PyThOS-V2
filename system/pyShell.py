#PyThOS shell and related stuff

from colorama import init, Fore, Back, Style, deinit
from os import system
import core

init()

#Shell themes
bashstyle = (Fore.RED + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "PyThOS:/# " + Fore.RESET)

zshstyle = (Fore.WHITE + "PyThOS# " + Fore.RESET)

shstyle = (Fore.WHITE + "# " + Fore.RESET)

cshstyle = (Fore.WHITE + "# " + Fore.RESET)

fishstyle = (Fore.RED + "root" + Fore.MAGENTA + "@" + Fore.WHITE + "PyThOS" + Fore.RED + "/" + Fore.WHITE + " # " + Fore.RESET)

altzshstyle = (Fore.BLUE + "┌─[" + Fore.GREEN + "root" + Fore.BLUE + "@" + Fore.CYAN + "PyThOS" + Fore.BLUE + ''']
└─[''' + Fore.MAGENTA + "$" + Fore.BLUE + "] " + Fore.RESET)

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

    elif SHELL == "altzsh":
        return altzshstyle

    elif SHELL not in ["bash","zsh","sh","csh","fish","altzsh"]:
        if RCSHELL == "bash":
            return bashstyle

        elif RCSHELL == "zsh":
            return zshstyle

        elif RCSHELL == "sh":
            return shstyle

        elif RCSHELL == "csh":
            return cshstyle
    
        elif RCSHELL == "fish":
            return fishstyle 

        elif RCSHELL == "altzsh":
            return altzshstyle

        elif RCSHELL not in ["bash","zsh","sh","csh","fish","altzsh"]:
            return bashstyle           

#The shell and PyThOS program launcher commands
availCmds = ["exit","clear","counter","yuptime","cmds"]
def shellCmd(command):
    if command == "exit":
        core.exitConfirm()

    elif command == "clear":
        core.cls()

    elif command == "counter":
        core.counter()

    elif command == "yuptime":
        core.yuptime()

    elif command == "cmds":
        for availCmd in availCmds:
            print(availCmd)

    elif command not in availCmds:
        core.cnf(command)

