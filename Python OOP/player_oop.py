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


player1 = PlayerCharacter('Omar', 100)
print(player1.name)
player1.run()
player1.run()
