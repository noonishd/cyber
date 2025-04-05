

import os
import subprocess
try:
    import pytz
except ModuleNotFoundError:
    os.system('sudo apt install pip -y')
    os.system('pip install pytz')
from datetime import datetime


def run(cmd):
    output_lines = []
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

    for line in process.stdout:
        stripped = line.strip()
        output_lines.append(stripped)

    process.wait()

    return output_lines

def doubleprint(text, sendfile=True, sendtext=True):
    if sendfile:
        with open(r'master_log.txt', 'a') as file: 
            file.write(text)
    if sendtext:
        print(text, end="")


#-------------------Creating_log_if_doesn't_exist_alr-------------------------- (FIX THIS===============================================================================) w
if not(os.path.exists(run('pwd')[0] + '/master_log.txt')):
    with open(r'master_log.txt', 'w') as file: 
        file.write(f'\n\n\n\n\n\nLog created: {datetime.now(pytz.timezone("Canada/Pacific")).strftime("%I:%M:%S:%p")}')

if __name__ == '__main__':
    os.system('sudo chmod 755 main.py')
    

    os.system('sudo chmod 755 user_audit.py')
    from user_audit import main1 as user_audit

    os.system('sudo chmod 755 mal_pack_find.py')
    from mal_pack_find import main2 as mal_pack_find
    
    os.system('sudo chmod 755 login_defs_config.py')
    from login_defs_config import main3 as login_defs_config

    os.system('sudo chmod 755 pams.py')
    from pams import main4 as pams


    user_audit()
    input('Press enter to continue...   ')
    mal_pack_find()
    input('Press enter to continue...   ')
    login_defs_config()
    input('Press enter to continue...   ')
    pams()
    input('Press enter to continue...   ')