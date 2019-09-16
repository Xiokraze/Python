import math
import sys
import random
from PIL import ImageFont
import level_handling
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


class Player(pygame.sprite.Sprite):
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

    def get_segments(self):
        # Player image divided into 4 equal segments
        segments = []
        x = self.rect.x
        width = self.size[0]
        segment_width = width / 4
        for i in range(4):
            segments.append((x, x + segment_width))
            x += segment_width
        return segments

    def move_left(self):
        x = self.rect.x - self.speed - self.border_padding
        if x > self.x_min:
            self.rect.x -= self.speed
        return

    def move_right(self):
        x = self.rect.x + self.size[0] + self.speed + self.border_padding
        if x < self.x_max:
            self.rect.x += self.speed
        return

    def update(self):
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


class Screen(object):
    # Object to handle screen parameters
    def __init__(self):
        self.title = "Fracture"
        self.screen_width = 800
        self.screen_height = 800
        self.top_padding = 200
        self.x_min = 50
        self.x_max = self.screen_width - self.x_min
        self.border_width = 20
        self.screen = self.set_screen()

    def set_screen(self):
        pygame.display.set_caption(self.title)
        size = self.screen_width, self.screen_height
        screen = pygame.display.set_mode(size)
        return screen


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

    def get_sides(self):
        # center pixels on each of the sphere's side (left, right, top, bot)
        sides = []
        left = (self.rect.x, self.rect.y + self.size[1] / 2)
        right = (self.rect.x + self.size[0], self.rect.y + self.size[1] / 2)
        # top of block but bottom y px position
        bot = (self.rect.x + self.size[0] / 2, self.rect.y)
        # bottom of block but top y px position
        top = (self.rect.x + self.size[0] / 2, self.rect.y + self.size[1])
        top_left = (self.rect.x, self.rect.y)
        top_right = (self.rect.x + self.size[0], self.rect.y)
        bot_left = (self.rect.x, self.rect.y + self.size[1])
        bot_right = (self.rect.x + self.size[0], self.rect.y + self.size[1])
        sides.append(left)
        sides.append(right)
        sides.append(top)
        sides.append(bot)
        sides.append(top_left)
        sides.append(top_right)
        sides.append(bot_left)
        sides.append(bot_right)
        return sides

    def get_block_side_collision(self, block):  # TODO add corner collision handling
        block_side = block.get_sides()
        sphere_sides = self.get_sides()
        sides = ("left", "right", "top", "bot",
                 "top_left", "top_right", "bot_left", "bot_right")
        index = 0
        for sphere_side in sphere_sides:
            if block_side[0] < sphere_side[0] < block_side[1]:
                if block_side[2] < sphere_side[1] < block_side[3]:
                    return sides[index]
            index += 1
        return ""

    def set_block_deflection_angle(self, block):
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
        if border.side == "left":
            self.angle = 360 - self.angle
        if border.side == "right":
            self.angle = 360 - self.angle
        if border.side == "top":
            self.angle = (180 - self.angle) % 360
        if border.side == "bot":
            pass  # Place holder for sphere/bottom border collision handling
        return

    def set_player_deflection_angle(self, player_segments):
        # Set angle according to which player segments was collided with
        segment_num = 0
        for start, end in player_segments:
            if (start - self.size[0]) <= self.rect.x < (end + self.size[0]):
                break
            segment_num += 1
        self.angle = self.player_angles[segment_num]
        return

    def move(self):
        radians = math.radians(self.angle)
        self.rect.y += int(self.speed_y * math.cos(radians))
        self.rect.x += int(self.speed_x * math.sin(radians))
        return

    def update(self, game):
        game.border_collision()
        game.player_collision()
        game.block_collision()
        self.move()
        return


