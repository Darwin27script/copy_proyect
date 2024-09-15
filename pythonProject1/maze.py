import os
import random
import readchar

# constantes
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_MAP_OBJECTS = 10

# variables y listas
my_position = [0, 0]
tail_length = 0
tail = []
map_objects = []
end_game = False



# Bucle pricipal
while not end_game:
    os.system("cls")
    # Agregar objetos
    while len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # MAPA
    print("\t\t\t¡¡¡SNAKE!!!")
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            dies = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "#"
                    dies = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    # remueve el objeto:
                    map_objects.remove(object_in_cell)

                    # agranda cola:
                    tail_length += 1

                if my_position == dies:
                    end_game = True


            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Movimiento
    direction = readchar.readchar()

    if direction.upper() == "W":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction.upper() == "S":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction.upper() == "A":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH

    elif direction.upper() == "D":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH

    elif direction.upper() == "Q":
        end_game = True

print("GAME OVER")