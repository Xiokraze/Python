import pygame


class Button:
    buttons = []
    num_buttons = 0
    def __init__(self, x, y, text, game, is_menu_button, image_size=None):
        self.x = x
        self.y = y
        self.text = text
        self.text_color = game.text_color
        self.color = game.button_color
        self.hovering = False
        self.play_sound = True
        self.visible = True
        
        # Menu/Game Button Parameters
        if (is_menu_button):
            self.width = image_size[0]
        else:
            self.width = game.buttonW
        self.height = image_size[1]
        self.border = (self.x-2, self.y-2, self.width+4, self.height+4)


    #####################
    #      Getters      #
    #####################
    def get_menu_buttons(game):
        col = 1
        row = 1
        for index in range(len(game.grade_levels)):
            value = game.grade_levels[index]
            if (row == 1):
                y = game.y_menu_col_1
                if (col == 1):
                    image = game.grade_1st
                    image_size = image.get_size()
                    x = game.x_menu_col_1 - image_size[0] / 2
                elif (col == 2):
                    image = game.grade_2nd
                    image_size = image.get_size()
                    x = game.x_menu_col_2 - image_size[0] / 2
                else:
                    image = game.grade_3rd
                    image_size = image.get_size()
                    x = game.x_menu_col_3 - image_size[0] / 2
                    col = 0
                    row += 1
            elif (row == 2):
                y = game.y_menu_col_2
                if (col == 1):
                    image = game.grade_4th
                    image_size = image.get_size()
                    x = game.x_menu_col_1 - image_size[0] / 2
                elif (col == 2):
                    image = game.grade_5th
                    image_size = image.get_size()
                    x = game.x_menu_col_2 - image_size[0] / 2
                else:
                    image = game.grade_6th
                    image_size = image.get_size()
                    x = game.x_menu_col_3 - image_size[0] / 2
                    col = 0
                    row += 1
            elif (row == 3):
                y = game.y_menu_col_3
                if (col == 1):
                    image = game.grade_7th
                    image_size = image.get_size()
                    x = game.x_menu_col_3a - image_size[0] / 2
                elif (col == 2):
                    image = game.grade_8th
                    image_size = image.get_size()
                    x = game.x_menu_col_3b - image_size[0] / 2
            col += 1
            Button.add_button(x, y, value, True, image_size, game)
        return Button.buttons

    def get_game_buttons(game): # TODO refractor
        x_padding = 25

        # Mute
        image_size = game.mute_image.get_size()
        x = 0 + x_padding
        y = game.screenH / 2 - image_size[1] / 2
        Button.add_button(x, y, "Mute", False,  image_size, game)

        # Speed
        image_size = game.speed_image.get_size()
        x = game.screenW - image_size[0] - x_padding
        y = game.screenH / 2 - image_size[1] / 2
        Button.add_button(x, y, "Speed", False, image_size, game)

        # +
        image_size = game.speed_change.get_size()
        x = game.screenW - image_size[0]
        y = game.screenH / 2 - image_size[1] * 1.25 # offset for extra image px
        Button.add_button(x, y, "+", False, image_size, game)

        # -
        image_size = game.speed_change.get_size()
        x = game.screenW - image_size[0]
        y = game.screenH / 2 + image_size[1] * .9 # offset for extra image px
        Button.add_button(x, y, "-", False, image_size, game)

        return Button.buttons


    #####################
    #   Event Handling  #
    #####################
    def is_over(self, mouse_position):
        mouseX = mouse_position[0]
        mouseY = mouse_position[1]
        if (mouseX > self.x and mouseX < self.x + self.width):
            if (mouseY > self.y and mouseY < self.y + self.height):
                return True         
        return False

    def add_button(x, y, value, is_menu_button, image_size, game):
        Button.num_buttons += 1
        Button.buttons.append(Button(
            x, 
            y, 
            value,
            game,
            is_menu_button,
            image_size)
        )
        return
   
   
    #####################
    #      Drawing      #
    #####################
    def draw_button(self, screen, image, height, game):
        size = image.get_size()
        x = game.screenW - game.buttonW + (game.buttonW - size[0]) / 2
        y = game.screenH - height - game.bottom_boxH + (game.buttonH - size[1]) / 2
        screen.blit(image, (x, y))
        return

    def draw(self, screen, game, hover=None):
        if (self.visible):
            # Draw rect here to add outline to visible buttons
            #pygame.draw.rect(screen, self.color, self.border, game.border_width)
            if (self.hovering):
                if (self.text == "1st"):
                    screen.blit(game.grade_1st_hovering, (self.x, self.y))
                elif (self.text == "2nd"):
                    screen.blit(game.grade_2nd_hovering, (self.x, self.y))
                elif (self.text == "3rd"):
                    screen.blit(game.grade_3rd_hovering, (self.x, self.y))
                elif (self.text == "4th"):
                    screen.blit(game.grade_4th_hovering, (self.x, self.y))
                elif (self.text == "5th"):
                    screen.blit(game.grade_5th_hovering, (self.x, self.y))
                elif (self.text == "6th"):
                    screen.blit(game.grade_6th_hovering, (self.x, self.y))
                elif (self.text == "7th"):
                    screen.blit(game.grade_7th_hovering, (self.x, self.y))
                elif (self.text == "8th"):
                    screen.blit(game.grade_8th_hovering, (self.x, self.y))
                if (self.visible):
                    if (self.text == "Mute"):
                        screen.blit(game.mute_hovering, (self.x, self.y))
                    elif (self.text == "+"):
                        screen.blit(game.speed_up_hovering, (self.x, self.y))
                    elif (self.text == "-"):
                        screen.blit(game.speed_down_hovering, (self.x, self.y))
                    elif (self.text == "Speed"):
                        screen.blit(game.speed_image, (self.x, self.y))
            else:
                if (self.text == "Mute"):
                    screen.blit(game.mute_image, (self.x, self.y))
                elif (self.text == "Speed"):
                    screen.blit(game.speed_image, (self.x, self.y))
                elif (self.text == "+"):
                    screen.blit(game.speed_up, (self.x, self.y))
                elif (self.text == "-"):
                    screen.blit(game.speed_down, (self.x, self.y))
        return