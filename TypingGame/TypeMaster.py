import pygame
pygame.init()
import TitleScreen
import MenuScreen
import GameScreen
from PIL import ImageFont
import random
import Bubbles as Bub
import Buttons as But
import PlayerInput as PI
import Words as W
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

        # Flags
        self.blinking = True
        self.music_playing = False
        self.words_moving = False

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

        # Prompts/Text
        self.grade_levels = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        self.gwpm_prompt = "GWPM: "
        self.input_prompt = "Input: "
        self.menu_prompt = "Grade Level Vocabulary"
        self.score_prompt = "Score: "
        self.start_prompt = "Press Enter When Ready!"
        self.title_prompt = "Press Enter"

        # Media
        self.bg_image = pygame.image.load("Media/underwater.jpg")
        self.button_hover_sound = pygame.mixer.Sound("Media/bubble.ogg")
        self.game_music = "Media/gameMusic1.mp3"
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
        self.grade_1st_hovering = pygame.image.load("Media/1st_grade_hovering.png")
        self.grade_2nd_hovering = pygame.image.load("Media/2nd_grade_hovering.png")
        self.grade_3rd_hovering = pygame.image.load("Media/3rd_grade_hovering.png")
        self.grade_4th_hovering = pygame.image.load("Media/4th_grade_hovering.png")
        self.grade_5th_hovering = pygame.image.load("Media/5th_grade_hovering.png")
        self.grade_6th_hovering = pygame.image.load("Media/6th_grade_hovering.png")
        self.grade_7th_hovering = pygame.image.load("Media/7th_grade_hovering.png")
        self.grade_8th_hovering = pygame.image.load("Media/8th_grade_hovering.png")
        self.menu_header = pygame.image.load("Media/menu_prompt.png")
        self.mute_image = pygame.image.load("Media/mute.png")
        self.pause_image = pygame.image.load("Media/pause.png")
        self.speed_image = pygame.image.load("Media/speed.png")
        self.mute_hovering = pygame.image.load("Media/mute_hovering.png")
        self.pause_hovering = pygame.image.load("Media/pause_hovering.png")
        self.speed_up_hovering = pygame.image.load("Media/speed_up_hovering.png")
        self.speed_down_hovering = pygame.image.load("Media/speed_down_hovering.png")
        self.speed_up = pygame.image.load("Media/speed_up.png")
        self.speed_down = pygame.image.load("Media/speed_down.png")
        self.title_music = "Media/titleScreenMusic.mp3"
        self.title_text = pygame.image.load("Media/title_image.png")
        self.right_corner = pygame.image.load("Media/bubbles/right_bubble.png")
        self.left_corner = pygame.image.load("Media/bubbles/left_bubble.png")
        self.game_button_left = pygame.image.load("Media/bubbles/game_button_left.png")
        self.game_button_right = pygame.image.load("Media/bubbles/game_button_right.png")
        self.speed_change = pygame.image.load("Media/bubbles/speed_change.png")
        self.game_menu_top_left = pygame.image.load("Media/bubbles/game_menu_top_left.png")
        self.game_menu_top_right = pygame.image.load("Media/bubbles/game_menu_top_right.png")



        self.test = pygame.image.load("Media/test.png")
        self.test_hovering = pygame.image.load("Media/test_hover.png")








        # Menu Parameters
        self.x_menu_col_1 = self.screenW / 4
        self.x_menu_col_2 = self.screenW / 4 * 2
        self.x_menu_col_3 = self.screenW / 4 * 3
        self.x_menu_col_3a = self.screenW / 3
        self.x_menu_col_3b = self.screenW / 3 * 2
        self.y_menu_col_1 = self.screenH / 4
        self.y_menu_col_2 = self.screenH / 4 * 2
        self.y_menu_col_3 = self.screenH / 4 * 3


    #####################
    #      Getters      #
    ##################### 
    def get_word_object(self, word):
        return W.Word(self, word)

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
    def draw_buttons(self, screen):
        for button in But.Button.buttons:
            button.draw(screen, self)
        return
    
    def draw_bg_image(self, screen):
        screen.blit(self.bg_image, (0,0))
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
        for bubble in Bub.Bubbles.bubble_array:
            if not (bubble.draw(screen, self)):
                if (bubble.pop_bubble(screen)):
                    Bub.Bubbles.bubble_array.remove(bubble)
        Bub.Bubbles.update_bubbles(self, self)
        return


    #####################
    #   Event Handling  #
    #####################
    def quit_game(self):
        pygame.quit()
        sys.exit(0)

    def play_music(self, music):
        music = pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        self.music_playing = True
        return

    def check_frame_count(self):
        if (self.frame_count >= self.max_FPS):
            self.frame_count = 0
            self.seconds += 1
            self.add_word_seconds += 1
        return

    def check_quick_frame_count(self):
        max_FPS_fraction = self.max_FPS * self.add_word_delay
        if (self.quick_frame_count == max_FPS_fraction):
            self.quick_frame_count = 0
            return True
        self.quick_frame_count += 1
        return False

    def blink_text(self, screen, text, start_screen):
        if (self.update_seconds(self.text_blink_delay)):
            if (self.blinking):
                self.blinking = False
            else:
                self.blinking = True
        if (self.blinking):
            self.draw_blink_text(screen, text, start_screen)
        return

    def update_seconds(self, delay):
        self.frame_tracker += 1
        if (self.frame_tracker == (self.max_FPS * delay)):
            self.frame_tracker = 0
            self.seconds += 1
            return True
        return False

    def add_word_bubble(self, word, screen):
        image_size = self.menu_header.get_size()
        y_offset = word.y - image_size[1] / 2
        Bub.Bubbles.bubble_array.append(Bub.Bubbles(self, True, word.x, y_offset))
        return

    def pop_word_bubbles(self, screen):
        for bubble in Bub.Bubbles.bubble_array:
            if (bubble.pop_bubble(screen)):
                Bub.Bubbles.bubble_array.remove(bubble)
        return


#####################
#        Main       #
#####################
def main():
    game = Game()
    screen = game.set_screen()
    game.set_player_input()

    TitleScreen.title_screen(screen, game)
    MenuScreen.menu_screen(screen, game)
    TitleScreen.start_screen(screen, game)
    GameScreen.play(screen, game)

if __name__ == "__main__":
    main()