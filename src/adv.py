from room import Room
from player import Player

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
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south."""),
    }

    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

    player = Player("Josiah", room['outside'])

    is_playing = True    
    while(is_playing):
        print("\nCurrent Room:", player.current_room, "\n")
        user_input = input("Which direction would you like to go? (N, E, S, W, Q to quit): ")
        user_input = user_input.lower()
        if user_input == "q":
            is_playing = False
            print("\nGoodbye!")
        elif user_input not in ('n', 'e', 's', 'w'):
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
