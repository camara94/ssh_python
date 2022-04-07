#! /usr/local/Python_envs/Python3/bin/python3
import paramiko
import time
from getpass import getpass
import re


host = "ip or hostname"
username = "your username"
password = "your password"

print(f"\n{'#' * 55}\nConnecting to the Device {host}\n{'#' * 55} ")
SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(host, port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)
DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'cd /var/www/monapi\n')
DEVICE_ACCESS.send(b'ls -la\n')
#DEVICE_ACCESS.send(b'term length 0\n')
#DEVICE_ACCESS.send(b'show run\n')
time.sleep(1)
output = (DEVICE_ACCESS.recv(65000).decode('ascii'))
print(output)

print(f"\n{'#' * 55}\nFinished Executing Script\n{'#' * 55} ")
SESSION.close()
