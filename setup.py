import subprocess
import os
import time
import sys
ex=('''\033[95m
          +-------------------------------------------------+
          |         Welcome To BD 71 HACKER ZONE            |
          | Subscribe Our YouTube Channel:@BD71HACKERZONEb  |
          | Watch Ours Tutorials For Learn Ethical Hacking  |
          +-------------------------------------------------+''')

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
l1=('''\033[1m\033[33m
                      ███╗░░░███╗░█████╗░██████╗░
                      ████╗░████║██╔══██╗██╔══██╗
                      ██╔████╔██║███████║██║░░██║
                      ██║╚██╔╝██║██╔══██║██║░░██║
                      ██║░╚═╝░██║██║░░██║██████╔╝
                      ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░
''')
l2=('''\033[1m\033[32m              ▂▃▄▅▆▇▓▒░ Coded By MAD HACKRECKRE ░▒▓▇▆▅▄▃▂
''')
l3=('''\033[1m\033[31m             ]───────────────────────────────────────────[ ''')
os.system("clear")
print(l1)
print(l2)
print(l3)
print(  )

# Get user input
user_input = input(" Ar you install Dis Tool [y/n] : ")

if user_input == "y":
    os.system("clear")
    print("W8 For install")
    os.system("pkg update")
    os.system("pkg upgrade")
    os.system("pkg install git -y")
    os.system("pkg install python3 -y")
    os.system("pkg install bash -y")
    os.system("chmod +x login.sh")
    os.system("bash login.sh")
elif user_input == "n":
    slowprint(ex)
    os.system("exit")
else:
    slowprint(ex)