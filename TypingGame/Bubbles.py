import pygame
import random

class Bubbles:
        bubble = pygame.image.load("Media/bubbles/b1.png")
        bubble_pop = [
        pygame.image.load("Media/bubbles/b%s.png" % img) for img in range(2,8)
        ]
        bubble_array = []
        def __init__(self, game):
            self.img = Bubbles.bubble
            size = self.img.get_size()
            self.width = size[0]
            self.height = size[1]
            screenW, screenH = pygame.display.get_surface().get_size()
            self.x = random.randint(0, (game.screenW - self.width))
            self.y = game.screenH + self.height
            self.startX = self.x
            self.speed = random.uniform(.5, 1.5)
            self.max_wobble = 6
            self.direction = random.choice(["right", "left"])
            self.pop_count = 1
            self.popping = False
            self.pop_FPS = 5

        def draw(self, screen, game):
            if not (self.popping):
                screen.blit(self.img, (self.x, self.y))
                self.y -= self.speed
                if (self.y <= (0 - game.font_size - game.border_width)):
                    self.popping = True
            return
            
        def pop_bubble(self, screen):
            if (self.popping):
                img = self.bubble_pop[self.pop_count // self.pop_FPS]
                screen.blit(img, (self.x, self.y))
                self.pop_count += 1
                if (self.pop_count > len(self.bubble_pop) + 1):
                    return True
            return False

        def update_wobble(self):
            if not (self.popping):
                if (self.direction == "right"):
                    self.x += .2
                    if (self.x >= 0 + self.startX + self.max_wobble):
                        self.direction = "left"
                else:
                    self.x -= .2
                    if (self.x <= self.startX - self.max_wobble):
                        self.direction = "right"
            return

        def update_bubbles(self, game):
            for bubble in Bubbles.bubble_array:
                bubble.update_wobble()
            if (game.frame_count == game.max_FPS):
                Bubbles.bubble_array.append(Bubbles(game))
            return