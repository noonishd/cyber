
from main import run, doubleprint
import time

def main1():
  doubleprint(f'\n\n\nUsers:\n\n\n')

#-----------------------------Checking_Users--------------------------------------- w

  valid_shells = run('cat /etc/shells')[1:]

  users = run('cat /etc/passwd')

  doubleprint(f"Valid Shells in /etc/shells:\n{valid_shells}\n\n\n\n")
  current_user = run('whoami')[0]

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
      if user[0] == current_user:
        doubleprint('                          ↑  YOU!!!!!\n\n')
        continue




      admin_check = ('adm' in run(f'groups {user[0]}')[0].split())
      if admin_check:
        if 'n' == input(f'"{user[0]}" IS an admin. Should they be an admin? (y/n): ').lower(): #-----------first check
          if 'y' == input(f'Demote "{user[0]}"? (y/n): ').lower(): #------------Are you sure?
            run(f'sudo deluser {user[0]} adm')
            doubleprint(f'            {user[0]} DEMOTED from admin\n') #--------------done
      else:
        if 'y' == input(f'"{user[0]}" ISNT an admin. Should they be an admin? (y/n): ').lower(): #-----------first check
          if 'y' == input(f'Promote "{user[0]}"? (y/n): ').lower(): #------------Are you sure?
            run(f'sudo adduser {user[0]} adm')
            doubleprint(f'            {user[0]} PROMOTED to admin\n') #--------------done




      print(f'Should "{user[0]}" be deleted????? (y/n): ', end='')
      if 'y' == input().lower():
        print(f'ARE YOU ABSOLUTELY SURE YOU WANT TO DELETE {user[0]}????? (y/n): ', end='')
        time.sleep(4)
        if 'y' == input().lower():
          run(f'sudo deluser {user[0]} --force') #-----------------------------------------------CAUTIONNNN IT WILL DELETE EVEN ROOT
          doubleprint(f'        {user[0]} deleted\n')
    else:
      doubleprint(f"'{user[0]}' not in a login shell\n", sendtext=False)



  input('Press anything to continue...')

#--------------------Checking_Important_Groups---------------
  doubleprint(f"\n\nGroups:\n\n\n")

  groups = run('cat /etc/group')

  important_groups = ['samba', 'root', 'adm', 'sudo', 'crontab']
  for group in groups:
    #print(group) 
    group_name = group.split(':')[0]
    #print(group_name)
    tab = ''
    if group_name in important_groups:
      tab = '                      '
    users_in_group = (group.split(':')[3:])
    for user in users_in_group:
      doubleprint(f"{tab}{group_name}: {user}\n")

if __name__ == '__main__':
  main1()
  input('Press enter to continue...   ')
