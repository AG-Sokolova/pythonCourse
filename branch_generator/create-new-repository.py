import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url_repository', type=str)

args = parser.parse_args()

url = args.url_repository

def script_bash(path, url):
    with open(path, 'w') as new_repository:
        script = f'''
        #!/bin/bash
        mkdir new-folder
        cd new-folder
        git init
        git add README.md
        git commit -m "first commit"
        git branch -M main
        git remote add origin {url}
        git push -u origin main
        '''
        new_repository.write(script)
    new_repository.close()


script_bash('new_repository.sh', url)

