from menu import Menu
from character import *
from menu_item import MenuItem
import random

user=Player("", 0, 0, 0, 0)
monster=Character("Monster", 0, 0)
attack=True

def after_strike():
    global attack
    if attack==True:
        print("Monster: ")
        print(" Max Health: " + str(monster.health))
        monster.health=monster.health-2
        print(" Current Health: " + str(monster.health))
        print(user.begin_character())
    elif attack==False:
        print(user.name)
        print(" Max Health: " + str(user.health))
        user.health=user.health-2
        print(" Current Health: " + str(user.health))
        print(user.lost_character())
        print(monster.monster_status())

def try_luck():
    roll=random.randint(1, 6)+random.randint(1, 6)
    print("Your rolled number: "+str(roll))
    print("Your luck: " + str(user.luck))
    if roll>user.luck:
        if attack==False:
            print(" Max Health: " + str(user.health))
            print("You lost 3 health points")
            user.health=user.health-1
            print(" Current Health: " + str(user.health))
        elif attack==True:
            print(" Max Monster Health: " + str(monster.health))
            print("Monster lost 1 health points")
            monster.health=monster.health+1
            print(" Current Monster Health: " + str(monster.health))
    elif roll<=user.luck:
        if attack==False:
            print(" Max Health: " + str(user.health))
            print("You lost only 1 health and 1 luck point")
            user.health=user.health+1
            user.luck=user.luck-1
            print(" Current Health: " + str(user.health))
            print(" Current Luck: " + str(user.luck))
        elif attack==True:
            print(" Max Monster Health: " + str(monster.health))
            print(" Monster lost 4 health and you lost 1 luck ")
            monster.health=monster.health-2
            user.luck=user.luck-1
            print(" Current Monster Health: " + str(monster.health))
            print(" Current luck: " + str(user.luck))



    elif roll<user.luck:
        print("sajfs")

def retreat():
    print(":(")
    pass

def after_strike_menu():
    after_strike_items=Menu([
                            MenuItem(1, "Continue", after_strike),
                            MenuItem(2, "Try your Luck", try_luck),
                            MenuItem(3, "Retreat", retreat),
                            MenuItem(4, "Quit", quit_game)])
    after_strike_items.print_menu_items()
    after_strike_item=after_strike_items.select_menu_item()

def strike():
    user.dexterity=user.dexterity+user.get_random()+user.get_random()+12
    monster.dexterity=monster.dexterity+monster.get_random()+monster.get_random()+12
    print(("-*")*30)
    print("Character dexterity: " + str(user.dexterity))
    print("Monster dexterity: " + str(monster.dexterity))
    if monster.dexterity<user.dexterity:
        print("You hit the monster")
        print(("-*")*30)
        global attack
        attack=True
        after_strike_menu()
    elif monster.dexterity>user.dexterity:
        print("The monster hit you")
        print(("-*")*30)
        global attack
        attack=False
        after_strike_menu()
    elif monster.dexterity==user.dexterity:
        print("egyenlo")
        strike()

def begin():
    print(("-*")*30)
    print("Test your Sword in a test fight")
    print(user.begin_character())
    print(monster.monster_status())
    begin_submenu_items=Menu([
                            MenuItem(1, "Strike", strike),
                            MenuItem(2, "Retreat", begin),
                            MenuItem(3, "Quit", quit_game)])
    begin_submenu_items.print_menu_items()
    begin_submenu_item=begin_submenu_items.select_menu_item()

def print_character():
    print(user.get_character())
    print_submenu_items=Menu([
                            MenuItem(1, "Begin", begin),
                            MenuItem(2, "Save", save_game),
                            MenuItem(3, "Quit", quit_game)])
    print_submenu_items.print_menu_items()
    print_submenu_item=print_submenu_items.select_menu_item()

def potion_submenu():
    potion_submenu_items=Menu([
                            MenuItem(1, "Reselect the Potion", select_potion),
                            MenuItem(2, "Continue", print_character),
                            MenuItem(3, "Quit", quit_game)])
    potion_submenu_items.print_menu_items()
    potion_submenu_item=potion_submenu_items.select_menu_item()

def potion_of_dexterity():
    print("Your selected potion is dexterity")
    user.get_inventory("dexterity")
    return potion_submenu()


def potion_of_luck():
    print("Your selected potion is luck")
    user.get_inventory("luck")
    return potion_submenu()

def potion_of_health():
    print("Your selected potion is health")
    user.get_inventory("health")
    return potion_submenu()

def select_potion():
    print(" ")
    print("Select potion:")
    select_potion_items=Menu([
                    MenuItem(1, "Potion of Health", potion_of_health),
                    MenuItem(2, "Potion of Dexterity", potion_of_dexterity),
                    MenuItem(3, "Potion of Luck", potion_of_luck)])
    select_potion_items.print_menu_items()
    select_potion_item=select_potion_items.select_menu_item()

def save_and_quit():
    print("save and qoiut")
    pass

def quit_without_save():
    quit_answer=input('Are you sure (Y or N)? ')
    if quit_answer=='Y' or quit_answer=='y':
        pass
    elif quit_answer=='N' or quit_answer=='n':
        return quit_game()
    else:
        print("Wrong input")
        return quit_without_save()

def resume():
    print("resume")
    pass

def reenter_name():
    sure_reenter=input("Would you like to retipe your character name (Y or N)? ")
    if sure_reenter=="Y" or sure_reenter=="y":
        new_game()
    elif sure_reenter=="N" or sure_reenter=="n":
        roll_stat_game()
    else:
        print("Wrong input")
        reenter_name()

def roll_stat_game():
    user.get_dexterity()
    user.get_luck()
    user.get_health()
    roll_stat_items=Menu([
                    MenuItem(1, "Reroll stats", roll_stat_game),
                    MenuItem(2, "Continue", select_potion),
                    MenuItem(3, "Save", save_game),
                    MenuItem(4, "Quit", quit_game)])
    roll_stat_items.print_menu_items()
    roll_stat_item=roll_stat_items.select_menu_item()

def save_game():
    print("save_game")
    pass

def quit_game():
    quit_items=Menu([
                    MenuItem(1, "Save and Quit", save_and_quit),
                    MenuItem(2, "Quit without save", quit_without_save),
                    MenuItem(3, "Resume", resume)])
    quit_items.print_menu_items()
    quit_item=quit_items.select_menu_item()

def new_game():
    user.name=input('What is your name? ')
    print('Your name is: '+ user.name)
    submenu_items=Menu([
                    MenuItem(1, "Reenter name", reenter_name),
                    MenuItem(2, "Continue", roll_stat_game),
                    MenuItem(3, "Save", save_game),
                    MenuItem(4, "Quit", quit_game)])
    submenu_items.print_menu_items()
    sub_item=submenu_items.select_menu_item()

def load_game():
    print('kaki ez a load game')
    pass

def exit():
    pass

main_items=Menu([
                MenuItem(1, "New game", new_game),
                MenuItem(2, "Load game", load_game),
                MenuItem(3, "Exit", exit)])

main_items.print_menu_items()
item=main_items.select_menu_item()
