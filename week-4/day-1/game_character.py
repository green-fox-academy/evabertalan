class GameCharacter:
    def __init__(self, name, health_point, damage):
        self.name=name
        self.health_point=health_point
        self.damage=damage

    def print_status(self):
        if self.health_point<=0:
            print("Dead")
        else:
            print(str(self.name)+" has: "+ str(self.health_point)+" HP")

    def drink_potion(self, amount):
        self.health_point+=10

    def strike(self, other):
        other.health_point-=self.damage
        print( )
        print(str(self.name)+' hits '+ str(other.name)+'. ' +  str(other.name) +'\'s ' +'damaged with: '+str(self.damage))


class Cerlic(GameCharacter):
    def heal(self,ally):
        ally.health_point+=20
        print("Ally HP: "+ str(ally.health_point))


one=GameCharacter('Huba', 100, 50)
two=GameCharacter('Buci', 70, 20)
pap=Cerlic('Melkor', 1000, 80)

one.print_status()
two.print_status()

for i in range(3):
    one.strike(two)
    pap.heal(two)

one.print_status()
two.print_status()
