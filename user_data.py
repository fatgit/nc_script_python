#!/usr/bin/python

import connect


data = raw_input('Enter name server, user: ').split(' ')

username = data[2]
# domen = data[3]


check_domen = connect.request_to_server(data[0], data[1], 'grep DNS= /var/cpanel/users/' + username)
domen = check_domen.split('=')
domen = domen[1].split('.')
domen = domen[0]

lveinfo = connect.request_to_server(data[0], data[1], 'lveinfo -u ' + username + ' --period=1d')
cron = connect.request_to_server(data[0], data[1], 'cat /var/spool/cron/' + username)
top = connect.request_to_server(data[0], data[1], 'top -c -d -n 1 -u ' + username)
af = connect.request_to_server(data[0], data[1], 'lynx -dump -width=500 http://localhost:81/whm-server-status | grep ' + domen)
print (top)
print(lveinfo + '\n' + cron + '\n' +  top + '\n' + af)
