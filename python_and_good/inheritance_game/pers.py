class Hero:
    def __init__(self, name, toTypeHero, toAttack, clothes):
        self.name = name
        self.clothes = clothes  # => одежда
        self.damage = 0
        self.toTypeHero = toTypeHero
        self.toAttack = toAttack

    def attack(self):
        print(f'{self.toTypeHero} {self.name}, нанес удар {self.toAttack}. УРОН - {self.damage}')

    def casualties(self):
        self.damage += len(self.clothes)
        return self.damage


class Warrior(Hero):
    def __init__(self, name, *clothes):
        super().__init__(name, "Воин", "мечом", *clothes)

        super().casualties()

class Wizard(Hero):
    def __init__(self, name, healing, *clothes):
        super().__init__(name, "Маг", "огненым шаром", *clothes)

        self.healing = healing

        if healing:
            self.damage += 5

        super().casualties()

class Ranger(Hero):
    def __init__(self, name, *clothes):
        super().__init__(name, "Рейнджер", "из лука", *clothes)

        super().casualties()


if __name__ == "__main__":
    Wizard("Геральд", False, ["мантия", "доспехи", "зелья"]).attack()
