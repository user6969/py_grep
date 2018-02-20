# Creates SSH connection to server
# Copies py_grep.py to /tmp folder
# Runs py_grep.py with parameters, i.e. log name, search criteria

import paramiko

USERNAME = 'user'
PASSWORD = 'secret'


def get_ip_address():
    ip = raw_input('Enter server ip address: ')
    return str(ip)


def get_log_name():
    name = raw_input('Enter log name mask: ')
    return str(name)


def get_identity():
    number = raw_input('Enter identification number: ')
    return number


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(get_ip_address(), username=USERNAME, password=PASSWORD)


sftp = client.open_sftp()
sftp.put('/source/py_grep.py', '/tmp/py_grep.py')
sftp.close()

log_name = get_log_name()
identity = get_identity()
stdout = client.exec_command('python /tmp/py_grep.py {} {}'.format(log_name, identity))[1]

for line in stdout:
    print line
client.close()


