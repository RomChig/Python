import sys
from termcolor import colored
import socket
print('~' * 50, '\n')
green_color = colored('[+] ', 'green')
red_color = colored('[!] ', 'red')
yellow_color = colored('[!] ', 'yellow')
host = input(green_color + 'Host --> ')
print('\n')
#Нечетные до 50
for i in range(10,80,3):
    try:
        scan = socket.socket()
        scan.settimeout(0.5)
        scan.connect((host, i))
    except socket.error:
        print(red_color + 'Port -- ', i, ' -- [CLOSED]')
    else:
        print(yellow_color + 'Port -- ', i, ' -- [OPEN]')
