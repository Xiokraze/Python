import pygame


class Button:
    buttons = []
    num_buttons = 0
    def __init__(self, x, y, text, visible, game, menu_button=False):
        self.x = x
        self.y = y + game.border_width
        self.text = text
        self.visible = visible
        self.text_color = game.text_color
        self.color = game.button_color
        self.hovering = False
        self.play_sound = True
        if (menu_button):
            self.height = game.menu_buttonH
            self.width = game.menu_buttonW
        else:
            self.height = game.buttonH
            self.width = game.buttonW
        self.border = (self.x-2, self.y-2, self.width+4, self.height+4)

    def draw_button(self, screen, image, height, game):
        size = image.get_size()
        x = game.screenW - game.buttonW + (game.buttonW - size[0]) / 2
        y = game.screenH - height - game.bottom_boxH + (game.buttonH - size[1]) / 2
        screen.blit(image, (x, y))
        return

    def draw(self, screen, game, hover=None):
        if (self.visible):
            # Draw rect here to add outline to visible buttons\
            #pygame.draw.rect(screen, self.color, self.border, game.border_width)
            if (self.hovering):
                pygame.draw.rect(screen, game.text_color, self.border, game.border_width)
            text = game.word_font.render(self.text, 1, self.text_color)
            text_size = game.font.getsize(self.text)
            fontW = text_size[0]
            fontH = text_size[1] + game.font_size / 2
            if (self.text == "Pause"):
                height = game.buttonH
                self.draw_button(screen, game.pause_image, height, game)
            elif (self.text == "Mute"):
                height = game.buttonH * 2 + game.border_width * 2
                self.draw_button(screen, game.mute_image, height, game)
            else:
                x = self.x + (self.width / 2 - fontW / 2) + game.border_width
                y = self.y + (self.height / 2 - fontH / 2)
                screen.blit(text, (x,y))
        return
    
    def is_over(self, mouse_position):
        mouseX = mouse_position[0]
        mouseY = mouse_position[1]
        if (mouseX > self.x and mouseX < self.x + self.width):
            if (mouseY > self.y and mouseY < self.y + self.height):
                return True         
        return False

    def addButton(y, index, game):
        Button.num_buttons += 1
        x = game.screenW / 2 - game.menu_buttonW / 2 - game.border_width
        Button.buttons.append(Button(
            x, 
            y, 
            game.grade_levels[index],
            True,
            game,
            True)
        )
        return

    def get_menu_buttons(game):
        text_size = game.font.getsize(game.menu_prompt)
        top_padding = text_size[1] + game.border_width
        button_padding = game.border_width * 4
        num_borders = 2
        for index in range(len(game.grade_levels)):
            num_buttons = Button.num_buttons
            buttonH_padding = game.menu_buttonH * num_buttons
            border_padding = button_padding * num_borders
            y = top_padding + buttonH_padding + border_padding
            Button.addButton(y, index, game)
            num_borders += 2
        Button.num_buttons = 0
        return Button.buttons

    def get_game_buttons(game):
        x = game.get_menu_button_x()
        y = game.get_menu_button_y()
        Button.buttons.append(Button(x, y, "Pause", True, game))
        y = y - (game.buttonH) - (game.border_width)
        Button.buttons.append(Button(x, y, "Mute", True, game))
        return Button.buttons