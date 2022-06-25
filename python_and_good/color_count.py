colors = ['yellow', 'blue', 'red', 'blue', 'pink', 'yellow', 'green', 'violet']

colors_dict = {}

for color in colors:
    count = 0
    for i in range(0, len(colors)):
        if color.lower() == colors[i].lower():
            count += 1
        colors_dict.update({color: count})
print(colors_dict)
