#Double check iodines, icecasts, and ettercap
#unable to find logkeys, nikito, tightvnc, pyrit, lcrack, fof, 
#Check Burp Suite on ur own bc i think its uninstall is through gui
#Check Armitage


import os
import subprocess
import sys
import time
import pexpect
from datetime import datetime


pexpect.run('sudo su')
pexpect.run('clear')
pexpect.run('sudo chmod 755 Mal_pack_find.py')
pexpect.run('pip install pytz')

import pytz
#-------------------Creating_log_if_doesn't_exist_alr-------------------------- 
if not(os.path.exists(pexpect.run(f'pwd').decode('UTF-8').strip() + '/Mal_pack_log.txt')):
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
    console_output = pexpect.run(f'dpkg -s {pak_to_check}').decode('UTF-8').split()
    #print()

    #------------If_not_installed---------------------------
    if 'dpkg-query:' in console_output[0]:
        if console_output[2] == ("\'" + pak_to_check + "\'"):
            print(f"'{pak_to_check}' missing!")
            with open(r'Mal_pack_log.txt', 'a') as file: 
                file.write(f"'{pak_to_check}' missing!\n")

    #-----------If_installed------------------------------------
    elif "Package:" == console_output[0]:
        index = console_output.index('Status:')
        if console_output[index+1] == 'install' and console_output[index+2] == 'ok' and console_output[index+3] == 'installed':
            print(f"                   '{pak_to_check}' found!!! (Added to log)")
            with open(r'Mal_pack_log.txt', 'a') as file: 
                file.write(f"                   '{pak_to_check}' found!!!           sudo apt-get purge --autoremove {pak_to_check}              CHECK IF NEEDED FIRST I STG\n")
