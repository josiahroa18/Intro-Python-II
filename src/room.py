# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    n_to = None
    e_to = None
    s_to = None
    w_to = None

    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description

    def __str__(self):
        return f"{self.room_name} - {self.room_description}"


        