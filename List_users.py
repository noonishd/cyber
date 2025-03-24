
from datetime import datetime
from main import run, doubleprint
import pytz

doubleprint(f'\n\n\n\n\n\nLog created: {datetime.now(pytz.timezone("Canada/Pacific")).strftime("%I:%M:%S:%p")}\n\n\nUsers:\n\n\n')

#-----------------------------Checking_Users---------------------------------------

valid_shells = run('cat /etc/shells')[1:]

users = run('cat /etc/passwd')

doubleprint(f"Valid Shells in /etc/shells:\n{valid_shells}\n\n\n\n")

for user in users:
  user = user.split(':')
  if user[len(user)-1] in valid_shells:
    doubleprint(f"                      '{user[0]}' in valid shell")
    if int(user[2]) == 0 and int(user[3]) == 0:
      doubleprint('                      Root User!\n')
    elif int(user[2]) < 1000:
      doubleprint('                      Hidden User!\n')
    elif int(user[2]) >= 1000:
      doubleprint('                      Valid User\n')

  else:
    doubleprint(f"'{user[0]}' not in a login shell\n")


#--------------------Checking_Important_Groups---------------
doubleprint(f"\n\nGroups:\n\n\n")

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
    doubleprint(f"{tab}{group_name}: {user}\n")
    
