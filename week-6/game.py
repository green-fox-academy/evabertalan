from menu import Menu
import random
from character import Character
from menu_item import MenuItem

user_name=''

def user_character():
    player=Character(user_name,4,5,6,3)
    print(player.get_character())

def potion_submenu():
    potion_submenu_items=Menu([
                            MenuItem(1, "Reselect the Potion", select_potion),
                            MenuItem(2, "Continue", user_character),
                            MenuItem(3, "Quit", quit_game)])
    potion_submenu_items.print_menu_items()
    potion_submenu_item=potion_submenu_items.select_menu_item()

def potion_of_dexterity():
    print("Your selected potion is dexterity")
    return potion_submenu()


def potion_of_luck():
    print("Your selected potion is luck")
    return potion_submenu()

def potion_of_health():
    print("Your selected potion is health")
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
    dexterity=random.randint(1, 6)
    health=random.randint(1, 12)
    luck=random.randint(1, 6)
    print("Your dexterity points are: " + str(dexterity) +" + 6 = " + str(dexterity+6))
    print("Your health points are: "+ str(health) +" + 12 = " + str(health+12))
    print("Your health points are: "+ str(luck) +" + 6 = " + str(luck+6))
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
    global user_name
    user_name=input('What is your name? ')
    print('Your name is: '+ user_name)
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
