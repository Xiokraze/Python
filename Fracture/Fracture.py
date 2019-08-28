import pygame
pygame.init()
import Draw
import Events
import Sphere
from PIL import ImageFont


class Game:
    def __init__(self):
        # Screen
        self.title = "Fracture"
        self.title_prompt = "PRESS ENTER"
        self.screen_width = 800
        self.screen_height = 600

        # Fonts/Colors
        self.master_font = "Media/ariblk.ttf"
        self.font_size = 20
        self.text_color = (255,255,255)
        self.font = ImageFont.truetype(self.master_font, self.font_size)
        self.word_font = pygame.font.Font(self.master_font, self.font_size)

        # Time Handling
        self.clock = pygame.time.Clock()
        self.max_FPS = 50
        self.frame_count = 0
        self.blink_frame_count = 0
        self.blink_delay = .5
        self.blinking = True
        self.seconds = 0

        # Media
        self.title_image = pygame.image.load("Media/title_image.png")
        self.sphere = pygame.image.load("Media/spheres/dark_blue.png")

    def set_screen(self):
        pygame.display.set_caption(self.title)
        size = (self.screen_width, self.screen_height)
        screen = pygame.display.set_mode(size)
        return screen

    def draw_blink_text(self, screen, text):
        Draw.blink_text(self, screen, text)
        return


def title_screen(game, screen):
    while (True):
        if (Events.check_title_events(game)):
            break
        game.clock.tick(game.max_FPS)
        game.frame_count += 1
        Events.check_frame_count(game)
        screen.fill((0,0,0))
        Draw.title_image(game, screen)
        Events.blink_text(game, screen, game.title_prompt)
        pygame.display.update()
    return

def blink_text(game, screen, text):
    font_size = game.font.getsize(text)
    x = (game.screen_width / 2) - (font_size[0] / 2)
    y = (game.screen_height / 2) + font_size[1]
    text = game.word_font.render(text, 1, game.text_color)
    screen.blit(text, (x,y))
    return

def play_game(game, screen):
    game.seconds = 0
    Sphere.Sphere(game)
    while (True):
        if not (Events.check_game_events(game)):
            break
        game.clock.tick(game.max_FPS)
        game.frame_count += 1
        Events.check_frame_count(game)
        screen.fill((0,0,0))
        Sphere.update(game)
        Sphere.draw(game, screen)
        pygame.display.update()

def main():
    game = Game()
    screen = game.set_screen()

    title_screen(game, screen)
    play_game(game, screen)



if __name__ == "__main__":
    main()