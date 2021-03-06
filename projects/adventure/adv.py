from room import Room
from player import Player
from world import World
from util import Stack


import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


opposite_dir = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

paths = Stack()
visited = set()

# Comparing visited to length of rooms
while len(visited) < len(world.rooms):
    exits = player.current_room.get_exits()
    path = []

    for exit in exits:
        if exit is not None and player.current_room.get_room_in_direction(
                exit) not in visited:  # if Exit exists and haven't visited room in that direction add to path
            path.append(exit)

    visited.add(player.current_room)  # Add current room to visited set

    if len(path) > 0:  # As long as path exists
        move = random.randint(0, len(path) - 1)
        paths.push(path[move])
        player.travel(path[move])  # Move one of the available paths
        traversal_path.append(path[move])
        print(f'Available moves: {path}, Direction: {path[move]}')

    else:
        move_back = paths.pop()
        player.travel(opposite_dir[move_back])  # move back opposite direction
        traversal_path.append(opposite_dir[move_back])
        print(move_back, "going back")


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######

# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
