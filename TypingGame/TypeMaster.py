import pygame
pygame.init()
import GameScreen
from PIL import ImageFont
import random
import Bubbles as Bub
import Buttons as But
import EventHandling as Events
import PlayerInput as PI
import sys


#####################
#     Game Class    #
#####################
class Game():   
    def __init__(self):
        # Window
        self.border_width = 2
        self.bottom_boxH = 35
        self.screenW = 950
        self.screenH = 600
        self.title = "Type Master"
        self.top_padding = 100

        # Fonts/Colors
        self.button_color = (44, 150, 199)
        self.button_hover_color = (194,178,128)
        self.button_text_color = (255,255,255)
        self.font_size = 20
        self.master_font = "Media/ariblk.ttf"
        self.text_color = (255,255,255)
        self.font = ImageFont.truetype(self.master_font, self.font_size)
        self.word_font = pygame.font.Font(self.master_font, self.font_size)

        # Buttons
        self.button_spacing = 10
        self.buttonW = 150
        self.buttonH = 75
        self.menu_buttonH = 50
        self.menu_buttonW = 100

        # Important Variables
        self.word_delay_score_multiplier = 1.0
        self.up_or_down = -1 # -1 for words up 1 for words down
        self.add_word_seconds = 0
        self.add_word_delay_default = 3.0
        self.add_word_delay = 3.0
        self.add_words_trigger = 3
        self.word_delay_low_cap = 10
        self.word_delay_high_cap = .25
        self.max_word_speed = 1
        self.text_blink_delay = .5
        self.player_score = 0
        self.clock = pygame.time.Clock()
        self.is_paused = False

        # Flags
        self.blinking = True
        self.music_playing = False
        self.words_moving = False
        self.pause_screen_drawn = False
        self.pause_bubbles_drawn = False

        # Word Handling
        self.avg_word_length = 0
        self.characters_typed = 0
        self.current_words = [""]
        self.gross_words_per_min = 0
        self.wordbank = [""]

        # HUD Variables
        self.left_corner_x_offset = .15
        self.right_corner_x_offset = .85
        self.bubble_y_offset = .42
        self.input_width = 0
        self.button_padding = 10

        # Frames
        self.bubble_frame_count = 0
        self.frame_count = 0
        self.frame_tracker = 0
        self.quick_frame_count = 0
        self.max_FPS = 40
        self.seconds = 1

        # Input Handling
        self.input_left_padding = 20
        self.player_input = None
        self.player_input_obj = None

        # Menu Parameters
        self.x_menu_col_1 = self.screenW / 4
        self.x_menu_col_2 = self.screenW / 4 * 2
        self.x_menu_col_3 = self.screenW / 4 * 3
        self.x_menu_col_3a = self.screenW / 3
        self.x_menu_col_3b = self.screenW / 3 * 2
        self.y_menu_col_1 = self.screenH / 4
        self.y_menu_col_2 = self.screenH / 4 * 2
        self.y_menu_col_3 = self.screenH / 4 * 3

        # Prompts/Text
        self.grade_levels = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        self.gwpm_prompt = "GWPM: "
        self.input_prompt = "Input: "
        self.menu_prompt = "Grade Level Vocabulary"
        self.score_prompt = "Score: "
        self.start_prompt = "Press Enter When Ready!"
        self.title_prompt = "Press Enter"

        # Game Media
        self.bg_image = pygame.image.load("Media/underwater.jpg")
        self.pause_bg = pygame.image.load("Media/underwater.jpg")
        self.title_text = pygame.image.load("Media/title_image.png")
        self.right_corner = pygame.image.load("Media/bubbles/right_bubble.png")
        self.left_corner = pygame.image.load("Media/bubbles/left_bubble.png")
        self.game_button_left = pygame.image.load("Media/bubbles/game_button_left.png")
        self.game_button_right = pygame.image.load("Media/bubbles/game_button_right.png")
        self.speed_change = pygame.image.load("Media/bubbles/speed_change.png")

        # Sound Media
        self.button_hover_sound = pygame.mixer.Sound("Media/bubble.ogg")
        self.game_music = "Media/gameMusic1.mp3"
        self.title_music = "Media/titleScreenMusic.mp3"

        # Button Media
        self.menu_header = pygame.image.load("Media/menu_prompt.png")
        self.mute_image = pygame.image.load("Media/mute.png")
        self.pause_image = pygame.image.load("Media/pause.png")
        self.speed_image = pygame.image.load("Media/speed.png")
        self.speed_up = pygame.image.load("Media/speed_up.png")
        self.speed_down = pygame.image.load("Media/speed_down.png")
        self.grade_1st = pygame.image.load("Media/1st_grade.png")
        self.grade_2nd = pygame.image.load("Media/2nd_grade.png")
        self.grade_3rd = pygame.image.load("Media/3rd_grade.png")
        self.grade_4th = pygame.image.load("Media/4th_grade.png")
        self.grade_5th = pygame.image.load("Media/5th_grade.png")
        self.grade_6th = pygame.image.load("Media/6th_grade.png")
        self.grade_7th = pygame.image.load("Media/7th_grade.png")
        self.grade_8th = pygame.image.load("Media/8th_grade.png")
        self.all_vocab = (
            self.grade_1st, 
            self.grade_2nd, 
            self.grade_3rd, 
            self.grade_4th, 
            self.grade_5th, 
            self.grade_6th, 
            self.grade_7th, 
            self.grade_8th
        )

        # Button Hover Media
        self.grade_1st_hovering = pygame.image.load("Media/1st_grade_hovering.png")
        self.grade_2nd_hovering = pygame.image.load("Media/2nd_grade_hovering.png")
        self.grade_3rd_hovering = pygame.image.load("Media/3rd_grade_hovering.png")
        self.grade_4th_hovering = pygame.image.load("Media/4th_grade_hovering.png")
        self.grade_5th_hovering = pygame.image.load("Media/5th_grade_hovering.png")
        self.grade_6th_hovering = pygame.image.load("Media/6th_grade_hovering.png")
        self.grade_7th_hovering = pygame.image.load("Media/7th_grade_hovering.png")
        self.grade_8th_hovering = pygame.image.load("Media/8th_grade_hovering.png")
        self.mute_hovering = pygame.image.load("Media/mute_hovering.png")
        self.speed_up_hovering = pygame.image.load("Media/speed_up_hovering.png")
        self.speed_down_hovering = pygame.image.load("Media/speed_down_hovering.png")



    #####################
    #      Getters      #
    ##################### 
    def get_menu_buttons(self):
        return But.Button.get_menu_buttons(self)

    def get_game_buttons(self):
        return But.Button.get_game_buttons(self)

    def get_num_buttons(self):
        return But.Button.num_buttons

    def get_score_text_size(self, score, return_flag=None):
        convert_text = str(score) + str(self.border_width)
        text = self.score_prompt + convert_text
        width_height = self.font.getsize(text)
        if (return_flag == "width"):
            return width_height[0]
        elif (return_flag == "height"):
            return width_height[1]
        return width_height[0], width_height[1]

    def get_bottom_offset(self, text, score=""):
        text_height = self.get_score_text_size(score, "height")
        input_box_text_offset = (self.bottom_boxH - text_height) // 2
        borders_offset = (self.border_width * 3)
        screenH_offset = self.screenH - text_height
        bottom_offset = screenH_offset - borders_offset - input_box_text_offset
        return bottom_offset

    def get_right_offset(self, score=""):
        text_width = self.get_score_text_size(score, "width")
        right_offset = self.screenW - self.buttonW - text_width
        return right_offset


    #####################
    #      Setters      #
    #####################
    def set_player_input(self):
        self.player_input_obj = PI.PlayerInput(self)
        return

    def set_screen(self):
        pygame.display.set_caption(self.title)
        return (pygame.display.set_mode((self.screenW, self.screenH)))

    def reset_buttons(self):
        But.Button.buttons.clear()
        return

    def set_game_speed_up(self):
        # Decrease the word delay
        if (self.add_word_delay > 1.0):
            self.add_word_delay -= 1.0
        elif (self.add_word_delay == .25):
            pass
        else:
            self.add_word_delay -= .25

        # Increase score multiplier
        if (self.word_delay_score_multiplier == 6.0):
            pass
        elif (self.word_delay_score_multiplier >= 1.0):
            self.word_delay_score_multiplier += 1.0
        else:
            self.word_delay_score_multiplier += .1
        self.word_delay_score_multiplier = round(self.word_delay_score_multiplier, 2)
        return

    def set_game_speed_down(self):
        # Increase word delay
        if (self.add_word_delay == 10):
            pass
        elif (self.add_word_delay >= 1.0):
            self.add_word_delay += 1.0
        else:
            self.add_word_delay += .25

        # Decrease score multiplier
        if (self.word_delay_score_multiplier == .3):
            pass
        elif (self.word_delay_score_multiplier <= 1.0):
            self.word_delay_score_multiplier -= .1
        else:
            self.word_delay_score_multiplier -= 1.0
        self.word_delay_score_multiplier = round(self.word_delay_score_multiplier, 2)
        return


    #####################
    #      Drawing      #
    #####################
    def draw_buttons(self, screen, game_button=False):
        for button in But.Button.buttons:
            button.draw(screen, self)
            if (game_button):
                Bub.Bubbles.draw_button_bubble(button, screen, self)
        return
    
    def draw_bg_image(self, screen):
        screen.blit(self.bg_image, (0,0))
        return

    def draw_corner_bubbles(self, screen):
        Bub.Bubbles.draw_corner_bubble(screen, self)
        Bub.Bubbles.draw_corner_bubble(screen, self, True)
        return
   
    def draw_blink_text(self, screen, text, start_screen):
        font_size = self.font.getsize(text)
        x = ((self.screenW / 2) - (font_size[0] / 2))
        if (start_screen):
            y = (self.screenH / 2) - (font_size[1] / 2)
        else:
            y = ((self.screenH / 2) - (font_size[1] / 2) + self.top_padding)
        text = self.word_font.render(text, 1, self.text_color)
        screen.blit(text, (x,y))
        return

    def draw_bubbles(self, screen):
        Bub.Bubbles.draw_bubbles(self, self, screen)
        return


    #####################
    #   Event Handling  #
    #####################
    def quit_game(self):
        Events.quit_game()

    def play_music(self, music):
        Events.play_music(self, music)
        return

    def add_word_bubble(self, word, screen):
        Bub.Bubbles.add_word_bubble(self, word, screen)
        return

    def pop_word_bubbles(self, screen):
        Bub.Bubbles.pop_word_bubbles(screen)
        return

    def blink_text(self, screen, text, start_screen):
        Events.blink_text(self, screen, text, start_screen)
        return

    def check_frame_count(self):
        Events.check_frame_count(self)
        return

    def check_quick_frame_count(self):
        status = Events.check_quick_frame_count(self)
        return status

    def update_seconds(self, delay):
        status = Events.update_seconds(self, delay)
        return status

    def check_game_events(self, buttons):
        status = Events.check_game_events(self, buttons)
        return status

    def check_menu_events(self, buttons):
        status = Events.check_menu_events(self, buttons)
        return status

    def check_title_events(self):
        status = Events.check_title_events(self)
        return status


