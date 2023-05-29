#Boot animation module for PyThOS

from colorama import init, Fore, Back, Style, deinit
from os import system
from time import sleep
import core

#Stuff to call before doing anything else


#Main boot Icon/Frame
def primaryFrame():

    """The massive amount of empty space in here
    has no functional purpose whatsoever, it just
    makes it much easier to read & modify."""

    init()
    print(Fore.MAGENTA + "     ##############################################"                                                                             )
    print(Fore.MAGENTA + "    #                                              #"                                                                            )
    print(Fore.MAGENTA + "   #  " + Fore.RED + " PPPP       " + Fore.GREEN + " TTTTTTTTT h    " + Fore.BLUE + "   OOO    SSSSS " + Fore.MAGENTA + "  #    ")
    print(Fore.MAGENTA + "  #   " + Fore.RED + " P   P      " + Fore.GREEN + "     T     h    " + Fore.BLUE + "  O   O  S      " + Fore.MAGENTA + "   #   ")
    print(Fore.MAGENTA + " #    " + Fore.RED + " P   P      " + Fore.GREEN + "     T     h    " + Fore.BLUE + " O     O S      " + Fore.MAGENTA + "    #  ")
    print(Fore.MAGENTA + "#     " + Fore.RED + " PPPP  y   y" + Fore.GREEN + "     T     hhhh " + Fore.BLUE + " O     O  SSSS  " + Fore.MAGENTA + "     # ")
    print(Fore.MAGENTA + " #    " + Fore.RED + " P      y y " + Fore.GREEN + "     T     h   h" + Fore.BLUE + " O     O      S " + Fore.MAGENTA + "    #  ")
    print(Fore.MAGENTA + "  #   " + Fore.RED + " P       y  " + Fore.GREEN + "     T     h   h" + Fore.BLUE + "  O   O       S " + Fore.MAGENTA + "   #   ")
    print(Fore.MAGENTA + "   #  " + Fore.RED + " P      y   " + Fore.GREEN + "     T     h   h" + Fore.BLUE + "   OOO   SSSSS  " + Fore.MAGENTA + "  #    ")
    print(Fore.MAGENTA + "    # " + Fore.RED + "       y    "                                   + Fore.MAGENTA +  "                                 #     ")
    print(Fore.MAGENTA + "     ##############################################"                                                                             )
    deinit()

#Border line for booting screen
def borderLine():
    init()
    print(Back.GREEN + Fore.RED + "<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    deinit()
    
bootProgress = ["*", "* *", "* * *", "* * * *", "* * * * *", "* * * * * *", "* * * * * * *", "* * * * * * * *"]

#Entire boot screen run
def bootInit():
    init()
    for i in range(8):
        core.cls()
        primaryFrame()
        print()
        borderLine()
        print()
        print(Fore.YELLOW + Back.RESET + bootProgress[i])
        sleep(1)
    deinit()


    
primaryFrame()
