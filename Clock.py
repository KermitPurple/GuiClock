from Game import Game
import numpy as np
import pygame

class Clock(Game):
    def __init__(self, size: int, radius: int):
        self.radius = radius
        self.center = int(size[0]/2), int(size[1]/2)
        Game.__init__(self, "Clock", size)
        self.play()

    def kbin(self, code: str, key: "pygame constant") -> None:
        pass

    def update(self):
        self.draw_clock()

    def draw_clock(self):
        self.draw_face()

    def draw_face(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius, 2)
        for i in range(12):
            theta = (i * 30) / 180 * np.pi
            offset = (6 if i % 3 == 0 else 4)
            width = (2 if i % 3 == 0 else 1)
            p1 = self.center[0], self.radius + offset + self.center[1]
            p2 = self.center[0], self.radius - offset + self.center[1]
            p1 = self.rotate_point(p1, theta, self.center)
            p2 = self.rotate_point(p2, theta, self.center)
            pygame.draw.line(self.screen, (255, 255, 255), p1, p2, width)

    @staticmethod
    def rotate_point(point: ('x', 'y'), theta: "radians", center: ('x', 'y')) -> ('x', 'y'):
        x = (point[0] - center[0]) * np.cos(theta) + (point[1] - center[1]) * np.sin(theta) + center[0]
        y = (point[0] - center[0]) * -np.sin(theta) + (point[1] - center[1]) * np.cos(theta) + center[1]
        return(x, y)
