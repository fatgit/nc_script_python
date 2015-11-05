#!/usr/bin/python

import connect

data = raw_input ('Enter name server, user name:').split(' ')

user = data[2]
bash_list_quarantine = 'cd /opt/cxs/quarantine/cxsuser/' + user +'; ls -la; cxs --force ./'

print(connect.request_to_server(data[0], data[1], bash_list_quarantine))

show_file = raw_input ('Do you want to look into file?(n/name file)')
if show_file != ('n' or 'no'):
    bash_cat_file = 'cat /opt/cxs/quarantine/cxsuser/' + user + '/' + show_file
    print(connect.request_to_server(data[0], data[1], bash_cat_file ))

restore_file = raw_input('Do you want to restore the file?(n/name file)')

if restore_file != ('n' or 'no'):
    md5sum = connect.request_to_server(data[0], data[1], 'md5sum /opt/cxs/quarantine/cxsuser/' + user +'/'+ restore_file)
    md5sum = md5sum.split(' ')
    md5sum = md5sum[0]
    bash_actfile = 'grep actfile /opt/cxs/quarantine/cxsuser/' + user +'/'+ restore_file + '.restore4'
    bash_actfile = connect.request_to_server(data[0], data[1], bash_actfile).split('=')
    bash_actfile = bash_actfile[1]
    print(bash_actfile)
    # bash_actfile = bash_actfile[1]
    # print(bash_actfile)
    bash_whitelist = 'echo md5sum:' + md5sum + ' >> /etc/cxs/cxs.ignore; echo md5sum:' + md5sum + ' >> /etc/cxs/cxs.ignore.watch ; cp ' + restore_file + ' ' + bash_actfile + '; chown '  + user + '. ' + bash_actfile
    print(bash_whitelist)
    # print(connect.request_to_server(data[0], data[1], bash_whitelist))
    bash_check_file = 'ls ' + bash_actfile
    # print(connect.request_to_server(data[0], data[1], bash_check_file))