import os
import subprocess
import sys
import time
from datetime import datetime

os.system('sudo apt install pip -y')
os.system('pip install pytz')

import pytz

os.system('sudo chmod 755 List_users.py')
#os.system('sudo su')

def run(cmd):
    output_lines = []
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

    for line in process.stdout:
        stripped = line.strip()
        #print(line)
        output_lines.append(stripped)

    process.wait()

    return output_lines

#-------------------------------Init_Log-------------------------------------------
if not(os.path.exists(run('pwd')[0] + '/Users.txt')):
  with open(r'Users.txt', 'w') as file: 
    file.close()

with open(r'Users.txt', 'a') as file:
    file.write(f'\n\n\n\n\n\nLog created: {datetime.now(pytz.timezone("Canada/Pacific")).strftime("%I:%M:%S:%p")}\n\n\nUsers:\n\n\n')

#-----------------------------Checking_Users---------------------------------------

valid_shells = run('cat /etc/shells')[1:]

users = run('cat /etc/passwd')

print(f"Valid Shells in /etc/shells:\n{valid_shells}\n")
with open(r'Users.txt', 'a') as file:
    file.write(f"Valid Shells in /etc/shells:\n{valid_shells}\n\n\n\n")

for user in users:
  user = user.split(':')
  if user[len(user)-1] in valid_shells:
    print(f"                      '{user[0]}' in valid shell")
    with open(r'Users.txt', 'a') as file:
      file.write(f"                      '{user[0]}' in valid shell")
      if int(user[2]) == 0 and int(user[3]) == 0:
        file.write('                      Root User!\n')
        print('                      Root User!\n')
      elif int(user[2]) < 1000:
        file.write('                      Hidden User!\n')
        print('                      Hidden User!\n')
      elif int(user[2]) >= 1000:
        file.write('                      Valid User\n')
        print('                      Valid User\n')
  else:
    print(f"'{user[0]}' not in a login shell \n")
    with open(r'Users.txt', 'a') as file:
      file.write(f"'{user[0]}' not in a login shell\n")


#--------------------Checking_Important_Groups---------------
with open(r'Users.txt', 'a') as file:
      file.write(f"\n\nGroups:\n\n\n")

groups = run('cat /etc/group')

important_groups = ['samba', 'root', 'adm', 'sudo', 'crontab']
for group in groups:
  #print(group) 
  group_name = group.split(':')[0]
  #print(group_name)
  if group_name in important_groups:
    tab = '                      '
  else:
    tab = ''
  users_in_group = (group.split(':')[3:])
  for user in users_in_group:
    print(tab + group_name + ': ' + user)
    with open(r'Users.txt', 'a') as file:
      file.write(f"{tab}{group_name}: {user}\n")
    
