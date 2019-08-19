import pygame


def check_events(game):
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
                    game.quit_game()
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RETURN):
                return True
    return False

def draw_screen(screen, game, start_screen=False):
    game.clock.tick(game.max_FPS)
    game.frame_count += 1
    game.draw_bg_image(screen)
    if (start_screen):
        game.draw_text_blink(screen, game.start_prompt, start_screen)
    else:
        game.draw_title(screen)
        game.draw_text_blink(screen, game.title_prompt, start_screen)
    game.draw_bubbles(screen, game)
    pygame.display.update()
    game.check_frame_count()
    return

def play(screen, game):
    game.play_music(game.title_music)
    while (True):
        if (check_events(game)):
            break
        draw_screen(screen, game)
    return

def start_screen(screen, game):
    while (True):
        if (check_events(game)):
            game.words_falling = True
            break
        draw_screen(screen, game, True)
    return