import subprocess
import time

list_email = []
list_branch_name = []


def read_file_email(path, list_mail):
    with open(path, 'r') as get_email:
        lines = get_email.read().splitlines()
        for line in lines:
            list_mail.append(line)
    get_email.close()
    return list_mail

def name_resolution(list_mail, list_branch):
    for mail in list_mail:
        name = mail.split('@')
        name = name[0].lower()
        list_branch.append(name)
    return list_branch

def script_bash(path, name):
    environment = '#!/bin/bash'
    with open(path, 'w') as add_branch:
        add_branch.write(environment + '\n')
        add_branch.write(f'git branch test/{name}' + '\n')
        add_branch.write(f'git push -u origin test/{name}' + '\n')
    add_branch.close()

def run_scripts(path):
    proc = subprocess.Popen(path, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    print(output)


read_file_email('email_list.txt', list_email)
name_resolution(list_email, list_branch_name)



for branch_name in list_branch_name:
    script_bash('test.sh', branch_name)
    run_scripts('./test.sh')
    time.sleep(3)





