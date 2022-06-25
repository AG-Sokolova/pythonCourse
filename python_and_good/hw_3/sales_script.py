from dealership import *

if __name__ == "__main__":
    """инициализация входных данных"""
    car_1 = Car("Nissan", "Altima", 2000, 1000.0, ["Engine", "Windshield"])
    car_2 = Car("Honda", "CRV", 2002, 4300.0, [])
    car_3 = Car("Honda", "Accord", 2002, 2200.0, ["Exaust Pipe"])
    car_4 = Car("Nissan", "Frontier", None, 6900.0, ["Engine", "Transmission", "Oxigen Sensor", "Steering Wheel"])
    car_5 = Car("Toyota", "Tacoma", 2019, 25000.0, [])
    car_6 = Car("Tesla", "Model3", 2022, 56000.0, [])

    invent = Inventory([car_1, car_2, car_3, car_4, car_5, car_6])
    # print(invent)

    """задание"""
    invent.sell(car_5)  # => Продать Тойоту
    invent.sell(car_4)  # => Продать Ниссан фронтир
    car_1.fix('Windshield')  # => Починить Windsheild в ниссане алтима
    invent.send_car_for_maintanance(car_4)  # => Отправить ниссан фронтир не тех обслуживание
    invent.sell(car_4)  # => Попробовать продать ниссан фронтир еще раз
    print("\n \033[42m\033[30m Общая выгода с продажи: \033[0m", invent.profit)  # => Вывести общий profit на экран

    """Дополнительно"""
    print('===========================================================')
    print(invent)

    # print('===========================================================')
    # invent.get_car("Nissan", "JBJBb")  # => проверка работы метода get_car()