import pygame


class Block(pygame.sprite.Sprite):
    # Sprite class for blocks
    def __init__(self, block):
        super().__init__()
        self.image = block[0]
        self.rect = self.image.get_rect()
        self.rect.x = block[1]
        self.rect.y = block[2]
        self.size = self.image.get_size()
        self.sides = self.get_sides()
        self.health = block[3]

    def get_sides(self):
        # Returns a list of the x and y coordinates for the 4 sides. The order
        # is always left, right, top, bottom.
        sides = [
            self.rect.x,
            self.rect.x + self.size[0],
            self.rect.y,
            self.rect.y + self.size[1]
        ]
        return sides


class Border(pygame.sprite.Sprite):
    # Sprite class for borders
    # Border Media
    border_left = pygame.image.load("Media/borders/gray/graphite_left.png")
    border_right = pygame.image.load("Media/borders/gray/graphite_right.png")
    border_top = pygame.image.load("Media/borders/gray/graphite_top.png")
    corner_left = pygame.image.load("Media/borders/gray/graphite_top_left.png")
    corner_right = pygame.image.load("Media/borders/gray/graphite_top_right.png")

    def __init__(self, screen_obj, border_position):
        super().__init__()
        self.side = border_position
        self.thickness = screen_obj.border_width
        self.side_height = screen_obj.screen_height - screen_obj.top_padding
        self.top_width = self.get_top_width(screen_obj)
        self.color = (0, 0, 255)
        self.image = self.get_image()
        # self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.get_rect_x(screen_obj)
        self.rect.y = self.get_rect_y(screen_obj)

    def draw_top(self, screen_obj):
        # Draws the top border sprites
        image = Border.border_top
        size = image.get_size()
        x = self.rect.x + size[0] / 2
        y = self.rect.y
        while True:
            screen_obj.screen.blit(image, (x, y))
            x += size[0]
            if x > screen_obj.x_max - size[0]:
                break
        return

    def draw_corners(self, screen_obj):
        # Draws the top left and top right corner sprites
        left_corner = Border.corner_left
        right_corner = Border.corner_right
        size = left_corner.get_size()
        # Draw left corner
        x = self.rect.x - size[0] / 2
        y = self.rect.y
        screen_obj.screen.blit(left_corner, (x, y))
        # Draw right corner
        x = screen_obj.x_max - size[0]
        screen_obj.screen.blit(right_corner, (x, y))
        return

    def draw(self, screen_obj):
        # Draws the left and right border sprites
        if self.side == "left" or self.side == "right":

            # Get the left or right image
            if self.side == "left":
                image = Border.border_left
            else:
                image = Border.border_right
            size = image.get_size()

            # Get the left or right x coordinate
            if self.side == "left":
                x = self.rect.x
            else:
                x = self.rect.x - size[0] / 2
            y = self.rect.y + size[1]
            self.draw_sides(image, x, y, size, screen_obj)
        # Draws the top border sprites
        elif self.side == "top":
            self.draw_corners(screen_obj)
            self.draw_top(screen_obj)
        return

    @staticmethod
    def draw_sides(image, x, y, size, screen_obj):
        # Draws the side border sprite images
        while True:
            screen_obj.screen.blit(image, (x, y))
            y += size[1]
            if y > screen_obj.screen_height:
                break
        return

    def get_rect_x(self, screen_obj):
        # Returns starting x-axis coordinate for the corresponding side
        if self.side == "left":
            return screen_obj.x_min
        elif self.side == "right":
            return screen_obj.screen_width - screen_obj.x_min - self.thickness
        else:
            return screen_obj.x_min + self.thickness

    def get_rect_y(self, screen_obj):
        # Returns starting x-axis coordinate for the corresponding side
        if self.side == "left" or self.side == "right" or self.side == "top":
            return screen_obj.top_padding
        else:
            return screen_obj.screen_height

    def get_image(self):
        # Returns pygame surface for the corresponding side
        if self.side == "left" or self.side == "right":
            return pygame.Surface([self.thickness, self.side_height])
        else:
            return pygame.Surface([self.top_width, self.thickness])

    def get_top_width(self, screen_obj):
        # Returns the gap size between the top of the screen and the top border
        screen_width = screen_obj.screen_width
        width = screen_width - screen_obj.x_min * 2 - self.thickness * 2
        return width


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
