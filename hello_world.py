import random
import time
import colorama
from colorama import Fore
dead_inside = True
while dead_inside == True:
    print(Fore.YELLOW + "Hello World ")
    time.sleep(1)
    if (random.randint(0,10)==0):
        print(Fore.RED + "Doesnt say hello")
        print(Fore.BLACK)
        break
