import pygame


class Player:
    def __init__(self, game):
        self.image = pygame.image.load("Media/player/player_default.png")
        self.width, self.height = game.get_image_size(self.image)
        self.x, self.y = self.get_start_location(game)
        self.speed = 3

    def get_start_location(self, game):
        x = game.screen_width / 2 - self.width / 2
        y = game.screen_height - self.height * 2
        return x, y

    # Movement
    def move_left(self, game):
        if (self.x - self.speed > 0):
            self.x -= self.speed
        return

    def move_right(self, game):
        if (self.x + self.width + self.speed < game.screen_width):
            self.x += self.speed
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
        # Arrow keys
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):
            self.move_left(game)
        if (keys[pygame.K_RIGHT]):
            self.move_right(game)
        return