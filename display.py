#!/usr/bin/env python
# encoding: utf-8

import npyscreen


def main():

    options =[
        "Run All :)", #0
        "Audit users (user_audit.py)", #1
        "Package managing (mal_pack_find.py)", #2
        "Login config (login_defs_config.py)", #3
        "Pams (pams.py)", #4
        "Firewall (firewall in main)", #5
        "ClamAV (clam in main)" #6
    ]

    def myFunction(*args):
        F = npyscreen.Form(name='Linux Script Selector')
        myFW = F.add(npyscreen.TitleMultiSelect, max_height=-2, value = [], name="Choose scripts to run (Ctrl + C to exit):",
                    values = options, scroll_exit=True)   # options are list above
        F.edit()
        return myFW.value   # returns list with option as index

    
    return npyscreen.wrapper_basic(myFunction) # returns list to main

if __name__ == '__main__':
    main()