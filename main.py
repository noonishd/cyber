

import os
import subprocess
os.system('sudo apt install pip -y')
os.system('pip install pytz')
import pytz
from datetime import datetime

def run(cmd):
    output_lines = []
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

    for line in process.stdout:
        stripped = line.strip()
        output_lines.append(stripped)

    process.wait()

    return output_lines

def doubleprint(text):
    with open(r'master_log.txt', 'a') as file: 
                file.write(text)
    print(text, end="")


#-------------------Creating_log_if_doesn't_exist_alr-------------------------- (FIX THIS================================================================================)
if not(os.path.exists(run('pwd')[0] + '/master_log.txt')):
  with open(r'master_log.txt', 'w') as file: 
    file.write(f'\n\n\n\n\n\nLog created: {datetime.now(pytz.timezone("Canada/Pacific")).strftime("%I:%M:%S:%p")}')

os.system('sudo chmod 755 Mal_pack_find.py')
os.system('sudo chmod 755 List_users.py')
import List_users
import Mal_pack_find #mal is running before list issue here