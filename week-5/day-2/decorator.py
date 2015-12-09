class Sword:
    def damage(self):
        return 10

class Rusty:
    def __init__(self, weapon):
        self.weapon=weapon
    def damage(self):
        return self.weapon.damage()/2

class Enhanced:
    def __init__(self, weapon):
        self.weapon=weapon

    def damage(self):
        return self.weapon.damage()+ 5

class Magical:
    def __init__(self, weapon):
        self.weapon=weapon

    def damage(self):
        return self.weapon.damage()*2

class Warrior:
    def __init__(self, weapon=Sword()):
        self.hp=100
        self.weapon=weapon

    def strike(self, opponent):
        damage=self.weapon.damage()
        opponent.hp-=damage


    def strike(self, opponent):
        damage=self.weapon.damage()
        opponent.hp-=damage

warrior=Warrior(Magical(Enhanced(Rusty())))
opponent=Warrior(Sword())

print(opponent.hp)
warrior.strike(opponent)
print(opponent.hp)
