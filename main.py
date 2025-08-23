#!/usr/bin/env python
# encoding: utf-8



# if ever stuck downloading
#sudo killall apt apt-get
#sudo dpkg --configure -a
import os
import subprocess

#------------------------Dependencies-----------------------------------
try:
    import pytz
    import npyscreen
except ModuleNotFoundError:
    os.system('sudo apt install pip -y')
    os.system('pip install pytz')
    os.system('pip install npyscreen')

from datetime import datetime
import time

#----------------------------Important procedures-----------------------------
def run(cmd, sendToTerminal=False):
    output_lines = []
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

    for line in process.stdout:
        stripped = line.strip()
        if sendToTerminal:
            print(stripped)
        output_lines.append(stripped)

    process.wait()

    return output_lines

def doubleprint(text, sendfile=True, sendtext=True):
    if sendfile:
        with open(r'master_log.txt', 'a') as file: 
            file.write(text)
    if sendtext:
        print(text, end="")

#-------------------Creating_log_if_doesn't_exist_alr--------------------------
if not(os.path.exists(run('pwd')[0] + '/master_log.txt')):
    with open(r'master_log.txt', 'w') as file: 
        file.write(f'\n\n\n\n\n\nLog created: {datetime.now(pytz.timezone("Canada/Pacific")).strftime("%I:%M:%S:%p")}')

if __name__ == '__main__':
    os.system('sudo chmod 755 main.py')

    #-------------------------Display Section-----------------------------
    os.system('sudo chmod 755 display.py')
    from display import main as display
    scripts_to_run = display()
    
    #---------------------------Grabbing procedures-------------------------
    os.system('sudo chmod 755 user_audit.py')
    from user_audit import main as user_audit

    os.system('sudo chmod 755 mal_pack_find.py')
    from mal_pack_find import main as mal_pack_find
    
    os.system('sudo chmod 755 login_defs_config.py')
    from login_defs_config import main as login_defs_config

    os.system('sudo chmod 755 pams.py')
    from pams import main as pams

    os.system('sudo chmod 755 ssh_config.py')
    from ssh_config import main as ssh_config

    #---------------------Non-file scripts--------------
    def firewall():
        doubleprint("\n\n\nFirewall:\n\n\n")
        doubleprint("Installing ufw...\n")
        firewall_output = run("sudo apt install ufw") #for debug
        firewall_output2 = run("sudo ufw enable")
        doubleprint(firewall_output2[-1] + "\n")

    def clam():
        doubleprint("\n\n\nClamAV:\n\n\n")
        clam_output = run("sudo apt install clamav -y")
        if 'E: Unable to locate package' in clam_output:
            doubleprint('ClamAV install failed: updating sources\n')
            run('sudo apt update')
            run('sudo apt install clamav -y')
            doubleprint('clamav installed\n')
        if input("Are you ABSOLUTELY SURE you want to scan right now? (Will take ages) (y/n):") == 'y':
            doubleprint("Scanning system (this may take a while go grab a snack or smth)...")
            clam_output2 = run("sudo freshclam")
            clam_output3 = run("clamscan -r /", sendToTerminal=True)
            print(clam_output3)

    def rc_local():
        doubleprint("\n\n\nrc.local:\n\n\n")
        with open(r'/etc/rc.local', 'w') as file:#--------------------------------------------------Appended
            file.writelines([])
        doubleprint('/etc/rc.local emptied!\n')

    #add to this to make it run after being selected through gui
    scripts = [
        "all",
        user_audit,
        mal_pack_find,
        login_defs_config,
        pams,
        firewall,
        clam,
        ssh_config,
        rc_local]


    #------------Script runner-----------------
    if len(scripts_to_run) < 1:
        print("Chose no scripts!!")
        quit()
    elif 0 == scripts_to_run[0]:
        for script in scripts[1:]:
            script()
            input('Press enter to continue...   ')
    else:
        for i in scripts_to_run:
            scripts[i]()
            input('Press enter to continue...   ')
