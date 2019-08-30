import pygame


class Blocks:
    def __init__(self, game):
        self.blue_block = pygame.image.load("Media/blocks/blue_01.png")
        self.width, self.height = game.get_image_size(self.blue_block)

class Level:
    def __init__(self, game):
        self.level = game.level_number
        self.block_images = Blocks(game)
        self.blocks = self.get_blocks()
    
    def get_blocks(self):
        if (self.level == 1):
            return self.get_level_1_blocks()
        return

    def get_level_1_blocks(self):
        blocks = []
        blue = self.block_images.blue_block
        blue_positions = ((100, 100), (300,300), (700, 100))       
        for pos in blue_positions:
            blocks.append((blue, pos))
        return blocks
