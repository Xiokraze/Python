import pygame


#####################
#   Event Handling  #
#####################
def check_events(game):
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
                    game.quit_game()
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RETURN):
                return True
    return False


#####################
#      Drawing      #
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

#####################
#    Title Screen   #
#####################
def title_screen(screen, game):
    game.play_music(game.title_music)
    while (True):
        if (check_events(game)):
            break
        draw_screen(screen, game)
    return


#####################
#    Start Screen   #
#####################
def start_screen(screen, game):
    while (True):
        if (check_events(game)):
            game.words_moving = True
            break
        draw_screen(screen, game, True)
    return