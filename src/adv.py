from room import Room
from player import Player
from item import Item

def handle_quit(user_input):
    # Return False to quit, True to continue
    if user_input.lower() == 'q':
        print("\nGoodbye!")
        return False
    return True

def main():
    room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! The only exit is to the south."""),
    }

    # Connect rooms
    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

    # Assign items to room
    room['outside'].add_item(Item("Sword", "A powerful weapon used to defend yourself"))
    room['outside'].add_item(Item("Shield", "A great way to defend yourself"))
    room['treasure'].add_item(Item("Treasure", "The treasure you've been looking for"))
    room['foyer'].add_item(Item("Coins", "Some old rusty coins"))
    room['narrow'].add_item(Item("Cloth", "Useless cloth"))

    player = Player("Josiah", room['outside'])

    is_playing = True    
    print("Welcome to treasure hunter! To win, bring the treasure back to the South entrance!")
    while(is_playing):
        if player.current_room.name() == "Outside Cave Entrance" and player.has_treasure():
            is_playing = False
            print("You won the game!")
            break
        print("\nCurrent Room:", player.current_room)

        is_deciding = True
        while(is_deciding):
            print("*** Current items in room:")
            print(player.current_room.get_items())
            user_input = input("*** Would you like to do anything with your items? (take <item_name>, drop <item_name>, v to view Inventory, C to Continue, Q to Quit): ")
            is_playing = handle_quit(user_input)
            if not is_playing:
                break
            user_input = user_input.split(" ")
            if user_input[0].lower() == "drop":
                item = player.drop_item(user_input[1])
                if item:
                    player.current_room.add_item(item)
                    print(f"Item {user_input[1]} has been dropped on the ground")
                else:
                    print("That item does not exist in your inventory")
            elif user_input[0].lower() == "take":
                if player.current_room.get_item_by_name(user_input[1].lower()):
                    player.add_item(player.current_room.get_item_by_name(user_input[1].lower()))
                    print(f"Item {user_input[1]} has been added to your inventory")
                    player.current_room.remove_item_by_name(user_input[1].lower())
                else:
                    print("That item does not exist in this room")
            elif user_input[0].lower() == "c":
                is_deciding = False
            elif user_input[0].lower() == "v":
                print("*** Player inventory: ")
                print(player.get_inventory())
        
        # Check to see if the player has quit the game from previous loop
        if not is_playing:
            break
            
        user_input = input("Which direction would you like to go? (N, E, S, W, Q to Quit): ")
        user_input = user_input.lower()
        is_playing = handle_quit(user_input)
        if user_input not in ('n', 'e', 's', 'w', 'q'):
            print("\nI'm not sure which direction that is\n")
        else:
            if user_input == 'n':
                if player.current_room.n_to != None:
                    player.current_room = player.current_room.n_to
                else:
                    print("\nThere is no room in that direction, please try again.")
            if user_input == 'e':
                if player.current_room.e_to != None:
                    player.current_room = player.current_room.e_to
                else:
                    print("\nThere is no room in that direction, please try again.")
            if user_input == 's':
                if player.current_room.s_to != None:
                    player.current_room = player.current_room.s_to
                else:
                    print("\nThere is no room in that direction, please try again.")
            if user_input == 'w':
                if player.current_room.w_to != None:
                    player.current_room = player.current_room.w_to
                else:
                    print("\nThere is no room in that direction, please try again.")
            
if __name__ == "__main__":
    main()
