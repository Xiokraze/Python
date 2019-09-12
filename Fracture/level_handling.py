import pygame


class Block(pygame.sprite.Sprite):
    # Side lists are in order: Left Right Top Bot
    def __init__(self, block):
        super().__init__()
        self.image = block[0]
        self.rect = self.image.get_rect()
        self.rect.x = block[1]
        self.rect.y = block[2]
        self.size = self.image.get_size()
        self.sides = self.get_sides()

    def get_sides(self):
        left = self.rect.x
        right = self.rect.x + self.size[0]
        top = self.rect.y
        bot = self.rect.y + self.size[1]
        sides = [left, right, top, bot]
        return sides


class Border(pygame.sprite.Sprite):
    def __init__(self, screen_obj, border_position):
        super().__init__()
        self.side = border_position
        self.thickness = screen_obj.border_width
        self.side_height = screen_obj.screen_height - screen_obj.top_padding
        self.top_width = self.get_top_width(screen_obj)
        self.color = (0, 0, 255)
        self.image = self.get_image()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.get_rect_x(screen_obj)
        self.rect.y = self.get_rect_y(screen_obj)

    def get_rect_x(self, screen_obj):
        if self.side == "left":
            return screen_obj.x_min
        elif self.side == "right":
            return screen_obj.screen_width - screen_obj.x_min - self.thickness
        else:
            return screen_obj.x_min + self.thickness

    def get_rect_y(self, screen_obj):
        if self.side == "left" or self.side == "right" or self.side == "top":
            return screen_obj.top_padding
        else:
            return screen_obj.screen_height

    def get_image(self):
        if self.side == "left" or self.side == "right":
            return pygame.Surface([self.thickness, self.side_height])
        else:
            return pygame.Surface([self.top_width, self.thickness])

    def get_top_width(self, screen_obj):
        screen_width = screen_obj.screen_width
        width = screen_width - screen_obj.x_min * 2 - self.thickness * 2
        return width


class Level(object):
    def __init__(self, level):
        self.level = level
        self.backgrounds = [
            pygame.image.load("Media/backgrounds/space1.png")
        ]
        self.background = self.get_background()
        self.blocks = self.get_blocks()

    def get_blocks(self):
        blocks = []
        for block in Levels.get_positions(self.level):
            blocks.append(block)
        return blocks

    # Fetches background assigned to each level
    def get_background(self):
        background = None
        if self.level == 1:
            background = self.backgrounds[0]  # Space bg
        return background

    # Reload blocks when the current level changes
    def set_blocks(self):
        self.blocks = self.get_blocks()
        return

    # Reload background if current level changes
    def set_background(self):
        self.background = self.get_background()
        return

    # Called to change the current game level
    def set_level(self, level):
        self.level = level
        return

    # Checks if player has advanced to another level
    def check_level(self, level_num):
        if level_num != self.level:
            return True
        return False


class Levels:
    # Class for simplifying level handling for blocks
    @staticmethod
    def get_positions(level):
        blue = pygame.image.load("Media/blocks/blue_01.png")
        blocks = ()
        if level == 1:
            blocks = (
                (blue, 300, 400),
                (blue, 400, 400),
                (blue, 600, 400),
                (blue, 500, 600),
                (blue, 100, 400),
            )
        return blocks
