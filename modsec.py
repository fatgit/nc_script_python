#!/usr/bin/python

import connect

data = raw_input ('Enter name server, username, role:').split(' ')
username = data[2]
rule = data[3]
path_std = '/usr/local/apache/conf/userdata/std/2_2/'
path_ssl = '/usr/local/apache/conf/userdata/ssl/2_2/'
path_ssl_std = [path_std, path_ssl]
check_user = connect.request_to_server(data[0], data[1], 'id ' + username).split(' ')



if check_user[2] != 'No':
    print 'User has been found'
    bash_restart_httpd = 'service httpd restart'
    for path in path_ssl_std:
        bash_create_modsec = 'echo -e "<LocationMatch .*>\n</LocationMatch>" > ' + path + username + '/modsec.conf'
        bash_edit_modsec = 'sed -i "/<LocationMatch .*>/ a      SecRuleRemoveById ' + rule + '" ' + path + username +'/modsec.conf'
        bash_create_folder = 'mkdir ' + path + username + '; chmod 775 ' + path + username
        bash_grep_rules = 'grep ' + rule +' ' + path + username + '/modsec.conf'
        bash_check_dir = 'ls -l ' + path + ' | grep ' + username
        dir_path = connect.request_to_server(data[0], data[1], bash_check_dir)


        if dir_path:
            print (dir_path)
            bash_check_modsec = 'ls ' + path + username + '/modsec.conf'
            bash_check_modsec_result = connect.request_to_server(data[0], data[1], bash_check_modsec).split(' ')
            print bash_check_modsec_result

            if len(bash_check_modsec_result) > 1:

                print (connect.request_to_server(data[0], data[1], bash_create_modsec + '; ' + bash_edit_modsec))
            else:
                if connect.request_to_server(data[0], data[1], bash_grep_rules) == '':
                    print (connect.request_to_server(data[0], data[1], bash_edit_modsec))
                else:
                    print ('Rule already is!!!!')
        else:
            print ('Directory is empty')
            print (connect.request_to_server(data[0], data[1], bash_create_folder + '; ' + bash_create_modsec + ';' + bash_edit_modsec ))
    print (connect.request_to_server(data[0], data[1], bash_restart_httpd))
    print 'Modsec {0} is ready'.format(username)
else:
    print 'User has not found'




