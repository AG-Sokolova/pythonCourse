file_path = 'file/'
text_file_title = 'text_1.txt'

file_title = file_path + text_file_title


# f = open(file_title, 'w')
# f.write('Hello, World')  # => 'Hello, World' в новом созданном файле
# f.close()

ll = ['QA', 'Automation', 'employees']

# w - создает файл
# x - проверяет существует ли файл с таким именем
# a - добавляет в уже существующий файл новые данные
# r - чтение

# with open(file_title, 'w', encoding='utf-8') as f:
    # f.write('Hello QA')  # => Hello QA
    # f.write(str(ll))  # => список ll ['QA', 'Automation', 'employees']
    # f.writelines(ll)  # => QAAutomationemployees
    # f.write('\n'.join(ll))  # => QA /n Automation /n employees

    # for i in ll:
        # f.write(i)
        # f.write('\n')  # => QA /n Automation /n employees

        # f.writelines(i)  # => QAAutomationemployees
        # f.write('\n')  # => QA /n Automation /n employees

    # for n in range(0, 10):
    #     for i in ll:
    #         w_line = str(n) + '_' + i
    #         f.write(w_line)
    #         f.write('\n')

# with open(file_title, 'r') as f:
    # ff = f.read()
    # ff = f.read(10)
    # print(ff)

    # ff = f.readlines()
    # print(len(ff)) # => количество строк

    # ff = f.readlines()
    # print(ff)
    #
    # for lines in ff:
    #     print(lines)
    #     print(lines.rstrip())

with open(file_title, 'r') as f:
    ff = f.readlines()
    print(ff)
    del ff[1]
    with open(file_title, 'w') as wf:
        wf.writelines(ff)




