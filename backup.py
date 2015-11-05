#!/usr/bin/python

import connect

data = raw_input ('Enter name server, nusers name:').split(' ')
print ('Now we are checking if backup is...')

# bash_check_backup = 'ls -la /backup/cpbackup/daily/ | grep ' + data[2]
# bash_check_backup = 'date -r /backup/cpbackup/daily/' + data[2] + '/version'
bash_check_backup = 'date +%m.%-d.%Y_%H-%M-%S -r /backup/cpbackup/daily/' + data[2] + '/version'


result_split = connect.request_to_server(data[0], data[1], bash_check_backup)[:-1]

if result_split.find('No such file or directory') != -1:
    print 'Backup has not been found'
else:
    print (('Backup has been found: {0} {1}').format(result_split, data[2]))
    print(connect.request_to_server(data[0], data[1], 'du -sh /backup/cpbackup/daily/' + data[2]))
    answer1 = raw_input ('Do you want to create an archive of backup? (y/n)')
    if answer1 == ('y' or 'Y' or 'yes' or 'Yes'):
        name_of_archive = 'backup-' + result_split + '_' + data[2] + '.tar.gz'
        answer_link = raw_input ('Do you want to create a link on the backup? (y/n)')
        if answer_link == ('y' or 'Y' or 'yes' or 'Yes'):
            bash_create_backup = 'cd /backup/cpbackup/daily/' +data[2] + '/; tar cvfz /home/' + name_of_archive+ ' ./; ln -s /home/' + name_of_archive+ ' /etc/httpd/htdocs/' + name_of_archive
            print(bash_create_backup)
            connect.request_to_server(data[0], data[1], bash_create_backup)
            print('Archive: /home/' + name_of_archive + '\nLink: ' + connect.host + '/' + name_of_archive)

        else:
            bash_create_backup = 'cd /backup/cpbackup/daily/' +data[2] + '; tar cvfz /home/' + name_of_archive+ ' .'
            connect.request_to_server(data[0], data[1], bash_create_backup)
            print('Archive: /home/' + name_of_archive)