import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num_1', type=int)
parser.add_argument('num_2', type=int)
parser.add_argument('action', type=str, default='div')

args = parser.parse_args()
print(args)

item_1 = args.num_1
item_2 = args.num_2
act = args.action

match act:
    case 'sum':
        result = item_1 + item_2
        print('result =', result)
    case 'multi':
        result = item_1 - item_2
        print('result =', result)
    case 'div':
        result = item_1 / item_2
        print('result =', result)
    case 'pow':
        result = item_1 ** item_2
        print('result =', result)

# if act == 'sum':
#     result = item_1 + item_2
#     print('result:', result)
# elif act == 'multi':
#     result = item_1 + item_2
#     print('result:', result)
# elif act == 'div':
#     result = item_1 / item_2
#     print('result:', result)


# parser = argparse.ArgumentParser()
# parser.add_argument('name', type=str)  # => --name Nastia
# parser.add_argument('age', type=int, default=20)  # => age 27
# args = parser.parse_args()
# print('Name =', args.name)
# print('Age', args.age)

# args_dict = args.__dict__
# for k, v in args_dict.items():
#     print(k, v)

# print('Hello, world')

# parms = sys.argv
# print('parms =', parms)

# parms = sys.argv[4:7]
# print('parms =', parms)

# sum_3 = []
# for el in parms[0:3]:
#     sum_3.append(int(el))
# sum_3 = sum(sum_3)
# print('sum_3 =', sum_3)

# parser = argparse.ArgumentParser
# parser.add_argument('--name', type=str)  # => --name='Nastia'
# parser.add_argument('--age', type=int)  # => --age=27
# args = parser.parse_args()
# print('Name =', args.name)
# print('Age', args.age)
