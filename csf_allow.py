#!/usr/bin/python

import connect
import argparse


data = raw_input('Enter name server, user, port, chat:').split(' ')


username = data[2]
port = data[3]
chat = data[4]
id_user = connect.request_to_server(data[0], data[1], 'id -u ' + username)

# if check_user[2] != 'No':
try:
    id_user_id = int(id_user)
    id_user_id = str(id_user_id)
    bash_rule_in_csf = 'sed -i "/#=-=-=-= Custom ACL  =-=-=-=#/ a tcp:out:d=' + port + ':u=' + id_user_id + '           # caht ID ' + chat + '" /etc/csf/csf.allow'
    print(bash_rule_in_csf)
    # print (connect.request_to_server(data[0], data[1], bash_create_modsec + '; ' + bash_edit_modsec + '; ' + bash_restart_httpd))
    print (connect.request_to_server(data[0], data[1], bash_rule_in_csf + '; csf -r '))



except ValueError:
    print('User has been not found')

