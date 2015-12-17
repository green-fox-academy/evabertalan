import random

class Character():
    def __init__(self, name, dexterity, luck, health, inventory):
        self.name=name
        self.dexterity=dexterity
        self.luck=luck
        self.health=health
        self.inventory=["Sword", "Leather Armor"]

    def get_random(slef):
        return random.randint(1, 6)

    def get_dexterity(self):
        self.dexterity=self.get_random()+6
        print("Your dexterity points are: " + str(self.dexterity))

    def get_luck(self):
        self.luck=self.get_random()+6
        print("Your luck points are: "+ str(self.luck))

    def get_health(self):
        self.health=self.get_random()+self.get_random()+12
        print("Your health points are: "+ str(self.health))

    def get_inventory(self, item):
        self.inventory.append(item)

    def get_character(self):
        return("\n"+"Character name: "+self.name+"\n "+"Dexterity: "+str(self.dexterity)+"\n "+"Luck: "+str(self.luck)+"\n "+'Health: '+str(self.health)+"\n "+"Inventory: "+str(self.inventory)+"\n")

    def begin_character(self):
        return("\n"+"Character name: "+self.name+"\n "+'Max Health = Current Health: '+str(self.health)+"\n "+"Dexterity: "+str(self.dexterity)+"\n "+"Max Luck = Current Luck: "+str(self.luck)+"\n")

    def monster(self):
        self.dexterity=self.get_random()+6
        return("Monster:"+"\n "+'Max Health = Current Health: '+str(self.get_random()+self.get_random()+12)+"\n "+"Dexterity: "+str(self.dexterity)+"\n ")

    def lost_health(self):
        self.health=self.health-2
        return self.health

    def lost_character(self):
       return("\n"+self.name+"Max Health: "+str(self.health)+"\n"+"Cu")