#####################
#    Menu Screen    #
#####################
def draw_menu_header(screen, game):
    image_size = game.menu_header.get_size()
    x = (game.screenW - image_size[0]) / 2
    y = 0
    screen.blit(game.menu_header, (x,y))
    return

def draw_menu(screen, game, buttons):
    index = 0
    for button in buttons:
        screen.blit(game.all_vocab[index], (button.x, button.y))
        index += 1     
    return

def draw_menu_screen(screen, game, buttons):
    game.frame_count += 1
    game.draw_bg_image(screen)
    game.draw_bubbles(screen)
    draw_menu_header(screen, game)
    draw_menu(screen, game, buttons)
    game.draw_buttons(screen)
    pygame.display.update()
    game.check_frame_count()
    return

def menu_screen(screen, game):
    buttons = game.get_menu_buttons()
    while(True):
        game.clock.tick(game.max_FPS)
        if (game.check_menu_events(buttons)):
            break
        draw_menu_screen(screen, game, buttons)
    game.reset_buttons()
    game.frame_count = 0
    return


#####################
#    Title/Start    #
#####################
def draw_title(screen, game):
    text_size = game.title_text.get_size()
    x = (game.screenW - text_size[0]) / 2
    y = game.top_padding
    screen.blit(game.title_text, (x,y))
    return

def draw_screen(screen, game, start_screen=False):
    game.clock.tick(game.max_FPS)
    game.frame_count += 1
    game.draw_bg_image(screen)
    if (start_screen):
        game.blink_text(screen, game.start_prompt, start_screen)
    else:
        draw_title(screen, game)
        game.blink_text(screen, game.title_prompt, start_screen)
    game.draw_bubbles(screen)
    pygame.display.update()
    game.check_frame_count()
    return

def title_screen(screen, game):
    game.play_music(game.title_music)
    while (True):
        if (game.check_title_events()):
            break
        draw_screen(screen, game)
    return

def start_screen(screen, game):
    while (True):
        if (game.check_title_events()):
            game.words_moving = True
            break
        draw_screen(screen, game, True)
    return


#####################
#        Main       #
#####################
def main():
    game = Game()
    screen = game.set_screen()
    game.set_player_input()
    game.pause_bg.set_alpha(200)

    title_screen(screen, game)
    menu_screen(screen, game)
    start_screen(screen, game)
    GameScreen.play(screen, game)

if __name__ == "__main__":
    main()