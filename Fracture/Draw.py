import pygame


#####################
#       Title       #
#####################
def get_title_location(game):
    image_size = game.title_image.get_size()
    x = game.screen_width / 2 - image_size[0] / 2
    y = 0 + image_size[1]
    return x, y

def title_screen(game, screen):
    screen.fill(game.background)
    x, y = get_title_location(game)
    screen.blit(game.title_image, (x,y))
    return


#####################
#     Blink Text    #
#####################
def get_title_prompt_location(game, prompt):
    font_size = game.font.getsize(prompt)
    x = (game.screen_width / 2) - (font_size[0] / 2)
    y = (game.screen_height / 2) + font_size[1]
    return x, y

def blink_text(game, screen, prompt):
    text = game.word_font.render(prompt, 1, game.text_color)
    x, y = get_title_prompt_location(game, prompt)
    screen.blit(text, (x,y))
    return


#####################
#      Spheres      #
#####################
def draw_spheres(game, screen, spheres):
    for sphere in spheres:
        screen.blit(sphere.image, (sphere.x,sphere.y))
    return


#####################
#       Player      #
#####################
def draw_player(screen, player):
    screen.blit(player.image, (player.x, player.y))
    pygame.draw.rect(screen, (0,255,0), player.rect, 2)
    return


#####################
#        Game       #
#####################
def draw_game(game, screen, player, spheres):
    screen.fill(game.background)
    draw_player(screen, player)
    draw_spheres(game, screen, spheres)
    pygame.display.update()
    return