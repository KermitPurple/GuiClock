from Game import Game
import pygame

class Clock(Game):
    def __init__(self, size, radius):
        self.radius = radius
        self.center = int(size[0]/2), int(size[1]/2)
        Game.__init__(self, "Clock", size)
        self.play()

    def kbin(self, code: str, key: "pygame constant") -> None:
        pass

    def update(self):
        self.draw_face()

    def draw_clock(self):
        self.draw_face()

    def draw_face(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius, 2)
