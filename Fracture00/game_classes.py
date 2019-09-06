import pygame
import random
import math
import drawing
import game_levels
from PIL import ImageFont


#####################
#     Game Class    #
#####################
class Game:
    def __init__(self):
        # Screen
        #self.title = "Fracture"
        self.title_prompt = "PRESS ENTER"
        #self.screen_width = 800
        #self.screen_height = 800
        #self.screen = self.set_screen()

        # Fonts/Colors
        self.master_font = "Media/ariblk.ttf"
        self.font_size = 20
        self.text_color = (255,255,255)
        self.font = ImageFont.truetype(self.master_font, self.font_size)
        self.word_font = pygame.font.Font(self.master_font, self.font_size)

        # Time Handling
        self.clock = pygame.time.Clock()
        self.max_FPS = 60
        self.frame_count = 0
        self.blink_frame_count = 0
        self.blink_delay = .5
        self.blinking = True
        #self.seconds = 0

        # Media
        self.title_image = pygame.image.load("Media/title_image.png")
        #self.sphere_image = pygame.image.load("Media/spheres/dark_blue.png")
        self.player_image = pygame.image.load("Media/player/player_default.png")

        # Block Media
        self.blue_block = pygame.image.load("Media/blocks/blue_01.png")

        # Border Media
        self.fractured_gray = [
            pygame.image.load("Media/borders/fractured_stone/dark%s.png" % i)
            for i in range(8)
        ]

        # Background Media
        self.bg_space = pygame.image.load("Media/backgrounds/space1.png")

        # Level Variables
        self.level_number = 1
        self.level = self.set_game_level()

        # Sounds
        # Little Robot Factory www.littlerobotsoundfactory.com


    #####################
    #  Getters/Setters  #
    #####################
    def get_image_size(self, image):
        image_size = image.get_size()
        width = image_size[0]
        height = image_size[1]
        return width, height

    def get_title_image_location(self):
        image_size = self.title_image.get_size()
        x = self.screen_width / 2 - image_size[0] / 2
        y = 0 + image_size[1]
        return x, y

    def get_title_prompt_location(self, prompt):
        font_size = self.font.getsize(prompt)
        x = (self.screen_width / 2) - (font_size[0] / 2)
        y = (self.screen_height / 2) + font_size[1]
        return x, y

    #@staticmethod
    #def get_game_events(title_screen=False):
    #    mouse_position = pygame.mouse.get_pos()
    #    events = pygame.event.get()
    #    for event in events:
    #        if (event.type == pygame.QUIT):
    #            return False
    #        if (title_screen):
    #            if (event.type == pygame.KEYDOWN):
    #                if (event.key == pygame.K_RETURN):
    #                    return False       
    #    return True

    def set_game_level(self):
        level = Level(self)
        return level

    #def set_screen(self):
    #    pygame.display.set_caption(self.title)
    #    size = (self.screen_width, self.screen_height)
    #    screen = pygame.display.set_mode(size)
    #    return screen


    #####################
    #      Drawing      #
    #####################
    def draw_game(self, player, spheres):
        drawing.draw_background(self)
        self.level.draw_level_background(self, self.screen)
        drawing.draw_playable_borders(self, self.screen)
        drawing.draw_ui_borders(self, self.screen)
        self.level.draw_blocks(self.screen)
        player.draw(self.screen)
        drawing.draw_spheres(self.screen, spheres)
        pygame.display.update()
        return

    #####################
    #    Title Screen   #
    #####################
    def title_screen(self):
        title_screen = True
        while (self.continue_game(title_screen)):
            drawing.draw_background(self)
            drawing.draw_title_image(self)
            self.blink_text(self.title_prompt)
            pygame.display.update()
        return


    #####################
    #     Game Time     #
    #####################
    #def check_frame_count(self):
    #    if (self.frame_count >= self.max_FPS):
    #        self.frame_count = 0
    #        self.seconds += 1
    #    return

    #def continue_game(self, title_screen=False):
    #    if not (self.get_game_events(title_screen)):
    #        return False
    #    self.clock.tick(self.max_FPS)
    #    self.frame_count += 1
    #    self.check_frame_count()
    #    return True

    #def update_seconds(self):
    #    self.blink_frame_count += 1
    #    blink_frame_count = self.max_FPS * self.blink_delay
    #    if (self.blink_frame_count == (blink_frame_count)):
    #        self.blink_frame_count = 0
    #        return True
    #    return False

    def blink_text(self, prompt):
        if (self.update_seconds()):
            if (self.blinking):
                self.blinking = False
            else:
                self.blinking = True
        if (self.blinking):
            drawing.draw_blink_text(self, prompt)
        return

    #@staticmethod
    #def quit_game():
    #    pygame.quit()
    #    sys.exit(0)


