def initialize_level_1_blocks(game):
    image = game.blue_block
    size = image.get_size()
    left_x = 0 + size[0]
    right_x = game.screen_width - size[0] * 3
    y = 0 + size[1] * 3
    #positions = (
    #    # L
    #    (left_x, y), 
    #    (left_x, y + size[1]),
    #    (left_x, y + size[1] * 2), 
    #    (left_x, y + size[1] * 3), 
    #    (left_x, y + size[1] * 4), 
    #    (left_x, y + size[1] * 5), 
    #    (left_x, y + size[1] * 6), 
    #    (left_x + size[0], y + size[1] * 5),
    #    (left_x + size[0], y + size[1] * 6),


    #    # O
    #    (left_x + size[0] * 3, y),
    #    (left_x + size[0] * 3, y + size[1]),
    #    (left_x + size[0] * 3, y + size[1] * 2),
    #    (left_x + size[0] * 3, y + size[1] * 3),
    #    (left_x + size[0] * 3, y + size[1] * 4),
    #    (left_x + size[0] * 3, y + size[1] * 5),
    #    (left_x + size[0] * 3, y + size[1] * 6),
    #    (left_x + size[0] * 4, y),
    #    (left_x + size[0] * 4, y + size[1]),
    #    (left_x + size[0] * 4, y),
    #    (left_x + size[0] * 4, y + size[1] * 5),
    #    (left_x + size[0] * 4, y + size[1] * 6),
    #    (left_x + size[0] * 5, y),
    #    (left_x + size[0] * 5, y + size[1]),
    #    (left_x + size[0] * 5, y + size[1] * 2),
    #    (left_x + size[0] * 5, y + size[1] * 3),
    #    (left_x + size[0] * 5, y + size[1] * 4),
    #    (left_x + size[0] * 5, y + size[1] * 5),
    #    (left_x + size[0] * 5, y + size[1] * 6),

    #    # L
    #    (right_x, y),
    #    (right_x, y + size[1]), 
    #    (right_x, y + size[1] * 2), 
    #    (right_x, y + size[1] * 3), 
    #    (right_x, y + size[1] * 4), 
    #    (right_x, y + size[1] * 5), 
    #    (right_x, y + size[1] * 6), 
    #    (right_x + size[0], y + size[1] * 5),
    #    (right_x + size[0], y + size[1] * 6),
    #)
    #for pos in positions:
    #    Block(game, image, pos[0], pos[1])
    return