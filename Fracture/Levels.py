import pygame
import math


#####################
#    Block Class    #
#####################
class Block:
    block_list = []
    def __init__(self, game, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width, self.height = game.get_image_size(image)
        self.top_left = (self.x, self.y)
        self.top_right = (self.x + self.width, self.y)
        self.bot_left = (self.x, self.y + self.height)
        self.bot_right = (self.x + self.width, self.y + self.height)
        self.corners = [self.top_left, self.top_right, self.bot_left, self.bot_right]
        self.hit_left = False
        self.hit_right = False
        self.hit_top = False
        self.hit_bottom = False
        self.fracture = False
        Block.block_list.append(self)

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))
        return

    # coords = [top, bottom, left, right, topright, bottomright, bottomleft, topleft]
    def set_block_hit_side(self, coord_index, sphere):
        if (coord_index == 0 or coord_index == 1):
            sphere.speed_y *= -1
        elif (coord_index == 2 or coord_index == 3):
            sphere.speed_x *= -1
        else:
            sphere.speed_x *= -1
            sphere.speed_y *= -1
        return

    def sphere_collision(self, sphere):
        sphere.collision_coordinates = sphere.get_collision_coordinates()
        coord_index = 0
        for coord in sphere.collision_coordinates:
            if (coord[0] >= self.x and coord[0] <= self.x + self.width):
                if (coord[1] >= self.y and coord[1] <= self.y + self.height):
                    self.set_block_hit_side(coord_index, sphere)
                    return True
            coord_index += 1
        return False


#####################
#    Level Class    #
#####################
class Level:
    def __init__(self, game):
        self.level = game.level_number
        self.initialize_level_blocks(game)

    def initialize_level_blocks(self, game):
        if (self.level == 1):
            initialize_level_1_blocks(game)
        #elif (self.level == 2):
        #    return self.get_level_2_blocks(game)
        # etc....
        return

    @staticmethod
    def draw_blocks(screen):
        for block in Block.block_list:
            block.draw(screen)
        return

    #####################
    #  Collision Checks #
    #####################
    def block_collision(self, sphere, game):
        for block in Block.block_list:
            if (block.sphere_collision(sphere)):
                Block.block_list.remove(block)
                return True
        return False

    @staticmethod
    def sphere_edge_collision(game, sphere):
        x = sphere.circle_x
        y = sphere.circle_y
        radius = sphere.circle_radius
        if (x < radius or x > game.screen_width - radius):
            sphere.speed_x *= -1
        if (y < radius):
            sphere.speed_y *= -1
        if (y > game.screen_height - radius):
            return True
        return False


#####################
#       Levels      #
#####################

def initialize_level_1_blocks(game):
    image = game.blue_block
    size = image.get_size()
    left_x = 0 + size[0]
    right_x = game.screen_width - size[0] * 3
    y = 0 + size[1] * 3
    positions = (
        # L
        (left_x, y), 
        (left_x, y + size[1]),
        (left_x, y + size[1] * 2), 
        (left_x, y + size[1] * 3), 
        (left_x, y + size[1] * 4), 
        (left_x, y + size[1] * 5), 
        (left_x, y + size[1] * 6), 
        (left_x + size[0], y + size[1] * 5),
        (left_x + size[0], y + size[1] * 6),


        # O
        (left_x + size[0] * 3, y),
        (left_x + size[0] * 3, y + size[1]),
        (left_x + size[0] * 3, y + size[1] * 2),
        (left_x + size[0] * 3, y + size[1] * 3),
        (left_x + size[0] * 3, y + size[1] * 4),
        (left_x + size[0] * 3, y + size[1] * 5),
        (left_x + size[0] * 3, y + size[1] * 6),
        (left_x + size[0] * 4, y),
        (left_x + size[0] * 4, y + size[1]),
        (left_x + size[0] * 4, y),
        (left_x + size[0] * 4, y + size[1] * 5),
        (left_x + size[0] * 4, y + size[1] * 6),
        (left_x + size[0] * 5, y),
        (left_x + size[0] * 5, y + size[1]),
        (left_x + size[0] * 5, y + size[1] * 2),
        (left_x + size[0] * 5, y + size[1] * 3),
        (left_x + size[0] * 5, y + size[1] * 4),
        (left_x + size[0] * 5, y + size[1] * 5),
        (left_x + size[0] * 5, y + size[1] * 6),

        # L
        (right_x, y),
        (right_x, y + size[1]), 
        (right_x, y + size[1] * 2), 
        (right_x, y + size[1] * 3), 
        (right_x, y + size[1] * 4), 
        (right_x, y + size[1] * 5), 
        (right_x, y + size[1] * 6), 
        (right_x + size[0], y + size[1] * 5),
        (right_x + size[0], y + size[1] * 6),
    )
    for pos in positions:
        Block(game, image, pos[0], pos[1])
    return