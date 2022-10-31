#Core and main command functions
#Whatever you put here must be hooked into pyShell.shellCmd

import boot
import pyHelp
import pyShell
import pyFlask
from colorama import init, Fore, Back, Style, deinit
from subprocess import call
from time import sleep

def exitConfirm():

    ex = input("Really exit PyThOS? ")
    ex = ex.lower()

    if ex == "y":
        print("Goodbye!")
        exit()

    elif ex == "yes":
        print("Goodbye!")
        exit()
        
    else:
        print()

def cls():
    call("clear")

def counter():

    c =  0

    while True:
        print(c)
        c = c + 1
    
