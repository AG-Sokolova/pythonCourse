# OOP
class car:
    color = 'red'
    form = 'sedan'
    engine = '3'
    speed = 100

    def moove(self, speed):
        self.speed = speed

    def change_color(self, color):
        self.color = color

    def change_form(self, newform):
        self.form = newform


obj_1 = car()
obj_2 = car()


print('color =', obj_1.color)
print('form =', obj_1.form)
print('engine =', obj_1.engine)
print('speed =', obj_1.speed)

print('--------------')

print('2_color =', obj_2.color)
print('2_form =', obj_2.form)
print('2_engine =', obj_2.engine)
print('2_speed =', obj_2.speed)

print('--------------')

obj_1.moove(50)
obj_1.change_color('black')
print('obj1_change_speed =', obj_1.speed)
print('obj1_change_color =', obj_1.color)

obj_2.moove(78)
print('obj2_change_speed =', obj_2.speed)


print('-------------- InitVariant')
class InitVariant:
    def __init__(self, color, action):
        self.c_color = color
        self.c_action = action


obj_i1 = InitVariant('While', 'move')
print(obj_i1.c_color, obj_i1.c_action)


print('-------------- No_InitVariant')
class No_InitVariant:

    def car_actions(self, act_1, act_2):
        self.act_1 = act_1
        self.act_2 = act_2


obj_2 = No_InitVariant()
obj_2.car_actions('move', 'stop')
print(obj_2.act_1, obj_2.act_2)
