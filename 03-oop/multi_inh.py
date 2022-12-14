class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'{self.num_arrows} arrows left')

    def run(self):
        print('ran really fast')


class HybridBindary(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

    def attack(self):
        Archer.attack(self)
        Wizard.attack(self)

    def run(self):
        print('hybrid bindary')

    def check_arrows(self):
        print('hybrid bindary')


hb1 = HybridBindary('hb1', 100, 10)
print(hb1.sign_in())
