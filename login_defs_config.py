

from main import run, doubleprint
import os


def main():
    doubleprint(f'\n\n\nlogin.defs:\n\n\n')
    doubleprint(f'\n(sudo gedit /etc/login.defs)\n', sendtext=False)
    doubleprint(f'(sudo nano /etc/login.defs)\n\n', sendtext=False)

    keywords = ['PASS_MAX_DAYS', 'PASS_MIN_DAYS', 'PASS_WARN_AGE']
    new_lines = [
        'PASS_MAX_DAYS\t15\n',
        'PASS_MIN_DAYS\t7\n',
        'PASS_WARN_AGE\t7\n\n', ]


    with open(r'/etc/login.defs', 'r') as file:
        edits = file.readlines()
        set_back = file.readlines()
        for i in range(len(edits)):
            if '!authenticate' in edits[i] or '!NOPASSWD' in edits[i]: #----------------------Check for bad thingsc
                edits[i] = edits[i].replace('!authenticate', '').replace('!NOPASSWD', '')
                doubleprint('\n\n!authenticate or !NOPASSWD FOUND\n\n')
            for word in keywords: #------------------------------------------------------------Comment out important stuff to append later
                if word in edits[i]:
                    edits[i] = '#' + edits[i]
                    doubleprint(f'Commented {word}\n')


    for line in new_lines: #---------------------------------------------------------------------to Append
        edits.append(line)
        doubleprint(f'Added to end: {line}')


    with open(r'/etc/login.defs', 'w') as file:#--------------------------------------------------Appended
        file.writelines(edits)
        doubleprint('/etc/login.defs overwritten!\n')

    #WORKINGNGNGNGNGNG

if __name__ == '__main__':
    main()
