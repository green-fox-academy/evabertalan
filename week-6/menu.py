class Menu():
    def __init__(self, items):
        self.items=items

    def print_menu_items(self):
        for i in self.items:
            print(str(i.num)+". "+str(i.name))

    def choose(self, selected_item):
        for i in self.items:
            if selected_item==i.num:
                i.action()

    def select_menu_item(self):
        selected_item=int(input('Select menu item: '))
        self.choose(selected_item)
        try:
            if not selected_item or selected_item > len(self.items):
                raise ValueError
        except ValueError:
            print('You entered a wrong value.')
            self.select_menu_item()
