file_patch = '/d/github/pythonCourse/ lecture/lec_3/'
text_file_title = 'text.txt'

file_title = file_patch + text_file_title

# f = open(file_title, 'w')
# f.write('Hello file')
# f.close()

ll = ['QA', 'Automat', 'employee']

with open(file_title, 'w', encoding='utf-8') as f:
    # f.write('Hello QA')

    # f.writelines(ll)
    # f.write('\n'.join(ll))

    for i in ll:
        # f.write(i)
        # f.write('\n')
        f.writelines(i)
        f.write('\n')



