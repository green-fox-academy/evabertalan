import menu

def new_game():
     enter_name=input('What is your name? ')
     return enter_name
     pass

def load_game():
    print('kaki')
    pass

def exit():
    print("ebola")
    pass

main_items=[{'name':'1. New game', 'function': new_game},
            {'name':'2. Load game', 'function': load_game},
            {'name':'3. Exit', 'function':exit}]

main_menu=menu.Menu(main_items)
print(main_menu.print_menu_items())
item=main_menu.select_menu_item()
