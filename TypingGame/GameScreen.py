import pygame
import random



def check_buttons(game, button):
    if (button.text == "Start"):
        game.start_game(button)
    elif (button.text == "Pause"):
        game.toggle_pause()
    elif (button.text == "Mute"):
        game.toggle_mute()
    return

def check_mouse_position(mouse_position, buttons, game):
    for button in buttons:
        if (button.is_over(mouse_position)):
            button.color = game.button_hover_color
            button.text_color = game.button_text_color
            button.hovering = True
            if (button.play_sound):
                game.button_hover_sound.play()
                button.play_sound = False
        else:
            button.color = game.button_color
            button.text_color = game.button_text_color
            button.hovering = False
            button.play_sound = True
    return

def check_button_clicked(mouse_position, buttons, game):
    for button in buttons:
        if (button.is_over(mouse_position)):
            check_buttons(game, button)
    return

def check_events(game, buttons):
    mouse_position = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
            game.quit_game()      
        elif (event.type == pygame.KEYDOWN):
            pass
        elif (event.type == pygame.MOUSEMOTION):
            check_mouse_position(mouse_position, buttons, game)
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            check_button_clicked(mouse_position, buttons, game)
    game.update_player_input(events)
        # TODO add functionality to return false and break the loop
    return True
           
def remove_words_from_screen(game):
    if (game.player_input):
        player_input = game.player_input.split(' ')
        for word in game.current_words:
            for player_word in player_input:
                if (player_word == word.word):
                    game.player_score += len(word.word)
                    game.characters_typed += len(word.word) + 1
                    game.current_words.remove(word)
    return

def check_word_count(game):
    if (len(game.current_words) < game.add_words_trigger):
        words_to_add = game.add_words_trigger - len(game.current_words)
        for i in range(words_to_add):
            game.current_words.append(random.choice(game.wordbank))
    return

def word_str_to_obj(game):
    new_words = []
    for word in game.current_words:
        if (type(word) is str):
            new_words.append(game.get_word_object(word))
        else:
            new_words.append(word)
    game.current_words = new_words
    return

def move_words(game):
    for word in game.current_words:
        try:
            position = word.y + word.falling_speed
            if (position < game.screen_gameH - word.height):
                word.y += word.falling_speed
            else:
                game.player_score -= len(word.word)
                game.current_words.remove(word)
        except AttributeError:
            break
    return
    
def draw_game_screen(screen, game, buttons):
    game.draw_bg_image(screen)
    game.draw_words(screen)
    game.draw_buttons(screen, game)
    game.draw_input_box(screen)
    game.draw_input_text(screen)
    game.draw_score_text(screen)
    game.draw_words_per_min(screen)
    game.draw_input(screen)
    pygame.display.update()
    return

def play(screen, game):
    game.play_music(game.game_music)
    buttons = game.get_game_buttons()
    while(True):
        game.clock.tick(game.max_FPS)
        game.frame_count += 1
        if not (check_events(game, buttons)):
            break
        if (game.words_falling):
            check_word_count(game)
            if (game.update_seconds(game.seconds_delay)):
                game.add_word()
            word_str_to_obj(game)
            remove_words_from_screen(game)
            move_words(game)
            pygame.display.update()
        draw_game_screen(screen, game, buttons)
        game.check_frame_count()
    game.clear_current_buttons()
    return
