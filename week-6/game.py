import menu

def new_game():
     enter_name=input('What is your name? ')
     return enter_name

def load_game():
    pass

def exit():
    pass

main_items=[{'New game': new_game}, {'Load game': load_game}, {'Exit': exit}]



main_menu=menu.Menu(main_items)
print(main_menu.print_menu_items())
item=main_menu.select_menu_item()

if item==1:
    new=main_menu.items[item-1]
    for key, value in new.items():
        alma=value
        alma()
