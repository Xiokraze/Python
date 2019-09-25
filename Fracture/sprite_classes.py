import math
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


class Player(pygame.sprite.Sprite):
    # Player sprite
    def __init__(self, screen_obj):
        super().__init__()
        self.image = pygame.image.load("Media/player/player_default.png")
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.x = screen_obj.screen_width / 2 - self.size[1] / 2
        self.rect.y = screen_obj.screen_height - self.size[1] * 2
        self.speed = 7
        self.x_min = screen_obj.x_min
        self.x_max = screen_obj.x_max
        self.border_padding = screen_obj.border_width

    def get_segments(self, sphere):
        # Creates and returns a list of 4 segments by dividing the player
        # sprite's width by 4. Adds half the sphere image to the end of each
        # side for more realistic and accurate looking deflections.
        segments = []
        segment_width = self.size[0] / 4
        sphere_offset = sphere.size[0] / 2
        player_x = self.rect.x
        # Add the start and end x-axis px location for each segment to the list
        for i in range(4):
            if i == 0:  # Left segment of the player
                x_start = player_x - sphere_offset
                x_end = player_x + segment_width
            elif i == 3:  # Right segment of the player
                x_start = player_x
                x_end = x_start + segment_width + sphere_offset
            else:  # Middle two segments of the player
                x_start = player_x
                x_end = x_start + segment_width
            segments.append((x_start, x_end))
            player_x += segment_width
        return segments

    def move_left(self):
        # Handles moving the player to the left
        x = self.rect.x - self.speed - self.border_padding
        if x > self.x_min:
            self.rect.x -= self.speed
        return

    def move_right(self):
        # Handles moving the player to the right
        x = self.rect.x + self.size[0] + self.speed + self.border_padding
        if x < self.x_max:
            self.rect.x += self.speed
        return

    def update(self):
        # Overrides pygame's sprite.update function and handles player movement
        # Mouse
        if pygame.mouse.get_pressed()[0]:
            pygame.mouse.set_visible(False)
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] < self.rect.x + self.size[0] / 2:
                self.move_left()
            if mouse_pos[0] > self.rect.x + self.size[0] / 2:
                self.move_right()
        # Left/Right arrow keys
        else:
            pygame.mouse.set_visible(True)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.move_left()
            if keys[pygame.K_RIGHT]:
                self.move_right()
        return


class Sphere(pygame.sprite.Sprite):
    def __init__(self, screen_obj):
        super().__init__()
        self.images = [
            pygame.image.load("Media/spheres/dark_blue.png")
            ]
        self.image = self.images[0]
        self.speed = 5
        self.speed_x = self.speed
        self.speed_y = self.speed * -1
        self.angle = 45
        self.player_angles = [300, 340, 20, 60]
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.x = screen_obj.screen_width / 2 - self.size[0] / 2
        self.rect.y = screen_obj.screen_height - self.size[1] * 10
        self.x_min = screen_obj.x_min + screen_obj.border_width
        self.x_max = screen_obj.screen_width - screen_obj.x_max - self.size[0]
        self.y_max = screen_obj.top_padding + screen_obj.border_width + self.size[1]
        self.px_locations = ("left", "right", "top", "bot", "top_left",
                             "top_right", "bot_left", "bot_right")

    def get_px_positions(self):
        # Creates and returns a list of the 8 pixels on the rectangle
        # surrounding the sphere: the 4 corners and the central point
        # on each side. The list will always be in the following order:
        # left, right, top, bot, top_left, top_right, bot_left, bot_right
        px_positions = [
            (self.rect.x, self.rect.y + self.size[1] / 2),
            (self.rect.x + self.size[0], self.rect.y + self.size[1] / 2),
            (self.rect.x + self.size[0] / 2, self.rect.y + self.size[1]),
            (self.rect.x + self.size[0] / 2, self.rect.y),
            (self.rect.x, self.rect.y),
            (self.rect.x + self.size[0], self.rect.y),
            (self.rect.x, self.rect.y + self.size[1]),
            (self.rect.x + self.size[0], self.rect.y + self.size[1])
        ]
        return px_positions

    def get_block_side_collision(self, block):
        # Returns the string representation of which of the sphere's 8 pixels
        # collided with the block. This is determined by comparing each pixel's
        # location against the coordinates of the block's sides and finding
        # which one lies within the block's boundaries.
        #
        # Loop through each of the (x,y) coords of the sphere's rect pixels and
        # check the x against the block's left and right sides, then y against
        # the top and bottom. If both are true, it lies within the block. The
        # sides are always in the following order: left, right, top, bottom.
        block_sides = block.get_sides()
        index = 0
        for position in self.get_px_positions():
            if block_sides[0] <= position[0] <= block_sides[1]:
                if block_sides[2] <= position[1] <= block_sides[3]:
                    break
            index += 1
        return self.px_locations[index]

    def set_block_deflection_angle(self, block):
        # Calculates the sphere's new angle based on the side of the block hit.
        block_side = self.get_block_side_collision(block)
        if block_side == "left" or block_side == "right":
            self.angle = 360 - self.angle
        elif block_side == "top" or block_side == "bot":
            self.angle = (180 - self.angle) % 360
        else:
            angle = self.angle - 360
            if angle < 0:
                angle = 360 - angle
            self.angle = angle
        return

    def set_border_deflection_angle(self, border):
        # Calculates the sphere's new angle based on the border hit.
        if border.side == "left":
            self.angle = 360 - self.angle
        if border.side == "right":
            self.angle = 360 - self.angle
        if border.side == "top":
            self.angle = (180 - self.angle) % 360

        # Place holder for sphere/bottom border collision handling
        if border.side == "bot":
            pass
        return

    def set_player_deflection_angle(self, player_segments):
        # Calculates the sphere's new angle based on the player segment hit.
        # Sphere's bottom center x pixel coord
        sphere_x = self.rect.x + self.size[0] / 2
        segment_num = 0
        for start, end in player_segments:
            if start <= sphere_x <= end:
                break
            segment_num += 1
        # Ensure the segment number is not greater than the angles list length
        if segment_num < len(self.player_angles):
            self.angle = self.player_angles[segment_num]
        # If, for some reason, it is, then reverse the angle of the sphere
        else:
            self.angle = 360 - self.angle
        return

    def move(self):
        # Moves the sphere by converting the angle into radians and then using
        # sin and cos to calculate the x/y speeds, or number of pixels to move.
        radians = math.radians(self.angle)
        self.rect.y += int(self.speed_y * math.cos(radians))
        self.rect.x += int(self.speed_x * math.sin(radians))
        return

    def update(self, game):
        # Overrides pygame's sprite.update function and updates the sphere.
        # Checks for border, player, and block collisions, then handles movement.
        game.border_collision()
        game.player_collision()
        game.block_collision()
        self.move()
        return
