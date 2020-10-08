class Room:
    """
    Defines attributes for rooms
    """
    def __init__(self, , north, east, south, west):
        """Sets up variables for rooms """
        self.description = ""
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0

def main():
    # Empty list
    room_list = []

    # New variable room set equal to new instance of Room class
    room = Room
    # description of room
    """
    NEED to put description here; step 7
    """
    # adds the newly created room to room_list
    room_list.append(room)
    """
    Repeat creating new rooms for the rest of the rooms; use the room varible
    """
    # new variable
    current_room = 0
    # prints a list of every room object in adventure, may look a little strange inside <>
    print(room_list)


# calls main function
main()

