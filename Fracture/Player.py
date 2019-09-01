import pygame
import math


class Player:
    def __init__(self, game):
        self.image = pygame.image.load("Media/player/player_default.png")
        self.width, self.height = game.get_image_size(self.image)
        self.x, self.y = self.get_start_location(game)
        self.speed = 7
        self.top_border_width = 2
        self.rect = (self.x-2, self.y, self.width+4, self.height+2)
        self.segments = self.get_player_segments()



    #####################
    #      Getters      #
    #####################
    def get_segment_position(self, sphere):
        segment_position = 1
        for segment in self.player_segments:
            x_start = math.floor(segment[0])
            x_end = math.ceil(segment[1])
            if (sphere.circle_x >= x_start and sphere.circle_x <= x_end):
                break
            segment_position += 1
        return segment_position

    def get_player_segments(self):
    # Player image _______________________________
    #             [_______|_______|_______|_______]
    # Segments        1       2       3       4
        num_segments = 4
        segment_width = self.width / num_segments
        segments = []
        for i in range(num_segments):
            x_start = self.x + segment_width * i
            x_end = x_start + segment_width
            segments.append((x_start, x_end))
        return segments

    def get_start_location(self, game):
        x = game.screen_width / 2 - self.width / 2
        y = game.screen_height - self.height * 5
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
    def player_deflect(self, sphere): # TODO refine x check
    #    # Player image _______________________________
    #    #             [_______|_______|_______|_______]
    #    # Segments        1       2       3       4
        segment_position = self.get_segment_position(sphere)
        index = segment_position - 1
        sphere.angle = sphere.player_deflection_angles[index]
        sphere.radians = math.radians(sphere.angle)
        return

    def player_collision(self, sphere):
        self.player_segments = self.get_player_segments()
        self.player_deflect(sphere)
        sphere.speed_y *= -1
        return

    def player_sphere_collision(self, sphere):
        # Center of circle's x coordinate
        x = sphere.circle_x
        # Bottom of circle
        y = sphere.circle_y + sphere.circle_radius

        if (x >= self.x and x <= self.x + self.width):
            for px in range(sphere.speed_y):
                if (int(y + px) == self.y):
                    self.player_collision(sphere)
        return