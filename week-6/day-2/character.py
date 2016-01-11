class Character():
    def __init__(self, name, dexterity, luck, health, inventory):
        self.name=name
        self.dexterity=dexterity
        self.luck=luck
        self.health=health
        self.inventory=inventory

    def get_character(self):
        return(self.name+" "+str(self.dexterity)+" "+str(self.luck)+" "+str(self.health)+" "+str(self.inventory))
