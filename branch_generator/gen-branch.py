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

def script_bash(path, list_branch):
    environment = '#!/bin/bash'
    with open(path, 'w') as add_branch:
        add_branch.write(environment + '\n')
        for name in list_branch:
            add_branch.write(f'git branch {name}')
            add_branch.write('\n')
            add_branch.write(f'git push -u origin {name}')
            add_branch.write('\n')
    add_branch.close()


read_file_email('email_list.txt', list_email)
name_resolution(list_email, list_branch_name)
script_bash('new-folder/branches.sh', list_branch_name)

