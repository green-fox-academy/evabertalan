import random

class Character():
    def __init__(self, name, dexterity, health):
        self.name=name
        self.dexterity=dexterity
        self.health=health

    def get_random(slef):
        return random.randint(1, 6)

    def get_dexterity(self):
        self.dexterity=self.get_random()+6
        print(" ")
        print("Your dexterity points are: " + str(self.dexterity))

    def get_health(self):
        self.health=self.get_random()+self.get_random()+12
        print("Your health points are: "+ str(self.health))
        print(" ")

    def monster_status(self):
        self.dexterity=self.get_random()+6
        self.health=self.get_random()+self.get_random()+12
        return("Monster:"+"\n "+'Max Health = Current Health: '+str(self.health)+"\n "+"Dexterity: "+str(self.dexterity)+"\n ")

    def lost_health(self):
        self.health=self.health-2
        return self.health

class Player(Character):
    def __init__(self, name, dexterity, luck, health, inventory):
        self.name=name
        self.dexterity=dexterity
        self.luck=luck
        self.health=health
        self.inventory=["Sword", "Leather Armor"]

    def get_luck(self):
        self.luck=self.get_random()+6
        print("Your luck points are: "+ str(self.luck))

    def get_inventory(self, item):
        self.inventory.append(item)

    def get_character(self):
        return("\n"+"Character name: "+self.name+"\n "+"Dexterity: "+str(self.dexterity)+"\n "+"Luck: "+str(self.luck)+"\n "+'Health: '+str(self.health)+"\n "+"Inventory: "+str(self.inventory)+"\n")

    def begin_character(self):
        return("\n"+"Character name: "+self.name+"\n "+'Max Health = Current Health: '+str(self.health)+"\n "+"Dexterity: "+str(self.dexterity)+"\n "+"Max Luck = Current Luck: "+str(self.luck)+"\n")

    def lost_character(self):
        self.health=self.health-2
        self.get_character()
