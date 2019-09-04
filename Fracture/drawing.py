import pygame




#####################
#        Game       #
#####################
def draw_background(game):
    game.screen.blit(game.bg_space, (0,0))
    return

def draw_title_image(game):
    x, y = game.get_title_image_location()
    game.screen.blit(game.title_image, (x,y))
    return

def draw_blink_text(game, prompt):
    text = game.word_font.render(prompt, 1, game.text_color)
    x, y = game.get_title_prompt_location(prompt)
    game.screen.blit(text, (x,y))
    return

def draw_spheres(screen, spheres):
    for sphere in spheres:
        sphere.draw_sphere(screen)
    return


#####################
#      Borders      #
#####################
def draw_across(game, screen, size, image, ui_bot=False, ui_top=False):
    x_start = game.level.x_left - size[0] / 2
    x_end = game.level.x_right - size[0]
    if (ui_bot):
        y = game.level.y_top - size[1] - size[1] / 2
    elif(ui_top):
        y = size[1] - size[1] / 2
    else:
        y = game.level.y_top - size[1] / 2
    x_offset = size[0]
    num_sides = 1
    while (True):
        x = x_start + x_offset * num_sides
        if (x > x_end):
            break
        screen.blit(image, (x,y))
        num_sides += 1
    return

def draw_sides(game, screen, size, image, right=False, ui=False):
    if (right):
        x = game.level.x_right- size[0] / 2
    else:
        x = game.level.x_left- size[0] / 2
    if (ui):
        y_start = size[1] / 2
        y_end = game.level.y_top - size[1] * 2
    else:
        y_start = game.screen_height - game.level.playable_height - size[1] / 2
        y_end = game.screen_height
    y_offset = size[1]
    num_sides = 1
    while (True):
        y = y_start + y_offset * num_sides
        num_sides += 1
        if (ui and y > y_end):
            break
        else:
           if (y > y_end):
            break
        screen.blit(image, (x,y))
    return

def draw_corner_border(game, screen, size, image, right=False, ui_bot=False, ui_top=False):
    if (right):
        x = game.level.x_right- size[0] / 2
    else:
        x = game.level.x_left- size[0] / 2
    if (ui_bot):
        y = game.level.y_top - size[1] / 2 - size[1]
    elif(ui_top):
        y = size[1] / 2
    else:
        y = game.level.y_top - size[1] / 2
    screen.blit(image, (x,y))
    return

def draw_playable_borders(game, screen):
    # border = [topl, top, topr, right, botr, bottom, botl, left]
    size = game.level.border[0].get_size() # images are all same width/height in px
    draw_corner_border(game, screen, size, game.level.border[0])
    draw_corner_border(game, screen, size, game.level.border[2], True)
    draw_sides(game, screen, size, game.level.border[7])
    draw_sides(game, screen, size, game.level.border[3], True)
    draw_across(game, screen, size, game.level.border[1])

    #rect = (100, game.screen_height - game.playable_height, game.playable_width, game.screen_height)
    #pygame.draw.rect(screen, (0,0,255), rect, 2)
    return

def draw_ui_borders(game, screen):
    # border = [topl, top, topr, right, botr, bottom, botl, left]
    size = game.level.border[0].get_size() # images are all same width/height in px
    draw_corner_border(game, screen, size, game.level.border[6], False, True)
    draw_corner_border(game, screen, size, game.level.border[4], True, True)
    draw_corner_border(game, screen, size, game.level.border[0], False, False, True)
    draw_corner_border(game, screen, size, game.level.border[2], True, False, True)
    draw_across(game, screen, size, game.level.border[5], True)
    draw_across(game, screen, size, game.level.border[1], False, True)
    draw_sides(game, screen, size, game.level.border[7], False, True)
    draw_sides(game, screen, size, game.level.border[3], True, True)
    return