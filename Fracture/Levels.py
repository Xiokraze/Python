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


#####################
#    Level Class    #
#####################
class Level:
    def __init__(self, game):
        self.level = game.level_number
        self.initialize_level_blocks(game)

    def draw_blocks(self, screen):
        for block in Block.block_list:
            screen.blit(block.image, (block.x,block.y))
        return



    #####################
    #     Collision     #
    #####################
    def sphere_block_collision(self, block, sphere):
        sphere.collision_coordinates = sphere.get_collision_coordinates()




        return
    #def check_corners(self, block, sphere):
    #    for corner in block.corners:
    #        bx = corner[0]
    #        cx = sphere.circle_x
    #        by = corner[1]
    #        cy = sphere.circle_y
    #        distance = math.hypot(bx-cx, by-cy)
    #        if (distance < sphere.width / 2):
    #            return True
    #    return False

    def check_block_collision(self, sphere, game):
        for block in Block.block_list:
            if (self.sphere_block_collision(block, sphere)):
                print("block side collision")
                return True
        return False















    def initialize_level_blocks(self, game):
        if (self.level == 1):
            self.initialize_level_1_blocks(game)
        #elif (self.level == 2):
        #    return self.get_level_2_blocks(game)
        # etc....
        return

    def initialize_level_1_blocks(self, game):
        image = game.blue_block
        positions = ((100, 100), (300,300), (700, 100))       
        for pos in positions:
            Block(game, image, pos[0], pos[1])
        return

        return False
