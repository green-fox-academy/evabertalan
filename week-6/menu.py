class Menu():
    def __init__(self, items):
        self.items=items

    def print_menu_items(self):
        return '\n'.join(list(map(lambda u: u['name'], self.items)))

    def select_menu_item(self):
        selected_item=int(input('Select menu item: '))
        try:
            if not selected_item or selected_item > len(self.items):
                raise ValueError
        except ValueError:
            print('You entered a wrong value.')
            self.select_menu_item()
        return(self.items[selected_item-1]['function']())
