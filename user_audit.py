#sudo adduser frank
#sudo adduser frank adm
#sudo usermod --shell /usr/sbin/nologin frank
#
#
#
from main import run, doubleprint
import time

def main():
  doubleprint(f'\n\n\nUsers:')
  doubleprint(f'\n\n\nIs not a catch-all: CHECK MANUALLY FOR FUNKY USERS ESPECIALLY ROOTS\n\n\n')

  

  auth_users = ['root']
  while True:
    ok_user = input('Please input a valid user [root is included by default] (type exit123 to finish): ')
    if ok_user == 'exit123':
      break
    elif ok_user:
      auth_users.append(ok_user)




  def delete_check():
    print(f'Should "{user[0]}" be deleted????? (y/n): ', end='')
    if 'y' == input().lower():
      print(f'ARE YOU ABSOLUTELY SURE YOU WANT TO DELETE {user[0]}????? (y/n): ', end='')
      time.sleep(4)
      if 'y' == input().lower():
        run(f'sudo deluser {user[0]} --force') #-----------------------------------------------CAUTIONNNN IT WILL DELETE EVEN ROOT
        doubleprint(f'                      {user[0]} deleted\n')

  def admin_check():
    admin_status = ('adm' in run(f'groups {user[0]}')[0].split()) and user[0] in auth_users
    if admin_status:
      if 'n' == input(f'"{user[0]}" IS an admin. Should they be an admin? (y/n): ').lower(): #-----------first check
        if 'y' == input(f'Demote "{user[0]}"? (y/n): ').lower(): #------------Are you sure?
          run(f'sudo deluser {user[0]} adm')
          doubleprint(f'                      {user[0]} DEMOTED from admin\n') #--------------done
    else:
      if 'y' == input(f'"{user[0]}" ISNT an admin. Should they be an admin? (y/n): ').lower(): #-----------first check
        if 'y' == input(f'Promote "{user[0]}"? (y/n): ').lower(): #------------Are you sure?
          run(f'sudo adduser {user[0]} adm')
          doubleprint(f'                      {user[0]} PROMOTED to admin\n') #--------------done


#-----------------------------Checking_Users--------------------------------------- w

  valid_shells = run('cat /etc/shells')[1:]

  users = run('cat /etc/passwd')

  doubleprint(f"Valid Shells in /etc/shells:\n{valid_shells}\n\n\n\n")
  current_user = run('whoami')[0]


  #-----------------------------Grabs every user and compares their uids--------------------
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



      #-----------------------------Runs an admin check and allows operator to set to admin or remove from accordingly--------------------
      admin_check()



      #-----------------------------Allows operator to delete users accordingly--------------------
      delete_check()


    elif not(user[len(user)-1] in valid_shells) and user[0] in auth_users:
      doubleprint(f"                      '{user[0]}' not in a login shell\n")


      #-----------------------------Allows operator to set authenticated users into a valid login shell accordingly--------------------
      if 'y' == input(f'{user[0]} is not currently in a valid login shell but is an authenticated user\nWould you like to set {user[0]} to a valid shell? ({valid_shells[0]}) (y/n): ').lower():
        run(f'sudo usermod --shell {valid_shells[0]} {user[0]}')
        doubleprint(f'                      {user[0]} added to valid shell ({valid_shells[0]})\n')
      admin_check()
      delete_check()

    else:
      doubleprint(f"'{user[0]}' not in a login shell nor is a known user (check if sus in post)\n")





'''
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
'''



if __name__ == '__main__':
  main()

