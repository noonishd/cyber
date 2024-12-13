#Double check iodines, icecasts, and ettercap
#unable to find logkeys, nikito, tightvnc, pyrit, lcrack, fof, 
#Check Burp Suite on ur own bc i think its uninstall is through gui
#Check Armitage


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
        output_lines.append(stripped)

    process.wait()

    return output_lines


#-------------------Creating_log_if_doesn't_exist_alr-------------------------- (FIX THIS================================================================================)
if not(os.path.exists(run('pwd')[0] + '/Mal_pack_log.txt')):
  with open(r'Mal_pack_log.txt', 'w') as file: 
    file.close()

with open(r'Mal_pack_log.txt', 'w') as file:
    file.write(f'\n\n\n\n\n\nLog created: {datetime.now(pytz.timezone("Canada/Pacific")).strftime("%I:%M:%S:%p")}\n\n\n#Double check iodines, icecasts, and ettercap\n#unable to find logkeys, nikito, tightvnc, pyrit, lcrack, fof, \n#Check Burp Suite on ur own bc i think its uninstall is through gui\n#Check Armitage\n\n\n')


#-------------------initializing--------------------------------------------------------------------------------------------------------------------------------------

Package_list = ['apache2', 'deluge', 'tcpdump', 'iodine', 'iodine-client', 'manaplus', 'gameconqueror', 'wireshark', 'icecast', 'icecast2', 'zenmap', 'ndiff', 'nikto', 'p0f', 'deluge-gtk', 'ettercap', 'hashcat', 'logkeys', 'lkl', 'uberkey', 'nikito', 'tightvnc', 'pyrit', '4g8', 'squid', 'Burp Suite', 'kraken', 'crack', 'aircrack-ng', 'lcrack', 'pdfcrack', 'rarcrack', 'sipcrack', 'zeitgeist', 'nfs-common', 'Armitage', 'armitage', 'Metasploit', 'metasploit', 'ophcrack', 'tetris', 'netris', 'john', 'medusa', 'netcat', 'nmap', 'nginx', 'lolcat', 'fcrackzip', 'fof', 'goldeneye', 'hydra', 'samba', 'ssh']


#-------------------real_check-----------------------------
for pak in Package_list:
    pak_to_check = pak

    #----------------Runs_command_in_console-----------------
    console_output = run(f'dpkg -s {pak_to_check}')
    #print()

    #------------If_not_installed---------------------------
    if 'dpkg-query:' in console_output[0].split()[0]:
        if console_output[0].split()[2] == ("\'" + pak_to_check + "\'"):
            print(f"'{pak_to_check}' missing!")
            with open(r'Mal_pack_log.txt', 'a') as file: 
                file.write(f"'{pak_to_check}' missing!\n")

    #-----------If_installed------------------------------------
    elif f"Package: {pak_to_check}" == console_output[0]:
        if console_output[1] == 'Status: install ok installed':
            print(f"                   '{pak_to_check}' found!!! (Added to log)")
            with open(r'Mal_pack_log.txt', 'a') as file: 
                file.write(f"                   '{pak_to_check}' found!!!           sudo apt-get purge --autoremove {pak_to_check}              CHECK IF NEEDED FIRST I STG\n")
