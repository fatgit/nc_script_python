#!/usr/bin/python

import paramiko
def request_to_server (name_server, number_server, command):
    global host
    if name_server == 's':
        host = 'server' + number_server + '.web-hosting.com'
    elif name_server == 'p':
        host = 'premium' + number_server + '.web-hosting.com'
    elif name_server == 'b':
        host = 'business' + number_server + '.web-hosting.com'
    elif name_server == 'h':
        host = 'host' + number_server + '.registrar-servers.com'

    key = paramiko.DSSKey.from_private_key_file('/home/fat/.ssh/id_dsa', password=',hjyz=3333')
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print ("connecting")
    c.connect(hostname=host, username='root', pkey=key, port=12789)
    stdin, stdout, stderr = c.exec_command(command)
    data = stdout.read() + stderr.read()
    c.close()
    return data
