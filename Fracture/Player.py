import pygame
import math


class Player:
    def __init__(self, game):
        self.image = pygame.image.load("Media/player/player_default.png")
        self.width, self.height = game.get_image_size(self.image)
        self.x, self.y = self.get_start_location(game)
        self.speed = 5
        self.rect = (self.x-2, self.y, self.width+4, self.height+2)

    def get_start_location(self, game):
        x = game.screen_width / 2 - self.width / 2
        y = game.screen_height - self.height * 10
        return x, y


    #####################
    #      Movement     #
    #####################
    def move_left(self, game):
        if (self.x - self.speed > 0):
            self.x -= self.speed
            self.rect = (self.x-2, self.y, self.width+4, self.height+2)
        return

    def move_right(self, game):
        if (self.x + self.width + self.speed < game.screen_width):
            self.x += self.speed
            self.rect = (self.x-2, self.y, self.width+4, self.height+2)
        return

    def get_input(self, game):
        # Mouse
        if (pygame.mouse.get_pressed()[0]):
            pygame.mouse.set_visible(False)
            mouse_pos = pygame.mouse.get_pos()
            if (mouse_pos[0] < self.x + self.width / 2):
                self.move_left(game)
            if (mouse_pos[0] > self.x + self.width / 2):
                self.move_right(game)
        else:
            pygame.mouse.set_visible(True)
        # Left/Right arrow keys
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):
            self.move_left(game)
        if (keys[pygame.K_RIGHT]):
            self.move_right(game)
        return


    #####################
    #  Player Collision #
    #####################
    def get_player_segments(self):
    # Player image _______________________________
    #             [___|___|___|___|___|___|___|___]
    # Segments      1   2   3   4   5   6   7   8
        num_segments = 8
        segment_width = self.width / num_segments
        segments = []
        for i in range(num_segments):
            x_start = self.x + segment_width * i
            x_end = x_start + segment_width
            segments.append((x_start, x_end))
        return segments

    def sphere_collision(self, sphere):
        x_collision = False
        y_collision = False
        if (sphere.x >= self.x - sphere.width and sphere.x <= self.x + self.width + sphere.width):
            x_collision = True
        sphere_y = sphere.y + sphere.height + sphere.speed
        if (sphere_y >= self.y and sphere_y <= self.y + 3 and sphere.down):
            y_collision = True
        if (x_collision and y_collision):
            return True
        else:
            return False