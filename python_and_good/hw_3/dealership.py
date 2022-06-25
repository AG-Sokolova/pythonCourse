class Car:
    """Информация о машине"""

    def __init__(self, make, model, year, price, failures):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.failures = failures

        if len(self.failures) != 0:
            self.is_broken = True
        else:
            self.is_broken = False

    def __str__(self):
        return f"\n ===="\
               f"\n \033[1m Марка и модель машины: {self.make} {self.model} \033[0m"\
               f" \n Год выпуска машины: {self.year}" \
               f" \n Поломки в машине на данный момент: {self.failures}" \
               f" \n Цена машины: {self.price}$ "

    def is_drivable(self):
        """проверяет, работает ли машина"""
        if ("Transmission" not in self.failures) or ("Engine" not in self.failures):
            return True

    def fix(self, failure):
        """отремонтировать поломку"""
        if failure in self.failures:
            self.failures.remove(failure)
            self.price += 200.0
        else:
            print(f'{failure} такой поломки нет в машине {self.make, self.model}')
        # если поломок нет, то возвращается False в is_broken
        if len(self.failures) == 0:
            self.is_broken = False


class Inventory:

    def __init__(self, cars):
        self.cars = cars
        self.profit = 0

    def __str__(self, result=''):
        for car in self.cars:
            result += str(car)
        return result

    def add_car(self, make, model, year, price, failures):
        """добавить новый объект в список и в класс Car"""
        self.cars.append(Car(make, model, year, price, failures))

    def sell(self, car):
        # переменная profit увеличивается, если машина продана
        """продажа машины"""
        if car in self.cars:
            if car.is_drivable():
                self.cars.remove(car)
                self.profit = self.profit + car.price
                print(f'{car} \n \033[32m ПРОДАНО \033[0m')
            else:
                print(f'{car} \n \033[31m ПРОДАТЬ НЕЛЬЗЯ, есть поломки \033[0m')
        else:
            print(f'{car} \n \033[32m такой машины НЕТ \033[0m')

    def send_car_for_maintanance(self, car):
        """тех. обслуживание машины"""
        if car in self.cars:
            for failure in car.failures[::-1]:
                car.fix(failure)

    def get_car(self, make, model):
        """найти и вывести машину по марке и модели"""
        for car in self.cars:
            if car.make == make and car.model == model:
                return print(car)
            else:
                return print("\033[31m \n Вы искали: " + make + " " + model + " - такой машины нет в списке \033[0m")