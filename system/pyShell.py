#PyThOS shell and related stuff

from colorama import init, Fore, Back, Style, deinit
from subprocess import call
from time import sleep

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
            