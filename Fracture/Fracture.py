import math
import sys
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


class Border(pygame.sprite.Sprite):  # TODO refactor
    def __init__(self, screen_obj, border_position):
        super().__init__()
        self.side = border_position
        top_padding = 200
        side_padding = 50
        side_height = screen_obj.screen_height - top_padding
        self.border_width = 20
        border_width = self.border_width
        border_color = (0, 0, 255)

        if self.side == "left" or self.side == "right":
            self.image = pygame.Surface([border_width, side_height])
            self.image.fill(border_color)
            self.rect = self.image.get_rect()
            if self.side == "left":
                self.rect.x = side_padding
            else:
                self.rect.x = screen_obj.screen_width - border_width - side_padding
            self.rect.y = top_padding
        else:
            width = screen_obj.screen_width - side_padding * 2 - self.border_width * 2
            self.image = pygame.Surface([width, border_width])
            self.image.fill(border_color)
            self.rect = self.image.get_rect()
            self.rect.x = 0 + side_padding + self.border_width
            self.rect.y = top_padding


class Sphere(pygame.sprite.Sprite):
    def __init__(self, screen_obj):
        super().__init__()
        self.image = pygame.image.load("Media/spheres/dark_blue.png")
        self.speed = 5
        self.speed_x = self.speed
        self.speed_y = self.speed
        self.angle = 45
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.x = screen_obj.screen_width / 2 - self.size[0] / 2
        self.rect.y = screen_obj.screen_height - self.size[1] * 10

    def move(self):
        radians = math.radians(self.angle)
        self.rect.x += self.speed_x * math.sin(radians)
        self.rect.y -= self.speed_y * math.cos(radians)
        return

    def update(self, game):
        game.border_collision()
        self.move()
        return


class Screen(object):
    def __init__(self):
        self.title = "Fracture"
        self.screen_width = 800
        self.screen_height = 800
        self.screen = self.set_screen()

    def set_screen(self):
        pygame.display.set_caption(self.title)
        size = self.screen_width, self.screen_height
        screen = pygame.display.set_mode(size)
        return screen


class Game(object):
    def __init__(self):
        self.screen_obj = Screen()
        self.sphere_sprites = pygame.sprite.RenderUpdates()
        self.border_sprites = pygame.sprite.RenderPlain()
        self.player_sprites = pygame.sprite.RenderUpdates()

        # Time Handling
        self.clock = pygame.time.Clock()
        self.max_FPS = 60
        self.frame_count = 0
        self.seconds = 0

        return

    def check_frame_count(self):
        if self.frame_count >= self.max_FPS:
            self.frame_count = 0
            self.seconds += 1
        return

    def continue_game(self, title_screen=False):
        if not (self.get_game_events(title_screen)):
            return False
        self.clock.tick(self.max_FPS)
        self.frame_count += 1
        self.check_frame_count()
        return True

    #####################
    #      Getters      #
    #####################
    @staticmethod
    def get_game_events(title_screen=False):
        # mouse_position = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if title_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return False       
        return True

    def get_border_sprites(self):
        self.border_sprites.add(Border(self.screen_obj, "left"))
        self.border_sprites.add(Border(self.screen_obj, "right"))
        self.border_sprites.add(Border(self.screen_obj, "top"))
        return

    def get_sprites(self):
        self.get_border_sprites()
        self.sphere_sprites.add(Sphere(self.screen_obj))
        # self.player_sprites.add(Player(self.screen_obj))
        return

    def border_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.sphere_sprites, 
            self.border_sprites, 
            0, 
            0
        )
        for sphere in collisions:
            border = collisions[sphere][0]
            if border.side == "left" or border.side == "right":
                sphere.speed_x *= -1
            if border.side == "top":
                if sphere.speed_y > 0:
                    sphere.speed_y *= -1
        return

    def play(self):
        self.get_sprites()
        while self.continue_game():
            self.screen_obj.screen.fill((0, 0, 0))
            self.border_sprites.draw(self.screen_obj.screen)
            self.sphere_sprites.draw(self.screen_obj.screen)    
            # self.player_sprites.draw(self.screen_obj.screen)
            self.sphere_sprites.update(self)
            pygame.display.update()
        return


def quit_game():
    pygame.quit()
    sys.exit(0)


#####################
#        Main       #
#####################
def main():
    game = Game()
    # game.title_screen()
    game.play()
    quit_game()


if __name__ == "__main__":
    main()
