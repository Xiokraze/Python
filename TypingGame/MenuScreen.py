import pygame
import Wordbanks


#####################
#   Event Handling  #
#####################
def check_mouse_position(game, mouse_position, button):
    if (button.is_over(mouse_position)):
        button.color = game.button_hover_color
        button.textColor = game.button_text_color
        button.hovering = True
        if (button.play_sound):
            game.button_hover_sound.play()
            button.play_sound = False
    else:
        button.color = game.button_color
        button.textColor = game.button_text_color
        button.hovering = False
        button.play_sound = True
    return

def check_button(game, button):
    if (button.text == "1st"):
        game.wordbank = Wordbanks.vocab1stGrade
    elif (button.text == "2nd"):
        game.wordbank = Wordbanks.vocab2ndGrade
    elif (button.text == "3rd"):
        game.wordbank = Wordbanks.vocab3rdGrade
    elif (button.text == "4th"):
        game.wordbank = Wordbanks.vocab4thGrade
    elif (button.text == "5th"):
        game.wordbank = Wordbanks.vocab5thGrade
    elif (button.text == "6th"):
        game.wordbank = Wordbanks.vocab6thGrade
    elif (button.text == "7th"):
        game.wordbank = Wordbanks.vocab7thGrade
    elif (button.text == "8th"):
        game.wordbank = Wordbanks.vocab8thGrade
    if (game.wordbank != None):
        return True
    return False

def check_events(game, buttons):
    mouse_position = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
                    game.quit_game()
        elif (event.type == pygame.MOUSEMOTION):
            for button in buttons:
                check_mouse_position(game, mouse_position, button)
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            for button in buttons:
                if (button.is_over(mouse_position)):
                    if (check_button(game, button)):
                        return True
    return False


#####################
#      Drawing      #
#####################
def draw_menu_header(screen, game):
    text_size = game.menu_header.get_size()
    x = (game.screenW - text_size[0]) / 2
    y = 0
    screen.blit(game.menu_header, (x,y))
    return

def draw_menu_screen(screen, game):
    game.frame_count += 1
    game.draw_bg_image(screen)
    game.draw_bubbles(screen, game)
    draw_menu_header(screen, game)
    game.draw_buttons(screen, game)
    pygame.display.update()
    game.check_frame_count()
    return


#####################
#    Menu Screen    #
#####################
def play(screen, game):
    buttons = game.get_menu_buttons()
    while(True):
        game.clock.tick(game.max_FPS)
        if (check_events(game, buttons)):
            break
        draw_menu_screen(screen, game)
    game.clear_current_buttons()
    game.frame_count = 0
    return
