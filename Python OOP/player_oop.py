class PlayerCharacter:
    membership = True

    def __init__(self, name, health=100):
        if PlayerCharacter.membership:
            self._name = name
            if health > 0:
                self._health = health
            self._power = 10
            self._coins = 20
            self._alive = True

    def run(self):
        self._health -= 10
        print(f'Running, health: {self._health}')

    def speak(self):
        print(f'My name is {self._name} and I have {self._coins} coins.')


player1 = PlayerCharacter('Omar', 100)
print(player1._name)
player1.run()
player1.speak()

player1.name = "!!!!"
player1.speak = "BOOOOOO"

print(player1.speak)