#####################
#    Player Class   #
#####################
class Player:
    def __init__(self, game):
        self.image = game.player_image
        self.width, self.height = game.get_image_size(self.image)
        self.x, self.y = self.get_start_location(game)
        self.speed = 7
        self.top_border_width = 2
        self.rect = (self.x-2, self.y, self.width+4, self.height+2)
        self.segments = self.get_player_segments()


    #def draw(self, screen):
    #    screen.blit(self.image, (self.x, self.y))
    #    rect = (self.x - 2, self.y - 2, self.width + 4, self.height + 4)
    #    pygame.draw.rect(screen, (0,0,255), rect, 2)
    #    return

    #####################
    #      Getters      #
    #####################
    #def get_segment_position(self, sphere):
    #    segment_position = 0
    #    for segment in self.segments:
    #        x_start = segment[0]
    #        x_end = segment[1]
    #        if (sphere.circle_x >= x_start and sphere.circle_x <= x_end):
    #            return segment_position
    #        segment_position += 1
    #    return

    #def get_player_segments(self):
    ## Player image _______________________________
    ##             [___0___|___1___|___2___|___3___]
    ## Segments    x      x1      x2      x3      x4
    #    segments = []
    #    num_segments = 4
    #    fraction = .25
    #    multiplier = 0
    #    for i in range(num_segments):
    #        x1 = int(self.x + self.width * multiplier)
    #        multiplier += fraction
    #        x2 = int(self.x + self.width * multiplier)
    #        segments.append([x1, x2])
    #    return segments

    #def get_start_location(self, game):
    #    x = game.screen_width / 2 - self.width / 2
    #    y = game.screen_height - self.height * 5
    #    return x, y

    #def get_player_movement(self, game):
    #    # Mouse
    #    if (pygame.mouse.get_pressed()[0]):
    #        pygame.mouse.set_visible(False)
    #        mouse_pos = pygame.mouse.get_pos()
    #        if (mouse_pos[0] < self.x + self.width / 2):
    #            self.move_left(game)
    #        if (mouse_pos[0] > self.x + self.width / 2):
    #            self.move_right(game)
    #    else:
    #        pygame.mouse.set_visible(True)
    #    # Left/Right arrow keys
    #    keys = pygame.key.get_pressed()
    #    if (keys[pygame.K_LEFT]):
    #        self.move_left(game)
    #    if (keys[pygame.K_RIGHT]):
    #        self.move_right(game)
    #    return


    #####################
    #      Movement     #
    #####################
    def move_left(self, game):
        if (self.x - self.speed > game.level.x_left):
            self.x -= self.speed
            self.rect = (self.x-2, self.y, self.width+4, self.height+2)
        return

    def move_right(self, game):
        if (self.x + self.width + self.speed < game.level.x_right):
            self.x += self.speed
            self.rect = (self.x-2, self.y, self.width+4, self.height+2)
        return


#####################
#    Sphere Class   #
#####################
class Sphere:
    sphere_list = []
    def __init__(self, game):
        self.image = game.sphere_image
        self.default_speed_x = 5
        self.speed_x = self.default_speed_x
        self.speed_y = -self.default_speed_x
        self.width, self.height = game.get_image_size(self.image)
        self.angle = 45
        self.radians = math.radians(self.angle)
        self.x = game.screen_width / 2
        self.y = game.screen_height - self.x
        self.player_deflection_angles = [300, 340, 20, 60]
        self.hit_wall_sound = pygame.mixer.Sound("Media/sounds/hit_wall.wav")

        # Generate circle for more accurate collision detection
        self.circle_color = (0,255,0)
        self.circle_x = int(self.x + self.width / 2)
        self.circle_y = int(self.y + self.height / 2)
        self.circle_radius = int(self.width/2)
        self.collision_coords = self.get_collision_coords()

        # Add the sphere to the spheres list
        Sphere.sphere_list.append(self)

    def draw_sphere(self, screen):
        pygame.draw.circle(
            screen, 
            self.circle_color, 
            (int(self.circle_x), int(self.circle_y)), 
            self.circle_radius
        )
        screen.blit(self.image, (self.x,self.y))
        return

    #def move(self):
    #    move_x = self.speed_x * math.sin(self.radians)
    #    move_y = self.speed_y * math.cos(self.radians)
    #    self.x += move_x
    #    self.circle_x += move_x
    #    self.y += move_y
    #    self.circle_y += move_y
    #    return

    # Get 8 (x,y) coordinates on the circle for more accurate collision 
    # detection. The first 4 are where the circle crosses the x/y axes. The 
    # second 4 are calculated by taking the sin and cos at 45 degree angles
    # from the center of the circle (distance is the radius).
    # coords = [top, bottom, left, right, topright, bottomright, bottomleft, topleft]
    def get_collision_coords(self):
        # Add the 4 coordinates on the x/y axes
        coords = []
        coords.append([self.circle_x, self.circle_y - self.circle_radius])
        coords.append([self.circle_x, self.circle_y + self.circle_radius])
        coords.append([self.circle_x - self.circle_radius, self.circle_y])
        coords.append([self.circle_x + self.circle_radius, self.circle_y])
        # Add the 4 different 45 degree (x,y) coordinates
        angle = 45
        right_angle = 90
        for i in range(4):
            radians = math.radians(angle)
            x = self.circle_x + (self.circle_radius * (math.cos(radians)))
            y = self.circle_y + (self.circle_radius * (math.sin(radians)))
            coords.append([x,y])
            angle += right_angle
        # Round all the coordinates to the nearest pixel
        for coord in coords:
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
        return coords

    def block_collision(self):
        # TODO what happens when blocks are hit
        return

    #def player_collision(self, player):
    #    # Player image _______________________________
    #    # Angle       [__300*_|__340*_|__20*__|__60*__]
    #    # Segments        0       1       2       3
    #    self.speed_x *= -1
    #    player.segments = player.get_player_segments()
    #    segment = player.get_segment_position(self)
    #    self.angle = self.player_deflection_angles[segment]
    #    self.radians = math.radians(self.angle)
    #    return
    def player_collision(self, player):
        if (self.speed_x > 0):
            self.speed *= -1
        self.angle = 300
        angle_offset = (player.x + player.width/2) - (self.x+self.width/2)
        self.angle -= angle_offset
        self.radians = math.radians(self.angle)
        return

    def update(self, game, player):
        if (game.level.sphere_edge_collision(self, game)):
            Sphere.sphere_list.remove(self)
            # TODO add what happens when sphere goes off bottom
            return
        if (game.level.sphere_block_collision(self, game)):
            self.block_collision()
        if (game.level.player_sphere_collision(self, player)):
            self.speed_y *= -1
            self.player_collision(player)
        self.move()
        return

