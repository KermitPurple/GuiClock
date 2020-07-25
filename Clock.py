from Game import Game
import ClockHand
import numpy as np
import datetime
import pygame

class Clock(Game):
    def __init__(self, size: int, radius: int):
        self.radius = radius
        self.center = int(size[0]/2), int(size[1]/2)
        self.smooth_seconds = True
        pygame.font.init()
        Game.__init__(self, "Clock", size)
        self.play()

    def kbin(self, code: str, key: "pygame constant") -> None:
        if code == 's':
            self.smooth_seconds = not self.smooth_seconds

    def update(self):
        self.datetime = datetime.datetime.today()
        self.draw_clock()

    def draw_clock(self):
        self.draw_datetime()
        self.draw_face()
        ClockHand.SecondHand(self.radius, self.center).draw(self.screen, self.datetime.second, self.datetime.microsecond, self.smooth_seconds)
        ClockHand.MinuteHand(self.radius, self.center).draw(self.screen, self.datetime.minute, self.datetime.second)
        ClockHand.HourHand(self.radius, self.center).draw(self.screen, self.datetime.hour, self.datetime.minute, self.datetime.second)

    def draw_face(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius, 2)
        for i in range(12):
            theta = (i * 30 - 90) / 180 * np.pi
            offset = (6 if i % 3 == 0 else 4)
            width = (4 if i % 3 == 0 else 1)
            outer_tick_point = self.center[0], self.radius + offset + self.center[1]
            inner_tick_point = self.center[0], self.radius - offset + self.center[1]
            outer_tick_point = self.rotate_point(outer_tick_point, theta, self.center)
            inner_tick_point = self.rotate_point(inner_tick_point, theta, self.center)
            pygame.draw.line(self.screen, (255, 255, 255), outer_tick_point, inner_tick_point, width)
            num_point = (
                    np.cos(theta) * (self.radius - 20) + self.center[0] - 5,
                    np.sin(theta) * (self.radius - 20) + self.center[1] - 10
                    )
            self.draw_text(str(i if i != 0 else 12), num_point)

    def draw_datetime(self):
        self.draw_text_centered(self.datetime.strftime("%B %d, %Y"), (self.center[1], 100))
        self.draw_text_centered(str(self.datetime.date()), (self.center[1], 125))
        self.draw_text_centered(self.datetime.strftime("%A"), (self.center[1], 150))
        self.draw_text_centered(self.datetime.strftime("%I:%M:%S %p"), (self.center[1], 175))

    def draw_text(self, text: str, position: ('x', 'y'), color: ('r', 'g', 'b') = (255, 255, 255), font: str = "agencyfb", font_size: int = 20) -> None:
        text_surface = pygame.font.SysFont(font, font_size).render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_text_centered(self, text: str, position: ('x', 'y'), color: ('r', 'g', 'b') = (255, 255, 255), font: str = "agencyfb", font_size: int = 20) -> None:
        text_surface = pygame.font.SysFont(font, font_size).render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = position
        self.screen.blit(text_surface, text_rect)

    @staticmethod
    def rotate_point(point: ('x', 'y'), theta: "radians", center: ('x', 'y')) -> ('x', 'y'):
        x = (point[0] - center[0]) * np.cos(theta) + (point[1] - center[1]) * np.sin(theta) + center[0]
        y = (point[0] - center[0]) * -np.sin(theta) + (point[1] - center[1]) * np.cos(theta) + center[1]
        return(x, y)
