import pygame
import sprite_classes


class Level(object):
    # Handles parameters for creating levels
    def __init__(self, level, screen_obj):
        self.level = level
        self.backgrounds = [
            pygame.image.load("Media/backgrounds/space1.png")
        ]
        self.background = self.get_background()
        self.blocks = self.get_blocks(screen_obj)

    def get_blocks(self, screen_obj):
        # Returns a list of blocks of the corresponding level
        blocks = []
        for block in Levels.get_positions(self.level, screen_obj):
            blocks.append(block)
        return blocks

    def get_background(self):
        # Returns background image assigned to each level
        background = None
        if self.level == 1:
            background = self.backgrounds[0]  # Space bg
        return background

    def set_blocks(self, screen_obj):
        # Loads blocks when the current level changes
        self.blocks = self.get_blocks(screen_obj)
        return

    def set_background(self):
        # Sets background image
        self.background = self.get_background()
        return

    def set_level(self, level):
        # Updates the game's current level
        self.level = level
        return

    def check_level(self, level_num):
        # Checks if player has advanced to another level
        if level_num != self.level:
            return True
        return False


class Levels:
    # Class for simplifying level handling for blocks

    # Block Media
    blue = pygame.image.load("Media/blocks/blue_01.png")
    block_size = blue.get_size()

    @staticmethod
    def get_positions(level, screen_obj):
        max_blocks_row = 10
        max_blocks_col = 10
        x_min = screen_obj.x_min + screen_obj.border_width
        y_min = screen_obj.top_padding + screen_obj.border_width
        blocks = []

        if level == 1:
            x = x_min
            y = y_min
            health = 1
            for i in range(max_blocks_row):
                if i == 9:
                    for j in range(max_blocks_col):
                        if j == 8:
                            blocks.append((Levels.blue, x, y, health))
                        x += Levels.block_size[0]
                    x = x_min
                y += Levels.block_size[1]

        elif level == 2:
            x = x_min
            y = y_min
            health = 1
            for i in range(max_blocks_row):
                if i == 2 or i == 5:
                    for j in range(max_blocks_col):
                        if j % 2 == 0:
                            blocks.append((Levels.blue, x, y, health))
                        x += Levels.block_size[0]
                    x = x_min
                y += Levels.block_size[1]

        return blocks
