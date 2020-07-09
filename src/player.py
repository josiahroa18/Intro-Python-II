# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.items = []
        self.name = name
        self.current_room = current_room

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item_name):
        for i in range(len(self.items)):
            if self.items[i].name.lower() == item_name:
                return self.items.pop(i)
        return None
    
    def get_inventory(self):
        if len(self.items) == 0:
            return "- There are no items in your inventory\n"
        for i in range(len(self.items)):
            print(f"{i+1}. {self.items[i]}")
        return ""

    def has_treasure(self):
        for item in self.items:
            if item.name.lower() == "treasure":
                return True
        return False

        
