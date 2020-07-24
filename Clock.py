from Game import Game
import numpy as np
import pygame

class Clock(Game):
    def __init__(self, size: int, radius: int):
        self.radius = radius
        self.center = int(size[0]/2), int(size[1]/2)
        pygame.font.init()
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
            theta = (i * 30 - 90) / 180 * np.pi
            offset = (6 if i % 3 == 0 else 4)
            width = (2 if i % 3 == 0 else 1)
            outer_tick_point = self.center[0], self.radius + offset + self.center[1]
            inner_tick_point = self.center[0], self.radius - offset + self.center[1]
            outer_tick_point = self.rotate_point(outer_tick_point, theta, self.center)
            inner_tick_point = self.rotate_point(inner_tick_point, theta, self.center)
            pygame.draw.line(self.screen, (255, 255, 255), outer_tick_point, inner_tick_point, width)
            num_point = (
                    np.cos(theta) * (self.radius - 25) + self.center[0] - 5,
                    np.sin(theta) * (self.radius - 25) + self.center[1] - 10
                    )
            num = pygame.font.SysFont("Arial", 20).render(str(i + 1), True, (255, 255, 255))
            self.screen.blit(num, num_point)

    @staticmethod
    def rotate_point(point: ('x', 'y'), theta: "radians", center: ('x', 'y')) -> ('x', 'y'):
        x = (point[0] - center[0]) * np.cos(theta) + (point[1] - center[1]) * np.sin(theta) + center[0]
        y = (point[0] - center[0]) * -np.sin(theta) + (point[1] - center[1]) * np.cos(theta) + center[1]
        return(x, y)
