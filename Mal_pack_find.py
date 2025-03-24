#Double check iodines, icecasts, and ettercap
#unable to find logkeys, nikito, tightvnc, pyrit, lcrack, fof, 
#Check Burp Suite on ur own bc i think its uninstall is through gui
#Check Armitage

from main import run, doubleprint

#-------------------initializing--------------------------------------------------------------------------------------------------------------------------------------

package_list = ['apache2', 'remmina', 'deluge', 'tcpdump', 'iodine', 'iodine-client', 'manaplus', 'gameconqueror', 'wireshark', 'icecast', 'icecast2', 'zenmap', 'ndiff', 'nikto', 'p0f', 'deluge-gtk', 'ettercap', 'hashcat', 'logkeys', 'lkl', 'uberkey', 'nikito', 'tightvnc', 'pyrit', '4g8', 'squid', 'Burp Suite', 'kraken', 'crack', 'aircrack-ng', 'lcrack', 'pdfcrack', 'rarcrack', 'sipcrack', 'zeitgeist', 'nfs-common', 'Armitage', 'armitage', 'Metasploit', 'metasploit', 'ophcrack', 'tetris', 'netris', 'john', 'medusa', 'netcat', 'nmap', 'nginx', 'lolcat', 'fcrackzip', 'fof', 'goldeneye', 'hydra', 'samba', 'ssh', 'sucrack', 'unworkable', 'changeme']

check = input('Enter the REQUIRED programs separated by spaces:')
check = list(set(check.split(' ')))
for pack in check:
    if pack in package_list:
        package_list.remove(pack)

doubleprint(f'\n\n\n#Double check iodines, icecasts, and ettercap\n#unable to find logkeys, nikito, tightvnc, pyrit, lcrack, fof, \n#Check Burp Suite on ur own bc i think its uninstall is through gui\n#Check Armitage\n\n\n')

#-------------------real_check-----------------------------
for pak in package_list:
    pak_to_check = pak

    #----------------Runs_command_in_console-----------------
    console_output = run(f'dpkg -s {pak_to_check}')
    #print()

    #------------If_not_installed---------------------------
    if 'dpkg-query:' in console_output[0].split()[0]:
        if console_output[0].split()[2] == ("\'" + pak_to_check + "\'"):
            doubleprint(f"'{pak_to_check}' missing!\n")

    #-----------If_installed------------------------------------
    elif f"Package: {pak_to_check}" == console_output[0]:
        if console_output[1] == 'Status: install ok installed':
            doubleprint(f"                   '{pak_to_check}' found!!!           sudo apt-get purge --autoremove {pak_to_check}              CHECK IF NEEDED FIRST I STG\n")
        #-----------------------------Deleting------------------------------------
        if input(f'Delete {pak_to_check}? (y/n): ') == 'y':
            run(f'sudo apt-get purge --autoremove {pak_to_check} -y')
            doubleprint(f'                Uninstalled {pak_to_check}\n')

# to be installed
if len(pack) > 0:
    for pack in check:
        doubleprint(f'                     Installing {pack}')
        run(f'sudo apt install {pack} -y')
        doubleprint(f"                          '{pack}' installed!!!\n")