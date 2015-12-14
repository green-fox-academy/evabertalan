class Menu():
    def __init__(self, items):
        self.items=items

    def print_menu_items(self):
        output = ""
        for i,j in enumerate(self.items):
            for key, value in j.items():
                output += str(i+1) + ". " + key + "\n"
        return output

    def select_menu_item(self):
        selected_item=int(input('Select menu item: '))
        try:
            if not selected_item or selected_item > len(self.items):
                raise ValueError
        except ValueError:
            print('You entered a wrong value.')
            self.select_menu_item()
        return selected_item
