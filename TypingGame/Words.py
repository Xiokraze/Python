import random

class Word(object):
    def __init__(self, game, word):
        self.word = word
        self.text_color = game.text_color

        speed = Word.get_speed(len(word), game.max_word_speed)
        self.speed = speed * game.up_or_down

        # Calculate px size for word width and height
        text_size = game.font.getsize(self.word)
        self.width = text_size[0]
        self.height = text_size[1]

        # Get px offset from right border to keep the word on the game screen
        image_size = game.right_corner.get_size()
        image_x_offset = image_size[0] * game.right_corner_x_offset
        word_size = game.font.getsize(self.word)
        word_x_offset = word_size[0]
        x_min = image_x_offset
        x_max = game.screenW - image_x_offset - word_x_offset
        self.x = random.randint(x_min, x_max)
        if (game.up_or_down == -1):
            input_box_H = game.bottom_boxH - game.border_width * 2
            self.y = game.screenH - input_box_H - self.height
        else:
            self.y = 0 - self.height


    #####################
    #      Getters      #
    #####################
    def get_speed(word_length, max_speed):
        if (word_length == 2): return max_speed
        elif (word_length == 3): return max_speed * .8
        elif (word_length == 4): return max_speed * .7
        elif (word_length == 5): return max_speed * .6
        elif (word_length == 6): return max_speed * .5
        else: return max_speed * .4