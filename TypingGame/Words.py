import random

class Word(object):
    falling = False
    max_charH = 0
    def __init__(self, game, word):
        self.word = word
        self.text_color = game.text_color

        self.falling_speed = Word.get_falling_speed(len(word), game.max_y_speed)

        # Calculate px size for word width and height
        text_size = game.font.getsize(self.word)
        self.width = text_size[0]
        self.height = text_size[1]

        # Get px offset from right border to keep the word on the game screen
        xOffset = game.screenW - self.width - game.border_width * 4 - game.buttonW
        self.x = random.randint(0, xOffset)
        self.y = 0

        Word.max_charH = max(self.height, Word.max_charH)


    #####################
    #      Getters      #
    #####################
    def get_falling_speed(word_length, max_y_speed):
        if (word_length == 2): return max_y_speed 
        elif (word_length == 3): return max_y_speed * .8
        elif (word_length == 4): return max_y_speed * .6
        elif (word_length == 5): return max_y_speed * .5
        elif (word_length == 6): return max_y_speed * .3
        elif (word_length == 7): return max_y_speed * .3
        else: return max_y_speed * .2