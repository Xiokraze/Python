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

class Game():   
    def __init__(self):
        # Window
        self.title = "Type Master"
        self.screenW = 950
        self.screenH = 600
        self.top_padding = 100
        self.bottom_boxH = 35
        self.screen_gameH = self.screenH - self.bottom_boxH
        self.border_width = 2
        self.player_score = 0
        self.clock = pygame.time.Clock()

        # Font
        self.master_font = "Media/ariblk.ttf"
        self.font_size = 20
        self.text_color = (255,255,255)
        self.button_color = (44, 150, 199)
        self.button_text_color = (255,255,255)
        self.button_hover_color = (194,178,128)
        self.font = ImageFont.truetype(self.master_font, self.font_size)
        self.word_font = pygame.font.Font(self.master_font, self.font_size)

        # Buttons
        self.buttonW = 150
        self.buttonH = 75
        self.menu_buttonW = 100
        self.menu_buttonH = 50
        self.button_spacing = 10

        # Variables
        self.music_playing = False
        self.blinking = True
        self.text_blink_delay = .5
        self.seconds_delay = 1
        self.wordbank = [""]
        self.current_words = [""]
        self.max_y_speed = 2
        self.player_input = None
        self.player_input_obj = None
        self.characters_typed = 0
        self.gross_words_per_min = 0
        self.add_words_trigger = 3
        self.words_falling = False

        # Frames
        self.max_FPS = 40
        self.frame_count = 0
        self.frame_tracker = 0
        self.bubble_frame_count = 0
        self.seconds = 1

        # Input Box
        self.input_left_padding = 20

        # Prompts/Text
        self.grade_levels = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        self.title_prompt = "Press Enter"
        self.start_prompt = "Press Enter To Begin!"
        self.score_prompt = "Score: "
        self.input_prompt = "Input: "
        self.menu_prompt = "Grade Level Vocabulary"
        self.gwpm_prompt = "GWPM: "

        # Media
        self.bg_image = pygame.image.load("Media/underwater.jpg")
        self.title_text = pygame.image.load("Media/title_image.png") 
        self.title_music = "Media/titleScreenMusic.mp3"
        self.game_music = "Media/gameMusic1.mp3"
        self.button_hover_sound = pygame.mixer.Sound("Media/bubble.ogg")
        self.pause_image = pygame.image.load("Media/pause.png")
        self.mute_image = pygame.image.load("Media/mute.png")


    # PlayerInput
    def set_player_input(self):
        self.player_input_obj = PI.PlayerInput(self)
        return

    def update_player_input(self, events):
        if (self.player_input_obj.update(events)):
            self.player_input = self.player_input_obj.get_text()
            self.player_input_obj.reset_input_text()
        return

    def quit_game(self):
        pygame.quit()
        sys.exit(0)

    def get_screen(self):
        pygame.display.set_caption(self.title)
        return (pygame.display.set_mode((self.screenW, self.screenH)))

    def get_word_object(self, word):
        return W.Word(self, word)

    def get_menu_buttons(self):
        return But.Button.get_menu_buttons(self)

    def get_game_buttons(self):
        return But.Button.get_game_buttons(self)

    def get_menu_button_x(self):
        x = self.screenW - self.buttonW - (self.border_width * 2)
        return x

    def get_menu_button_y(self):
        convert_text = str(self.player_score) + str(self.border_width)
        textH = self.font.getsize(self.score_prompt + convert_text)
        bottom_padding = self.screenH - textH[1] - self.border_width * 3 - ((self.bottom_boxH - textH[1]) // 2)
        y = bottom_padding - self.buttonH - (self.border_width * 3)
        return y

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
        screen_height_offset = self.screenH - text_height
        bottom_offset = screen_height_offset - borders_offset - input_box_text_offset
        return bottom_offset

    def get_right_offset(self, score=""):
        text_width = self.get_score_text_size(score, "width")
        right_offset = self.screenW - self.buttonW - text_width
        return right_offset

    def play_music(self, music):
        music = pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        self.music_playing = True
        return
    
    def update_seconds(self, delay):
        self.frame_tracker += 1
        if (self.frame_tracker == (self.max_FPS * delay)):
            self.frame_tracker = 0
            self.seconds += 1
            return True
        return False
    
    def blink_text(self, screen, text, start_screen):
        font_size = self.font.getsize(text)
        x = ((self.screenW / 2) - (font_size[0] / 2))
        if (start_screen):
            y = (self.screenH / 2) - (font_size[1] / 2)
        else:
            y = ((self.screenH / 2) - (font_size[1] / 2) + self.top_padding)
        text = self.word_font.render(text, 1, self.text_color)
        screen.blit(text, (x,y))
        return

    def clear_current_buttons(self):
        But.Button.buttons.clear()
        return

    def add_word(self):
        new_word = random.choice(self.wordbank)
        self.current_words.append(new_word)
        return

    def check_frame_count(self):
        if (self.frame_count == self.max_FPS):
            self.frame_count = 0
        return

    # Button Checks
    def start_game(self, button):
        self.words_falling = True
        button.visible = True
        return

    def toggle_mute(self):
        if (self.music_playing):
            pygame.mixer.music.pause()
            self.music_playing = False
        else:
            pygame.mixer.music.unpause()
            self.music_playing = True
        return

    def toggle_pause(self):
        if (self.words_falling):
            self.words_falling = False
        else:
            self.words_falling = True
        return

    # Drawing   
    def draw_bg_image(self, screen):
        screen.blit(self.bg_image, (0,0))
        return
    
    def draw_text_blink(self, screen, text, start_screen):
        if (self.update_seconds(self.text_blink_delay)):
            if (self.blinking):
                self.blinking = False
            else:
                self.blinking = True
        if (self.blinking):
            self.blink_text(screen, text, start_screen)
        return
    
    def draw_title(self, screen):
        text_size = self.title_text.get_size()
        x = (self.screenW - text_size[0]) / 2
        y = self.top_padding
        screen.blit(self.title_text, (x,y))
        return

    def draw_menu_header(self, screen, game):
        text_size = self.font.getsize(self.menu_prompt)
        x = self.screenW / 2 - text_size[0] / 2 + self.border_width / 2
        text = self.word_font.render(self.menu_prompt, 1, self.text_color)
        screen.blit(text, (x, 0))
        return

    def draw_bubbles(self, screen, game):
        for bubble in Bub.Bubbles.bubble_array:
            if not (bubble.draw(screen, game)):
                if (bubble.pop_bubble(screen)):
                    Bub.Bubbles.bubble_array.remove(bubble)
        Bub.Bubbles.update_bubbles(self, game)
        return

    def draw_buttons(self, screen, game):
        for button in But.Button.buttons:
            button.draw(screen, game)
        return

    def draw_words(self, screen):
        for word in self.current_words:
            text = self.word_font.render(word.word, 1, word.text_color)
            screen.blit(text, (word.x, word.y))
            #except: # TODO why did I put this here lol
            #    break
        return

    def draw_input_box(self, screen):
        left_border = 0
        top_border = self.screenH - self.bottom_boxH - self.border_width
        right_border = self.screenW - self.border_width + 1
        bottom_border = self.bottom_boxH
        box = (left_border, top_border, right_border, bottom_border)
        pygame.draw.rect(screen, self.text_color, box, self.border_width)
        return

    def draw_input_text(self, screen):
        text = self.word_font.render(self.input_prompt, 1, self.text_color)
        x = self.input_left_padding
        y = self.get_bottom_offset(self.player_score)
        screen.blit(text, (x, y))
        return

    def draw_score_text(self, screen):
        text_string = self.score_prompt + str(self.player_score)
        text = self.word_font.render(text_string, 1, self.text_color)
        right_offset = self.get_right_offset(self.player_score)
        x = right_offset + self.buttonW
        y = self.get_bottom_offset(self.player_score)
        screen.blit(text, (x,y))
        return

    def draw_words_per_min(self, screen):
        gwpm = str(self.gross_words_per_min)
        if (self.characters_typed != 0 and self.seconds != 0):
            #TODO add tracking for actual average word length typed
            average_chars = self.characters_typed / 5
            average_time = self.seconds / 60
            gwpm = round(average_chars / average_time)
        text_string = self.gwpm_prompt + str(gwpm)
        text_size = self.font.getsize(text_string)
        text = self.word_font.render(text_string, 1, self.text_color)
        x = (self.screenW // 2) - (text_size[0] / 2)
        y = self.get_bottom_offset(self.player_score)
        screen.blit(text, (x,y))
        return

    def draw_input(self, screen):
        player_input = self.player_input_obj.get_surface()
        text_width = self.font.getsize(self.input_prompt)
        x = self.input_left_padding + text_width[0]
        y = self.get_bottom_offset(self.input_prompt)
        screen.blit(player_input, (x,y))
        return


def main():
    game = Game()
    screen = game.get_screen()
    game.set_player_input()

    TitleScreen.play(screen, game)
    MenuScreen.play(screen, game)
    TitleScreen.start_screen(screen, game)
    GameScreen.play(screen, game)

if __name__ == "__main__":
    main()