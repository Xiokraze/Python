# import math
import sys
import random
from PIL import ImageFont
import level_classes
import sprite_classes
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


class Game(object):
    # Primary game object class that handles the game's functionality.
    class Screen(object):
        # Screen object
        def __init__(self):
            self.title = "Fracture"
            self.screen_width = 800
            self.screen_height = 800
            self.top_padding = 200
            self.x_min = 50
            self.x_max = self.screen_width - self.x_min
            self.border_width = 20
            self.screen = self.set_screen()

        # Sets pygame window title display mode
        def set_screen(self):
            pygame.display.set_caption(self.title)
            size = (self.screen_width, self.screen_height)
            screen = pygame.display.set_mode(size)
            return screen

    def __init__(self):
        self.screen_obj = self.Screen()

        # Sprites
        self.sphere_sprites = pygame.sprite.RenderUpdates()
        self.border_sprites = pygame.sprite.RenderPlain()
        self.player_sprites = pygame.sprite.RenderUpdates()
        self.block_sprites = pygame.sprite.RenderPlain()
        self.all_sprites = pygame.sprite.Group()

        # Game Statistics
        self.player_lives = 3
        self.lives_px_offset = 5
        self.score = 0

        # Time Handling
        self.clock = pygame.time.Clock()
        self.max_FPS = 60
        self.frame_count = 0
        self.seconds = 0
        self.blink_frame_count = 0
        self.blink_delay = .5
        self.blinking = True

        # Prompts
        self.title_prompt = "PRESS ENTER"

        # Level
        self.level_num = 1
        self.level_obj = self.get_level_obj()

        # Fonts/Colors
        self.master_font = "Media/ariblk.ttf"
        self.font_size = 20
        self.text_color = (255, 255, 255)
        self.font = ImageFont.truetype(self.master_font, self.font_size)
        self.word_font = pygame.font.Font(self.master_font, self.font_size)

        # Media
        self.game_background = pygame.image.load("Media/backgrounds/space1.png")
        self.title_image = pygame.image.load("Media/title_image.png")
        self.player_lives_image = pygame.image.load("Media/player/player_default.png")
        self.splash_level = pygame.image.load("Media/splash_level.png")
        self.splash_complete = pygame.image.load("Media/splash_complete.png")

    #####################
    #    Game Control   #
    #####################
    def update(self):
        # Call update functions on sprites and the display.
        self.player_sprites.update()
        self.sphere_sprites.update(self)
        pygame.display.update()
        return

    def update_seconds(self):
        # Time handler for tracking the on/off of blinking text. Compares a
        # copy of the number of game frames against the max frames per second
        # and returns true if equal or false if not.
        self.blink_frame_count += 1
        blink_frame_count = self.max_FPS * self.blink_delay
        if self.blink_frame_count == blink_frame_count:
            self.blink_frame_count = 0
            return True
        return False

    def blink_text(self, prompt):
        # Handles blinking title screen text.
        if self.update_seconds():
            if self.blinking:
                self.blinking = False
                return True
            else:
                self.blinking = True
        if self.blinking:
            self.draw_blink_text(prompt)
        return False

    def check_frame_count(self):
        # Tracks the number of seconds elapsed by comparing the frame count
        # against the max frames per second.
        if self.frame_count >= self.max_FPS:
            self.frame_count = 0
            self.seconds += 1
        return

    def continue_game(self, title_screen=False):
        # Primary game time handler. Checks if user has pressed enter on the
        # title screen to move on to the game screen or if the user has exited
        # the game by closing the window. Also handles ticking the game clock,
        # and tracking the frame count.
        if self.get_game_events(title_screen):
            return False
        self.clock.tick(self.max_FPS)
        self.frame_count += 1
        self.check_frame_count()
        return True

    def player_missed_sphere(self, sphere):
        sphere.kill()
        self.player_lives -= 1
        if self.player_lives != 0:
            self.get_new_sphere()
        return

    def reset_sprites(self):
        # When a level changes, resets all sprites.
        for sprite in self.all_sprites:
            sprite.kill()
        self.get_sprites()
        return

    def level_completed(self):
        # Level has been completed, increases current level number, gets the
        # new level object, and resets all the sprites.
        self.level_num += 1
        self.level_obj = self.get_level_obj()
        self.reset_sprites()
        self.draw_level_splash_screen()
        return

    def play(self):
        # The primary game loop function. Gets the initial starting sprite
        # lists, draws the screen and sprite images, updates the sprites and
        # display, then checks if the level is complete or player has run out
        # of lives.
        self.get_sprites()
        while self.continue_game():
            self.draw_game_background()
            self.draw_hud()
            self.all_sprites.draw(self.screen_obj.screen)
            self.draw_borders()
            self.update()

            # Check if the player has run out of lives.
            if self.player_lives == 0:
                print("game over")
                break

            # Check if the level has been completed.
            if len(self.block_sprites) == 0:
                self.level_completed()
        return

    def title_screen(self):
        # Handles the game's title screen.
        while self.continue_game(True):
            self.draw_game_background()
            self.draw_title_image()
            self.blink_text(self.title_prompt)
            pygame.display.update()
        return

    #####################
    #      Getters      #
    #####################
    def get_level_obj(self):
        level = level_classes.Level(self.level_num, self.screen_obj)
        return level

    @staticmethod
    def get_game_events(title_screen=False):
        # Gets pygame events and returns true/false if the user quit the game
        # by closing the game window. Also returns true/false if on the title
        # screen and the player presses enter.

        # mouse_position = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit_game()
            if title_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
        return False

    def get_border_sprites(self):
        # Creates the left, right, top, and bottom border sprites.
        self.border_sprites.add(sprite_classes.Border(self.screen_obj, "left"))
        self.border_sprites.add(sprite_classes.Border(self.screen_obj, "right"))
        self.border_sprites.add(sprite_classes.Border(self.screen_obj, "top"))
        self.border_sprites.add(sprite_classes.Border(self.screen_obj, "bot"))
        return

    def get_block_sprites(self):
        # Converts the current level's block list into sprites.
        for block in self.level_obj.blocks:
            self.block_sprites.add(sprite_classes.Block(block))
        return

    def get_all_sprites(self):
        # Adds all sprite groups to a primary group.
        for border in self.border_sprites:
            self.all_sprites.add(border)
        for player in self.player_sprites:
            self.all_sprites.add(player)
        for block in self.block_sprites:
            self.all_sprites.add(block)
        return

    def get_new_sphere(self):
        self.sphere_sprites.add(sprite_classes.Sphere(self.screen_obj))
        for sphere in self.sphere_sprites:
            self.all_sprites.add(sphere)
        return

    def get_sprites(self):
        # Handles creation of all the sprite groups.
        self.get_border_sprites()
        self.get_new_sphere()
        self.player_sprites.add(sprite_classes.Player(self.screen_obj))
        self.get_block_sprites()
        self.get_all_sprites()
        return

    def get_sphere_border_collision(self, sphere):
        # Returns result of pygame's sprite collision function call between
        # the sphere and the border sprite group.
        border_collision = pygame.sprite.spritecollide(
            sphere,
            self.border_sprites,
            False
        )
        return border_collision

    def get_sphere_block_collision(self, sphere):
        # Returns result of pygame's sprite collision function call between
        # the sphere and the block sprite group.
        block_collision = pygame.sprite.spritecollide(
            sphere,
            self.block_sprites,
            False
        )
        return block_collision

    def get_sphere_player_collision(self):
        # Returns result of pygame's sprite collision function call between
        # the sphere sprite group and the player sprite group.
        collisions = pygame.sprite.groupcollide(
            self.sphere_sprites,
            self.player_sprites,
            0,
            0
        )
        return collisions

    #####################
    #     Collision     #
    #####################
    def border_collision(self):
        for sphere in self.sphere_sprites:
            border_collision = self.get_sphere_border_collision(sphere)
            if border_collision:
                border = border_collision[0]
                if border.side == "bot" and len(self.sphere_sprites) == 1:
                    self.player_missed_sphere(sphere)
                else:
                    sphere.set_border_deflection_angle(border)
        return

    def block_collision(self):
        # Iterates through each sphere in the sphere sprite group and checks
        # for block collision. The block's image is updated or killed depending
        # on the block's health.
        for sphere in self.sphere_sprites:
            block_collision = self.get_sphere_block_collision(sphere)
            if block_collision:
                block = block_collision[0]
                sphere.set_block_deflection_angle(block)

                # TODO change block image dependent on health, add unbreakable
                # blocks, scoring, etc.
                if block.health == 1:
                    block.kill()
                else:
                    block.health -= 1
        return

    def player_collision(self):
        # Handles sphere/player collisions. Gets dictionary of player and
        # sphere collisions and sets the angle of the sphere based on which
        # player segment was hit.
        player_collision = self.get_sphere_player_collision()
        for sphere in player_collision:
            player = player_collision[sphere][0]
            segments = player.get_segments(sphere)
            sphere.set_player_deflection_angle(segments)
        return

    #####################
    #      Drawing      #
    #####################
    def draw_title_image(self):
        # Draws the title screen game text.
        size = self.title_image.get_size()
        x = self.screen_obj.screen_width / 2 - size[0] / 2
        y = size[1]
        self.screen_obj.screen.blit(self.title_image, (x, y))
        return

    def draw_blink_text(self, prompt):
        # Draws the title screen blink text.
        text = self.word_font.render(prompt, 1, self.text_color)
        size = self.font.getsize(prompt)
        x = self.screen_obj.screen_width / 2 - size[0] / 2
        y = self.screen_obj.screen_height / 2 + size[1]
        self.screen_obj.screen.blit(text, (x, y))
        return

    def draw_borders(self):
        for border in self.border_sprites:
            border.draw(self.screen_obj)
        return

    def draw_game_background(self):
        # self.screen_obj.screen.blit(self.game_background, (0, 0))
        self.screen_obj.screen.fill((0, 0, 0))
        return

    def draw_player_lives(self):
        for player in self.player_sprites:
            image = self.player_lives_image
            x = player.x_min
            y = self.screen_obj.top_padding - self.screen_obj.border_width
            for i in range(self.player_lives):
                self.screen_obj.screen.blit(image, (x, y))
                x += player.size[0] + self.lives_px_offset
        return

    def draw_hud(self):
        self.draw_player_lives()
        # TODO draw score
        # TODO draw level number
        return

    def draw_level_image(self):
        # Draws the splash screen "Level" text
        size = self.splash_level.get_size()
        x = self.screen_obj.screen_width / 2 - size[0] / 2
        y = size[1]
        self.screen_obj.screen.blit(self.splash_level, (x, y))

        size = self.splash_complete.get_size()
        x = self.screen_obj.screen_width / 2 - size[0] / 2
        y = size[1] * 2
        self.screen_obj.screen.blit(self.splash_complete, (x, y))
        return

    def draw_level_splash_background(self):
        # self.screen_obj.screen.fill((100, 100, 100))
        self.screen_obj.screen.fill((0, 0, 0))
        return

    def draw_level_splash_screen(self):
        # Handles the game's splash screen when levels are completed
        while self.continue_game(True):
            self.draw_level_splash_background()
            self.draw_level_image()
            self.blink_text(self.title_prompt)
            pygame.display.update()
        return


#####################
#        Main       #
#####################
def quit_game():
    # Handles the game closing, quits pygame and exits the program.
    pygame.quit()
    sys.exit(0)


def main():
    # Primary application loop. Initializes the game object, runs the title
    # screen, plays the game, and quits.
    game = Game()
    game.title_screen()
    game.play()
    quit_game()


if __name__ == "__main__":
    main()
