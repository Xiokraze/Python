import pygame
pygame.init()
import Draw
import Events
import Levels
import Player
import Spheres
from PIL import ImageFont


#####################
#     Game Class    #
#####################
class Game:
    def __init__(self):

        # Screen
        self.title = "Fracture"
        self.title_prompt = "PRESS ENTER"
        self.screen_width = 800
        self.screen_height = 600
        self.background = (0,0,0)

        # Fonts/Colors
        self.master_font = "Media/ariblk.ttf"
        self.font_size = 20
        self.text_color = (255,255,255)
        self.font = ImageFont.truetype(self.master_font, self.font_size)
        self.word_font = pygame.font.Font(self.master_font, self.font_size)

        # Important Variables
        self.level = None
        self.level_number = 1

        # Time Handling
        self.clock = pygame.time.Clock()
        self.max_FPS = 60
        self.frame_count = 0
        self.blink_frame_count = 0
        self.blink_delay = .5
        self.blinking = True
        self.seconds = 0

        # Media
        self.title_image = pygame.image.load("Media/title_image.png")
        self.sphere = pygame.image.load("Media/spheres/dark_blue.png")



    def get_image_size(self, image):
        image_size = image.get_size()
        width = image_size[0]
        height = image_size[1]
        return width, height

    def set_screen(self):
        pygame.display.set_caption(self.title)
        size = (self.screen_width, self.screen_height)
        screen = pygame.display.set_mode(size)
        return screen

    def draw_blink_text(self, screen, text):
        Draw.blink_text(self, screen, text)
        return


#####################
# Game Time Handler #
#####################
def continue_game(game, title_screen=False):
    if not (Events.check_game_events(title_screen)):
        return False
    game.clock.tick(game.max_FPS)
    game.frame_count += 1
    Events.check_frame_count(game)
    return True


#####################
#    Title Screen   #
#####################
def title_screen(game, screen):
    title_screen = True
    while (continue_game(game, title_screen)):
        Draw.title_screen(game, screen)
        Events.blink_text(game, screen, game.title_prompt)
        pygame.display.update()
    
    return


#####################
#    Game Handler   #
#####################
def play_game(game, screen):
    Spheres.Sphere(game)
    player = Player.Player(game)
    while (continue_game(game)):
        game.level = Levels.Level(game)
        spheres = Spheres.Sphere.sphere_list
        Draw.draw_game(game, screen, player, spheres)
        Spheres.update(game, player, spheres)
        player.get_input(game)
    return


#####################
#        Main       #
#####################
def main():
    game = Game()
    screen = game.set_screen()

    #title_screen(game, screen)
    play_game(game, screen)
    Events.quit_game()


if __name__ == "__main__":
    main()