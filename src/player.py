# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    # def move_room(self, new_room):
    #     self.current_room = new_room

    def travel(self, direction):
        # Player should travel in new direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('You cannot move in that direction')
