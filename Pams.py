#auth\trequired\t\t\tpam_permit.so\n w
#auth\trequisite\t\t\tpam_faillock.so\naudit deny=5 unlock_time=900 even_deny_root_account

from main import run, doubleprint
import os

os.system('sudo chmod +x Pams.py')

download_check = run('sudo apt install libpam-pwquality -y')

if 'E: Unable to locate package libpam-pwquality' in download_check:
    run('sudo apt update')
    doubleprint('pam install failed: updating sources')
    run('sudo apt install libpam-pwquality -y')
    doubleprint('libpam-pwquality installed')

with open(r'/etc/pam.d/common-auth', 'r') as file:
    edits = file.readlines()
    for i in range(len(edits)):
        if 'nullok' in edits[i]:
            edits[i] = edits[i].replace('nullok', '')

edits.append('auth\trequisite\t\t\tpam_faillock.so audit deny=5 unlock_time=900 even_deny_root_account\n')

with open(r'/etc/pam.d/common-auth', 'w') as file: #WRITES TO FILE
    file.writelines(edits)


#USES EDITS2 BE CAREFUKLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL

with open(r'/etc/pam.d/common-password', 'r') as file:
    edits2 = file.readlines()
    for i in range(len(edits2)):
        if 'password\trequisite\t\t\tpam_pwquality.so' in edits2[i]:
            edits2[i] = '#' +  edits2[i]

edits2.append('password\trequisite\t\t\tpam_pwquality.so retry=3 minlen=14 difok=3 dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minclass=3 maxrepeat=2 maxsequence=3 gecoscheck enforce_for_root\n')

with open(r'/etc/pam.d/common-password', 'w') as file: #WRITES TO FILE
    file.writelines(edits2)