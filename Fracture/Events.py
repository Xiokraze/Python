import pygame
import pygame.locals as pl
import sys
import Draw


#####################
#   Game Specifics  #
#####################
def quit_game():
    pygame.quit()
    sys.exit(0)

def update_seconds(game):
    game.blink_frame_count += 1
    blink_frame_count = game.max_FPS * game.blink_delay
    if (game.blink_frame_count == (blink_frame_count)):
        game.blink_frame_count = 0
        game.seconds += 1
        return True
    return False

def check_frame_count(game):
    if (game.frame_count >= game.max_FPS):
        game.frame_count = 0
        game.seconds += 1
    return

def blink_text(game, screen, text):
    if (update_seconds(game)):
        if (game.blinking):
            game.blinking = False
        else:
            game.blinking = True
    if (game.blinking):
        game.draw_blink_text(screen, text)
    return


#####################
#    Title Events   #
#####################
def check_title_events(game):
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
                    quit_game()
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RETURN):
                return True
    return False


#####################
#  Gameplay Events  #
#####################



def check_game_events():
    mouse_position = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
            quit_game()
        #elif (event.type == pygame.KEYDOWN):

    return True