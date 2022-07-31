class PlayerCharacter:
    membership = True

    def __init__(self, name, health=100):
        if PlayerCharacter.membership:
            self.name = name
            if health > 0:
                self.health = health
            self.power = 10
            self.coins = 20
            self.alive = True

    def run(self):
        self.health -= 10
        print(f'Running, health: {self.health}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Omar', num1 + num2)
    
    @staticmethod
    def adding_things_static(num1, num2):
        return num1 + num2
