import random

class Character():
    def __init__(self, name, dexterity, luck, health, inventory):
        self.name=name
        self.dexterity=dexterity
        self.luck=luck
        self.health=health
        self.inventory=[]

    def get_dexterity(self):
        self.dexterity=random.randint(1, 6)
        print("Your dexterity points are: " + str(self.dexterity) +" + 6 = " + str(self.dexterity+6))

    def get_luck(self):
        self.luck=random.randint(1, 6)
        print("Your health points are: "+ str(self.health) +" + 12 = " + str(self.health+12))

    def get_health(self):
        self.health=random.randint(1, 12)
        print("Your health points are: "+ str(self.luck) +" + 6 = " + str(self.luck+6))

    def get_inventory(self, item):
        self.inventory.append(item)

    def get_character(self):
        return("\n"+"Character name: "+self.name+"\n "+"Dexterity: "+str(self.dexterity)+"\n "+"Luck: "+str(self.luck)+"\n "+'Health: '+str(self.health)+"\n"+"Inventory: "+str(self.inventory)+"\n")