#####################
#    Block Class    #
#####################
class Block:
    block_list = []
    def __init__(self, game, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width, self.height = game.get_image_size(image)
        self.top_left = (self.x, self.y)
        self.top_right = (self.x + self.width, self.y)
        self.bot_left = (self.x, self.y + self.height)
        self.bot_right = (self.x + self.width, self.y + self.height)
        self.corners = [self.top_left, self.top_right, self.bot_left, self.bot_right]
        self.fracture = False
        Block.block_list.append(self)

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))
        return

    # coords = [top, bottom, left, right, topright, bottomright, bottomleft, topleft]
    def set_block_hit_side(self, coord_index, sphere):
        if (coord_index == 0 or coord_index == 1):
            sphere.speed_y *= -1
        elif (coord_index == 2 or coord_index == 3):
            sphere.speed_x *= -1
        else:
            sphere.speed_x *= -1
            sphere.speed_y *= -1
        return

    def sphere_collision(self, sphere):
        sphere.collision_coords = sphere.get_collision_coords()
        coord_index = 0
        for coord in sphere.collision_coords:
            if (coord[0] >= self.x and coord[0] <= self.x + self.width):
                if (coord[1] >= self.y and coord[1] <= self.y + self.height):
                    self.set_block_hit_side(coord_index, sphere)
                    return True
            coord_index += 1
        return False


#####################
#    Level Class    #
#####################
class Level:
    def __init__(self, game):
        self.level = game.level_number
        self.border = self.initialize_level_blocks(game)
        self.playable_width = 600
        self.playable_height = 600
        self.background = self.get_level_background(game)
        size = self.border[0].get_size()
        self.border_width = size[0]
        self.border_height = size[1]
        self.x_left =  (game.screen_width - self.playable_width) / 2
        self.x_right = game.screen_width - self.x_left
        self.y_top = game.screen_height - self.playable_height

    def get_level_background(self, game):
        if (self.level == 1):
            background = game.bg_space        
        return background

    def draw_level_background(self, game, screen):
        #x = 0
        #y = game.level.y_top
        #screen.blit(game.level.background, (x,y))
        rect = (self.x_left, self.y_top, self.playable_width, game.screen_height)
        pygame.draw.rect(screen, (0,0,0), rect)
        return

    def initialize_level_blocks(self, game):
        if (self.level == 1):
            game_levels.initialize_level_1_blocks(game)
            border = game.fractured_gray
        return border

    @staticmethod
    def draw_blocks(screen):
        for block in Block.block_list:
            block.draw(screen)
        return

    #####################
    #  Collision Checks #
    #####################
    @staticmethod
    def player_sphere_collision(sphere, player):
        x = sphere.circle_x
        y = sphere.circle_y + sphere.circle_radius
        if (x >= player.x and x <= player.x + player.width):
            for px in range(int(sphere.speed_y)):
                if (int(y + px) == player.y):
                    return True
        return False

    @staticmethod
    def sphere_block_collision(sphere, game):
        for block in Block.block_list:
            if (block.sphere_collision(sphere)):
                Block.block_list.remove(block)
                return True
        return False

    def sphere_edge_collision(self, sphere, game):
        x = sphere.circle_x
        y = sphere.circle_y
        radius = sphere.circle_radius
        if (x < self.x_left + radius or x > self.x_right - radius):
            sphere.speed_x *= -1
            #sphere.hit_wall_sound.play()
        if (y < self.y_top + radius):
            sphere.speed_y *= -1
            #sphere.hit_wall_sound.play()
        if (y > game.screen_height - radius):
            sphere.speed_y *= -1
            #return True
        return False