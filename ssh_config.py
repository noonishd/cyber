from main import run, doubleprint
import os

def main():
    doubleprint(f'\n\n\nSSH:\n\n\n')
    #os.system("ssh-keygen")
    #os.system(f"ssh-copy-id {run('whoami')[0]}@localhost")
    input(f"ssh-keygen\nssh-copy-id {run('whoami')[0]}@localhost\nssh {run('whoami')[0]}@localhost\nDo this in another terminal rn")

    doubleprint(f'\n(sudo gedit /etc/ssh/sshd_config)\n', sendtext=False)
    doubleprint(f'(sudo nano /etc/ssh/sshd_config)\n\n', sendtext=False)

    keywords = [
        "PermitEmptyPasswords",
        "PermitRootLogin",
        "RSAAuthentication",
        "PubkeyAuthentication",
        "HostbasedAuthentication",
        "PasswordAuthentication",
        "X11Forwarding",
        "PermitUserEnvironment",
        "MaxAuthTries"
    ]

    new_lines = [
        "PermitEmptyPasswords no\n",
        "PermitRootLogin no\n",
        "RSAAuthentication yes\n",
        "PubkeyAuthentication yes\n",
        "HostbasedAuthentication no\n",
        "PasswordAuthentication no\n",
        "X11Forwarding no\n",
        "PermitUserEnvironment no\n",
        "MaxAuthTries 4\n"
    ]


    with open(r'/etc/ssh/sshd_config', 'r') as file:
        edits = file.readlines()
        #set_back = file.readlines()
        for i in range(len(edits)):
            for word in keywords: #------------------------------------------------------------Comment out important stuff to append later
                if word in edits[i]:
                    edits[i] = '#' + edits[i]
                    doubleprint(f'Commented {word}\n')
                    


    for line in new_lines: #---------------------------------------------------------------------to Append
        edits.append(line)
        doubleprint(f'Added to end: {line}')


    with open(r'/etc/ssh/sshd_config', 'w') as file:#--------------------------------------------------Appended
        file.writelines(edits)
        doubleprint('/etc/ssh/sshd_config overwritten!\n')

    run("systemctl restart ssh", sendToTerminal=True)

if __name__ == "__main__":
    main()