import menu
import random
from character import Character

user_name=''


def character():
    player=Character(user_name,4,5,6,3)
    print(player.get_character())

def potion_submenu():
    potion_submenu_items=[{'name':'1. Reselect the Potion', 'function': select_potion},
                        {'name':'2. Continue', 'function': character},
                        {'name':'3. Quit', 'function': quit_game}]
    potion_sub=menu.Menu(potion_submenu_items)
    print(potion_sub.print_menu_items())
    potion_submenu_item=potion_sub.select_menu_item()

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
    select_potion_items=[{'name':'1. Potion of Health', 'function': potion_of_health},
                        {'name':'2. Potion of Dexterity', 'function': potion_of_dexterity},
                        {'name':'3. Potion of Luck', 'function': potion_of_luck}]
    potion=menu.Menu(select_potion_items)
    print(potion.print_menu_items())
    select_potion_item=potion.select_menu_item()

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
    print("reenter_name")
    pass

def roll_stat_game():
    dexterity=random.randint(1, 6)
    health=random.randint(1, 12)
    luck=random.randint(1, 6)
    print("Your dexterity points are: " + str(dexterity) +" + 6 = " + str(dexterity+6))
    print("Your health points are: "+ str(health) +" + 12 = " + str(health+12))
    print("Your health points are: "+ str(luck) +" + 6 = " + str(luck+6))
    roll_stat_items=[{'name':'1. Reroll stats', 'function': roll_stat_game},
                        {'name':'2. Continue', 'function': select_potion},
                        {'name':'3. Save', 'function': save_game},
                        {'name':'4. Quit', 'function': quit_game}]
    roll_stat=menu.Menu(roll_stat_items)
    print(roll_stat.print_menu_items())
    roll_stat_item=roll_stat.select_menu_item()

def save_game():
    print("save_game")
    pass

def quit_game():
    quit_items=[{'name':'1. Save and Quit', 'function': save_and_quit},
                {'name':'2. Quit without save', 'function': quit_without_save},
                {'name':'3. Resume', 'function': resume}]
    quit=menu.Menu(quit_items)
    print(quit.print_menu_items())
    quit_item=quit.select_menu_item()


def new_game():
    global user_name
    user_name=input('What is your name? ')
    print('Your name is: '+ user_name)
    submenu_items=[{'name':'1. Reenter name', 'function': reenter_name},
                    {'name':'2. Continue', 'function': roll_stat_game},
                    {'name':'3. Save', 'function': save_game},
                    {'name':'4. Quit', 'function': quit_game},]
    submenu=menu.Menu(submenu_items)
    print(submenu.print_menu_items())
    sub_item=submenu.select_menu_item()

def load_game():
    print('kaki')
    pass

def exit():
    pass

main_items=[{'name':'1. New game', 'function': new_game},
            {'name':'2. Load game', 'function': load_game},
            {'name':'3. Exit', 'function':exit}]

main_menu=menu.Menu(main_items)
print(main_menu.print_menu_items())
item=main_menu.select_menu_item()
