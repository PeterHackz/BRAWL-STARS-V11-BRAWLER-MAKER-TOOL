import platform
import os
def clear():
    system = platform.system()
    if system == 'Windows': 
        os.system('cls') 
    else:
    	os.system('clear')
