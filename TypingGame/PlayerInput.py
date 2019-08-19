import pygame
import pygame.locals as pl


class PlayerInput:
    def __init__(self, game,):
        self.cursor_color = game.text_color,

        # Text related vars:
        self.antialias = True
        self.text_color = game.text_color
        self.input_string = ""  # Inputted text
        self.font_obj = pygame.font.Font(game.master_font, game.font_size)

        # Cursor related vars:
        self.cursor_surface = pygame.Surface((2, game.font_size))
        self.cursor_surface.fill(self.cursor_color)
        self.cursor_pos = len(self.input_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_ms = 400
        self.cursor_ms_counter = 0
        self.clock = game.clock

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True
                if event.key == pl.K_BACKSPACE:
                    PlayerInput.key_backspace(self)
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_pos = max(self.cursor_pos - 1, 0)
                elif (event.key == pl.KMOD_LSHIFT or event.key == pl.KMOD_RSHIFT):
                    if(False):
                        pass
                    else:
                        PlayerInput.key_shift(self)
                elif event.key == pl.K_RETURN:
                    return True
                #elif event.key == pl.ESCAPE: #TODO clear current input if esc is hit
                else:
                    PlayerInput.add_key_to_input(self, event) # TODO FIX

        # Re-render text surface:
        self.surface = self.font_obj.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_ms:
            self.cursor_ms_counter %= self.cursor_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_obj.size(self.input_string[:self.cursor_pos])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_pos > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            #self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 5))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_pos

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""
        self.cursor_pos = 0

    def key_shift(self):
        self.input_string = (
            self.input_string[:self.cursor_pos]
                + event.unicode
                + self.input_string[self.cursor_pos:]
            ).upper()
        return

    def key_backspace(self):
        self.input_string = (
            self.input_string[:max(self.cursor_pos - 1, 0)]
            + self.input_string[self.cursor_pos:]
        )
        return

    def add_key_to_input(self, event):
        self.input_string = (
            self.input_string[:self.cursor_pos]
            + event.unicode
            + self.input_string[self.cursor_pos:]
        )
        self.cursor_pos += len(event.unicode)  # Some are empty, e.g. K_UP
        return

    def reset_input_text(userInput):
        userInput.input_string = ""
        userInput.cursor_pos = 0
        return