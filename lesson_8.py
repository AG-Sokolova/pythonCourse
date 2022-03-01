class Car:
    def car_actions(self, act_1, act_2):
        self.a_move = act_1
        self.a_stop = act_2


car_1 = Car()
car_1.car_actions('Move', 'Stop')
print('car_1 =', car_1.a_move, car_1.a_stop)

car_2 = Car()
car_2.car_actions('Fly', 'Swim')
print('car_2', car_2.a_move, car_2.a_stop)

print('-------------')

class Track:
    def __init__(self, act_1, act_2):
        self.act_1 = act_1
        self.act_2 = act_2


track_1 = Track('Drive', 'Cheel')
print('Track_1 =', track_1.act_1, track_1.act_2)

track_2 = Track('Fly', 'Eat')
print('Track_2 =', track_2.act_1, track_2.act_2)

print('-------------')

class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('display_count =', Employee.emp_count)

    def display_employee(self):
        print('Name:', self.name, ', Salary:', self.salary)


emp_1 = Employee('Zoya', 2000)
emp_2 = Employee('Nata', 1700)
emp_3 = Employee('Dima', 1500)

emp_1.display_employee()
emp_2.display_employee()
emp_3.display_employee()

print('Count employee =', Employee.emp_count)
# -------------
emp_1.age = 20
print('emp_1 = Name:', emp_1.name, ', Age:', emp_1.age, ', Salary:', emp_1.salary)

emp_2.age = 38
print('emp_2 = Name:', emp_2.name, ', Age:', emp_2.age, ', Salary:', emp_2.salary)

attr_1 = getattr(emp_1, 'emp_count')
attr_2 = getattr(emp_2, 'age')
print('getattr_atter_1 =', attr_1, ', getattr_atter_2 =', attr_2)

print('hasattr_emp_1_age =', hasattr(emp_1, 'age'))

setattr(emp_1, 'car', 2)
print('car =', getattr(emp_1, 'car'))

delattr(emp_1, 'car')
print('delattr_emp_1_car = ', hasattr(emp_1, 'car'))
# -------------


print('-------------')
def ii(cl_ex, parms_list, ch):
    count = 0

    for i in parms_list:
        parm_value = count

        if i == 'children':
            setattr(cl_ex, i, ch)
            continue
        setattr(cl_ex, i, parm_value)
        count += 1


emp_4 = Employee('Dmitry', 2500)
parms_l = ['children', 'pets', 'cars']

ii(emp_4, parms_l, 2)

print('Name =', emp_4.name)
print('Salary =', emp_4.salary)
print('children =', emp_4.children)
print('pets =', emp_4.pets)
print('cars =', emp_4.cars)

print('cars', hasattr(emp_4, 'cars'))

delattr(emp_4, 'cars')
print('cars', hasattr(emp_4, 'cars'))
