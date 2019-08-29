

# Title
def title_image(game, screen):
    image_size = game.title_image.get_size()
    x = game.screen_width / 2 - image_size[0] / 2
    y = 0 + image_size[1]
    screen.blit(game.title_image, (x,y))
    return

# Blink Text
def blink_text(game, screen, text):
    font_size = game.font.getsize(text)
    x = (game.screen_width / 2) - (font_size[0] / 2)
    y = (game.screen_height / 2) + font_size[1]
    text = game.word_font.render(text, 1, game.text_color)
    screen.blit(text, (x,y))
    return

# Spheres
def spheres(game, screen, spheres):
    for sphere in spheres:
        screen.blit(sphere.image, (sphere.x,sphere.y))
    return

# Player
def player(screen, player):
    screen.blit(player.image, (player.x, player.y))
    return