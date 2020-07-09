# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    n_to = None
    e_to = None
    s_to = None
    w_to = None

    def __init__(self, room_name, room_description):
        self.items = []
        self.room_name = room_name
        self.room_description = room_description

    def __str__(self):
        return f"{self.room_name} - {self.room_description}"

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        if len(self.items) == 0:
            return "- There are no items in this room\n"
        for i in range(len(self.items)):
            print(f"{i + 1}. {self.items[i]}")
        return ""

    def get_item_by_name(self, item_name):
        for item in self.items:
            if(item.name.lower() == item_name):
                return item
        return None
    
    def remove_item_by_name(self, item_name):
        for i in range(len(self.items)):
            if(self.items[i].name.lower() == item_name):
                return self.items.pop(i)
        return None

    def name(self):
        return self.room_name



        