class Game(object):
    def __init__(self):
        self.screen_obj = Screen()
        self.sphere_sprites = pygame.sprite.RenderUpdates()
        self.border_sprites = pygame.sprite.RenderPlain()
        self.player_sprites = pygame.sprite.RenderUpdates()
        self.block_sprites = pygame.sprite.RenderPlain()
        self.all_sprites = pygame.sprite.Group()

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

        # Levels
        self.level_num = 1
        self.level_obj = level_handling.Level(self.level_num, self.screen_obj)

        # Fonts/Colors
        self.master_font = "Media/ariblk.ttf"
        self.font_size = 20
        self.text_color = (255, 255, 255)
        self.font = ImageFont.truetype(self.master_font, self.font_size)
        self.word_font = pygame.font.Font(self.master_font, self.font_size)

        # Media
        self.game_background = pygame.image.load("Media/backgrounds/space1.png")
        self.title_image = pygame.image.load("Media/title_image.png")

    #####################
    #    Game Control   #
    #####################
    def update_seconds(self):
        self.blink_frame_count += 1
        blink_frame_count = self.max_FPS * self.blink_delay
        if self.blink_frame_count == blink_frame_count:
            self.blink_frame_count = 0
            return True
        return False

    def check_frame_count(self):
        if self.frame_count >= self.max_FPS:
            self.frame_count = 0
            self.seconds += 1
        return

    def continue_game(self, title_screen=False):
        if self.get_game_events(title_screen):
            return False
        self.clock.tick(self.max_FPS)
        self.frame_count += 1
        self.check_frame_count()
        return True

    def play(self):
        self.get_sprites()
        while self.continue_game():
            self.draw_game_background()
            self.all_sprites.draw(self.screen_obj.screen)
            self.draw_borders()
            self.player_sprites.update()
            self.sphere_sprites.update(self)
            pygame.display.update()

            # # If player has advanced to next level, get appropriate level
            # if self.level_obj.check_level(self.level_num):
            #     self.level_obj = Level(self.level_num)
        return

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit(0)

    #####################
    #      Getters      #
    #####################
    @staticmethod
    def get_game_events(title_screen=False):
        # mouse_position = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True
            if title_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
        return False

    def get_border_sprites(self):
        self.border_sprites.add(level_handling.Border(self.screen_obj, "left"))
        self.border_sprites.add(level_handling.Border(self.screen_obj, "right"))
        self.border_sprites.add(level_handling.Border(self.screen_obj, "top"))
        self.border_sprites.add(level_handling.Border(self.screen_obj, "bot"))
        return

    def get_block_sprites(self):
        for block in self.level_obj.blocks:
            self.block_sprites.add(level_handling.Block(block))
        return

    def get_all_sprites(self):
        for border in self.border_sprites:
            self.all_sprites.add(border)
        for sphere in self.sphere_sprites:
            self.all_sprites.add(sphere)
        for player in self.player_sprites:
            self.all_sprites.add(player)
        for block in self.block_sprites:
            self.all_sprites.add(block)
        return

    def get_sprites(self):
        self.get_border_sprites()
        self.sphere_sprites.add(Sphere(self.screen_obj))
        self.player_sprites.add(Player(self.screen_obj))
        self.get_block_sprites()
        self.get_all_sprites()
        return

    def get_sphere_border_collision(self, sphere):
        border_collision = pygame.sprite.spritecollide(
            sphere,
            self.border_sprites,
            False
        )
        return border_collision

    def get_sphere_block_collision(self, sphere):
        block_collision = pygame.sprite.spritecollide(
            sphere,
            self.block_sprites,
            True
        )
        return block_collision

    #####################
    #     Collision     #
    #####################
    def block_collision(self):
        for sphere in self.sphere_sprites:
            block_collision = self.get_sphere_block_collision(sphere)
            if block_collision:
                block = block_collision[0]
                sphere.set_block_deflection_angle(block)

    def player_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.sphere_sprites,
            self.player_sprites,
            0,
            0
        )
        for sphere in collisions:
            player = collisions[sphere][0]
            segments = player.get_segments()
            sphere.set_player_deflection_angle(segments)
        return

    def border_collision(self):
        for sphere in self.sphere_sprites:
            border_collision = self.get_sphere_border_collision(sphere)
            if border_collision:
                border = border_collision[0]
                if border.side == "bot":
                    sphere.kill()
                    continue
                sphere.set_border_deflection_angle(border)
        return

    #####################
    #      Drawing      #
    #####################
    def draw_borders(self):
        for border in self.border_sprites:
            border.draw(self.screen_obj)
        return

    def draw_game_background(self):
        # self.screen_obj.screen.blit(self.game_background, (0, 0))
        self.screen_obj.screen.fill((0, 0, 0))
        return

    #####################
    #    Title Screen   #
    #####################
    def blink_text(self):
        if self.update_seconds():
            if self.blinking:
                self.blinking = False
                return True
            else:
                self.blinking = True
        if self.blinking:
            self.draw_blink_text(self.title_prompt)
        return False

    def draw_blink_text(self, prompt):
        text = self.word_font.render(prompt, 1, self.text_color)
        size = self.font.getsize(prompt)
        x = self.screen_obj.screen_width / 2 - size[0] / 2
        y = self.screen_obj.screen_height / 2 + size[1]
        self.screen_obj.screen.blit(text, (x, y))
        return

    def draw_title_image(self):
        size = self.title_image.get_size()
        x = self.screen_obj.screen_width / 2 - size[0] / 2
        y = size[1]
        self.screen_obj.screen.blit(self.title_image, (x, y))
        return

    def title_screen(self):
        while self.continue_game(True):
            self.draw_game_background()
            self.draw_title_image()
            self.blink_text()
            pygame.display.update()
        return


#####################
#        Main       #
#####################
def main():
    game = Game()
    game.title_screen()
    game.play()
    game.quit_game()


if __name__ == "__main__":
    main()
