import math
import sys
import random
from PIL import ImageFont
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


class Border(pygame.sprite.Sprite):  # TODO refactor
    def __init__(self, screen_obj, border_position):
        super().__init__()
        self.side = border_position
        side_padding = screen_obj.x_min
        side_height = screen_obj.screen_height - screen_obj.top_padding
        self.border_width = screen_obj.border_width
        border_width = self.border_width
        border_color = (0, 0, 255)

        if self.side == "left" or self.side == "right":
            self.image = pygame.Surface([border_width, side_height])
            self.image.fill(border_color)
            self.rect = self.image.get_rect()
            if self.side == "left":
                self.rect.x = side_padding
            else:
                x = screen_obj.screen_width - border_width - side_padding
                self.rect.x = x
            self.rect.y = screen_obj.top_padding

        if self.side == "top" or self.side == "bot":
            screen_width = screen_obj.screen_width
            width = screen_width - side_padding * 2 - self.border_width * 2
            self.image = pygame.Surface([width, border_width])
            self.image.fill(border_color)
            self.rect = self.image.get_rect()
            self.rect.x = 0 + side_padding + self.border_width
            if self.side == "top":
                self.rect.y = screen_obj.top_padding
            else:
                self.rect.y = screen_obj.screen_height


class Block(pygame.sprite.Sprite):
    def __init__(self, block):
        super().__init__()
        self.image = block[0]
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.x = block[1]
        self.rect.y = block[2]
        # Left Right Top Bot
        self.sides = self.get_sides()

    def get_sides(self):
        # Left Right Top Bot
        sides = []
        left = self.rect.x
        right = self.rect.x + self.size[0]
        top = self.rect.y
        bot = self.rect.y + self.size[1]
        sides.append(left)
        sides.append(right)
        sides.append(top)
        sides.append(bot)
        return sides


class Level(object):
    def __init__(self, level):
        self.level = level
        self.background = self.get_background()
        self.blocks = self.get_blocks()

    def get_blocks(self):
        blocks = []
        for block in Levels.get_positions(self.level):
            blocks.append(block)
        return blocks

    def get_background(self):
        if self.level == 1:
            background = pygame.image.load("Media/backgrounds/space1.png")
        return background

    def set_blocks(self):
        self.blocks = self.get_blocks()
        return

    def set_background(self):
        self.background = self.get_background()
        return

    def set_level(self, level):
        self.level = level
        return

    def check_level(self, level_num):
        if level_num != self.level:
            return True
        return False


class Levels:
    @staticmethod
    def get_positions(level):
        blue = pygame.image.load("Media/blocks/blue_01.png")
        if level == 1:
            blocks = (
                (blue, 300, 400),
                (blue, 400, 400),
                (blue, 600, 400),
                (blue, 500, 600),
                (blue, 100, 400),
            )
        return blocks


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
        self.image = pygame.image.load("Media/spheres/dark_blue.png")
        self.speed = 5
        self.speed_x = self.speed
        self.speed_y = self.speed * -1
        self.angle = 45
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
        # top of block but bottom y position
        bot = (self.rect.x + self.size[0] / 2, self.rect.y)
        # bottom of block but top y position
        top = (self.rect.x + self.size[0] / 2, self.rect.y + self.size[1])
        sides.append(left)
        sides.append(right)
        sides.append(top)
        sides.append(bot)
        return sides

    def get_block_side_collision(self, block):
        # x/y axes px for each block's side (left, right, top, bot)
        bs = block.get_sides()
        # center pixels on each of the sphere's side (left, right, top, bot)
        sphere_sides = self.get_sides()
        # Side to return
        sides = ("left", "right", "top", "bot")
        index = 0
        print("testing")
        for coord in sphere_sides:
            if bs[0] < coord[0] < bs[1]:
                if bs[2] < coord[1] < bs[3]:
                    return sides[index]
            index += 1
        return ""

    def set_block_deflection_angle(self, block):
        block_side = self.get_block_side_collision(block)
        if block_side == "left" or block_side == "right":
            self.angle = 360 - self.angle
        if block_side == "top" or block_side == "bot":
            self.angle = (180 - self.angle) % 360
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

    def new_angle(self, player_segments):
        segment_num = 0
        for start, end in player_segments:
            if start <= self.rect.x < end:
                break
            segment_num += 1
        if segment_num == 0:
            self.angle = 300
        elif segment_num == 1:
            self.angle = 340
        elif segment_num == 2:
            self.angle = 20
        elif segment_num == 3:
            self.angle = 60
        return

    def move(self):
        radians = math.radians(self.angle)
        move_x = int(self.speed_x * math.sin(radians))
        move_y = int(self.speed_y * math.cos(radians))
        self.rect.y += move_y
        self.rect.x += move_x
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
        self.level_obj = Level(self.level_num)

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
        if not (self.get_game_events(title_screen)):
            return False
        self.clock.tick(self.max_FPS)
        self.frame_count += 1
        self.check_frame_count()
        return True

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
        self.border_sprites.add(Border(self.screen_obj, "bot"))
        return

    def get_block_sprites(self):
        for block in self.level_obj.blocks:
            self.block_sprites.add(Block(block))
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
            sphere.new_angle(segments)
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

    def play(self):
        self.get_sprites()
        while self.continue_game():
            self.draw_game_background()
            self.all_sprites.draw(self.screen_obj.screen)
            self.player_sprites.update()
            self.sphere_sprites.update(self)
            pygame.display.update()

            # If player has advanced to next level, get appropriate level
            if self.level_obj.check_level(self.level_num):
                self.level_obj = Level(self.level_num)
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

    def draw_game_background(self):
        # self.screen_obj.screen.blit(self.game_background, (0, 0))
        self.screen_obj.screen.fill((0, 0, 0))
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
