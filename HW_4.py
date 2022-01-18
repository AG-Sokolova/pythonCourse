import time

count = 0  # 1
range_count = 10  # 2
for_count = 0  # 3
run = True  # 4

# While

# # 5. Сделать цикл while который будет работать пока run
# while run:
#     print('Hello, Cycle')

# # 6. Сделать цикл while который будет работать пока run
# while run:
#     print('Step =', count)
#     time.sleep(0.3)
#     count += 1

# # 7. Сделать цикл while который будет работать пока count < range_count
# while count < range_count:
#     print('Step =', count)
#     count += 1

# # 8. Сделать цикл while который будет работать пока count < range_count
# while count < range_count:
#     count += 1
#     if count == 3:
#         print('Step =', count, 'if body')
#     else:
#         print('Step =', count)

# # 9. Сделать цикл while который будет работать пока run
# while run:
#     print('Step =', count)
#     count += 1
#     if count == range_count:
#         print('STOP', count)
#         break

# For

# # 10. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
# for item in range(for_count, range_count):
#     print('Step =', item)

# # 11. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
# for item in range(0, 30):
#     if item == 5 or item == 10 or item == 4 or item == 27:
#         print('item =', item)
#     else:
#         print('Step =', item)

# # 12. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# for item in range(0, range_count+1):
#     print('Step =', item)
#     if item == 7:
#         inner_count = 0
#         print('--inner_count =', inner_count)
#         for inner_item in range(0, item):
#             print('-------- Inner_Step =', inner_item)
#             if inner_item == 5:
#                 inner_count = inner_item
#         print('--inner_count =', inner_count)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
for item in range(0, 20):
    if (7 < item) and (item < 12):
        print('If_item =', item)
        continue
    else:
        print('Step =', item)
print('End_iteration =', item)
