import pygame
import random
import Words


#####################
#      Getters      #
##################### 
def get_words_per_min(game):
    one_min = 60
    gwpm = str(game.gross_words_per_min)
    average_chars = game.characters_typed / game.avg_word_length
    average_time = game.seconds / one_min
    gwpm = round(average_chars / average_time)
    return gwpm

def get_gwpm_text_size(game):
    gwpm = str(game.gross_words_per_min)
    text_string = game.gwpm_prompt + str(gwpm)
    text_size = game.font.getsize(text_string)
    text = game.word_font.render(text_string, 1, game.text_color)
    return text, text_size[0]

def get_stopwatch_string(game):
    game_seconds = game.seconds
    seconds = game_seconds % 60
    mins = game_seconds // 60
    hours = game_seconds // 60 // 60
    if (hours > 0):
        stopwatch = (f"{hours:02}:{mins:02}:{seconds:02}")
    elif (mins > 0):
        stopwatch = (f"{mins:02}:{seconds:02}")
    else:
        stopwatch = (f"{seconds:02}")
    return stopwatch

def get_stopwatch_location(game, text_size):
    char_size = game.font.getsize("0")
    bubble_size = game.right_corner.get_size()
    x = 0 + (bubble_size[0] * game.right_corner_x_offset) / 2
    x -= text_size[0] / 2 + char_size[0]
    y = game.screenH - game.bottom_boxH * 2
    return x, y

def get_score_multiplier_location(text_size, game):
    char_size = game.font.getsize("0")
    image_size = game.right_corner.get_size()
    x = game.screenW - (image_size[0] * game.right_corner_x_offset) / 2
    x -= text_size[0] / 2 - char_size[0]
    y = game.screenH - game.bottom_boxH * 2
    return x, y

def add_word(game):
    new_word = random.choice(game.wordbank)
    game.current_words.append(new_word)
    return


#####################
#   Event Handling  #
#####################

def continue_game(screen, game):
    if (len(game.current_words) < game.add_words_trigger):
        game.current_words.append(random.choice(game.wordbank))
    if (game.add_word_delay < 1):
        if (game.check_quick_frame_count()):
            add_word(game)
    elif (game.add_word_seconds >= game.add_word_delay):
        game.quick_frame_count = 0
        add_word(game)
        game.add_word_seconds = 0
    Words.Word.word_str_to_obj(game)
    Words.remove_words_from_screen(screen, game)
    Words.move_words(screen, game)
    game.pop_word_bubbles(screen)
    pygame.display.update()
    return


#####################
#      Drawing      #
#####################
def draw_input_text(screen, game):
    player_input = game.player_input_obj.get_surface()
    size = game.player_input_obj.input_size
    x = game.screenW / 2 - size[0] / 2
    y = game.get_bottom_offset(game.score_prompt) + game.border_width
    screen.blit(player_input, (x,y))
    return

def draw_elapsed_time(screen, game):
    text_string = get_stopwatch_string(game)
    text_size = game.font.getsize(text_string)
    text = game.word_font.render(text_string, 1, game.text_color)
    x, y = get_stopwatch_location(game, text_size)
    screen.blit(text, (x,y))
    return

def draw_words_per_min(screen, game):
    if (game.characters_typed != 0 and game.seconds != 0):
        gwpm = get_words_per_min(game)
        game.gross_words_per_min = gwpm
    text, text_width = get_gwpm_text_size(game)
    x = 0 + game.input_left_padding
    y = game.get_bottom_offset(game.player_score)
    screen.blit(text, (x,y))
    draw_elapsed_time(screen, game)
    return

def draw_score_multiplier(screen, game):
    score_mult = game.word_delay_score_multiplier # TODO add functionality for correct words in a row
    text_string = "x " + str(score_mult)
    text = game.word_font.render(text_string, 1, game.text_color)
    text_size = game.font.getsize(text_string)
    x, y = get_score_multiplier_location(text_size, game)
    screen.blit(text, (x,y))
    return

def draw_score_text(screen, game):
    text_string = game.score_prompt + str(game.player_score)
    text = game.word_font.render(text_string, 1, game.text_color)
    right_offset = game.get_right_offset(game.player_score)
    x = right_offset + game.buttonW
    y = game.get_bottom_offset(game.player_score)
    screen.blit(text, (x,y))
    return

def draw_input_top(screen, game):
    image_size = game.right_corner.get_size()
    x_start = 0 + image_size[0] * .75
    x_end = game.screenW - image_size[0] * .75
    game.input_width = x_end - x_start
    y = game.screenH - game.bottom_boxH
    pygame.draw.line(screen, game.text_color, (x_start,y), (x_end,y), game.border_width)
    return

def draw_words(screen, game):
    for word in game.current_words:
        text = game.word_font.render(word.word, 1, word.text_color)
        screen.blit(text, (word.x, word.y))
    return

def draw_game_screen(screen, game, buttons):
    game.draw_bg_image(screen)
    draw_words(screen, game)
    game.draw_corner_bubbles(screen)
    draw_input_top(screen, game)
    draw_score_text(screen, game)
    draw_words_per_min(screen, game)
    draw_input_text(screen, game)
    if (game.is_paused):
        screen.blit(game.pause_bg, (0,0))
        game.draw_buttons(screen, True)
    draw_score_multiplier(screen, game)
    pygame.display.update()
    return


#####################
#    Game Screen    #
#####################

def play(screen, game):
    game.play_music(game.game_music)
    buttons = game.get_game_buttons()
    game.seconds = 0
    while(True):
        game.clock.tick(game.max_FPS)
        game.frame_count += 1
        if not (game.check_game_events(buttons)):
            break
        if (game.words_moving):
            continue_game(screen, game)
            game.check_frame_count()
        draw_game_screen(screen, game, buttons)
    game.reset_buttons()
    return