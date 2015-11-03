#!/usr/bin/python
import connect

data = raw_input ('Enter name server, nusers name:').split(' ')
answer1 = raw_input ('Where can I find?\n1. /var/cpanel/\n2. Backup')
if answer1 == '1':
    bash_check = 'cat /var/cpanel/users/'+ data[2]
elif answer1 == '2':
    bash_check = 'cat /backup/cpbackup/daily/' +data[2] + '/cp/' + data[2]



info= (connect.request_to_server(data[0], data[1], bash_check))
print info
print ('Number of domains = {0}').format(info.count('DNS'))
