import pygame
import math



class Block:
    block_list = []
    def __init__(self, game, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width, self.height = game.get_image_size(image)
        self.hit_left = False
        self.hit_right = False
        self.hit_top = False
        self.hit_bottom = False
        self.fracture = False
        Block.block_list.append(self)

class Level:
    def __init__(self, game):
        self.level = game.level_number
        self.initialize_level_blocks(game)

    def draw_blocks(self, screen):
        for block in Block.block_list:
            screen.blit(block.image, (block.x,block.y))
        return

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


    def moving_down_collision(self, block, sphere):
        x_collision = False
        y_collision = False
        block_top = block.y
        x1 = block.x
        x2 = block.x + block.width      

        # Bottom side of sphere
        y_floor = math.floor(sphere.y + sphere.height)
        # Middle of sphere image x location
        x_mid = int(sphere.x + sphere.width / 2)

        for px in range(sphere.speed):
            if (y_floor + px == block_top):
                y_collision = True

            if (sphere.left):
                if (x_mid - px >= x1 and x_mid - px <= x2):
                    x_collision = True
            elif (sphere.right):
                if (x_mid + px >= x1 and x_mid + px <= x2):
                    x_collision = True

        if (y_collision and x_collision):
            # TODO manage when sphere hits block
            return True
        return False




    def moving_up_collision(self, block, sphere):
        x_collision = False
        y_collision = False
        block_bottom = block.y + block.height
        x1 = block.x
        x2 = block.x + block.width

        # Top side of sphere
        y_ceiling = math.ceil(sphere.y)
        # Middle of sphere image x location
        x_mid = int(sphere.x + sphere.width / 2)

        for px in range(sphere.speed):
            if (y_ceiling - px == block_bottom):
                y_collision = True

            if (sphere.left):
                if (x_mid - px >= x1 and x_mid - px <= x2):
                    x_collision = True
            elif (sphere.right):
                if (x_mid + px >= x1 and x_mid + px <= x2):
                    x_collision = True

        if (y_collision and x_collision):
            # TODO manage when sphere hits block
            return True
        return False

    def moving_right_collision(self, block, sphere):
        x_collision = False
        y_collision = False
        block_left = block.x
        y1 = block.y
        y2 = block.y + block.height

        # Right side of sphere
        x_ceiling = math.ceil(sphere.x + sphere.width)
        # Middle of sphere image y location
        y_mid = int(sphere.y + sphere.height / 2)

        for px in range(sphere.speed):
            if (x_ceiling + px == block_left):
                x_collision = True

            if (sphere.up):
                if (y_mid - px >= y1 and y_mid - px <= y2):
                    y_collision = True
            elif (sphere.down):
                if (y_mid + px >= y1 and y_mid + px <= y2):
                    y_collision = True

        if (y_collision and x_collision):
            # TODO manage when sphere hits block
            return True
        return False

    def moving_left_collision(self, block, sphere):
        x_collision = False
        y_collision = False
        block_right = block.x + block.width
        y1 = block.y
        y2 = block.y + block.height

        # Left side of sphere
        x_floor = math.floor(sphere.x)
        # Middle of shere image y location
        y_mid =int(sphere.y + sphere.height / 2)

        for px in range(sphere.speed):
            if (x_floor - px == block_right):
                x_collision = True

            if (sphere.up):
                if (y_mid - px >= y1 and y_mid - px <= y2):
                    y_collision = True
            elif (sphere.down):
                if (y_mid + px >= y1 and y_mid + px <= y2):
                    y_collision = True

        if (y_collision and x_collision):
            # TODO manage when sphere hits block
            return True
        return False


    def check_block_collision(self, sphere, game):
        for block in Block.block_list:
            if (self.moving_left_collision(block, sphere)):
                block.hit_right = True
                print("hit right")
            if (self.moving_right_collision(block, sphere)):
                block.hit_left = True
                print("hit left")
            if (self.moving_up_collision(block, sphere)):
                block.hit_bottom = True
                print("hit bottom")
            if (self.moving_down_collision(block, sphere)):
                block.hit_top = True
                print("hit top")

        if (block.hit_left == True or
                block.hit_right == True or
                block.hit_bottom == True or
                block.hit_top == True):
            return True
        else:
            return False
