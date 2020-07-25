import pygame
import numpy as np

class ClockHand:

    def __init__(self, radius: int, center: ("x", "y"), color: ("r", "g", "b"), width: int):
        self.radius = radius
        self.center = center
        self.color = color
        self.width = width

    def draw(self, screen: "pygame surface object", theta: "radians") -> None:
        point = (
                np.cos(theta) * self.radius + self.center[0],
                np.sin(theta) * self.radius + self.center[1]
                )
        pygame.draw.line(screen, self.color, self.center, point, self.width)

class HourHand(ClockHand):

    def __init__(self, outer_radius: int, center: ("x" , "y")):
        ClockHand.__init__(self, outer_radius / 100 * 75, center, (255, 255, 255), 5)

    def draw(self, screen: "pygame surface object", hours: int) -> None:
        theta = hours / 6 * np.pi - np.pi/2
        ClockHand.draw(self, screen, theta)

class MinuteHand(ClockHand):

    def __init__(self, outer_radius: int, center: ("x" , "y")):
        ClockHand.__init__(self, outer_radius / 100 * 85, center, (255, 255, 255), 3)

    def draw(self, screen: "pygame surface object", minutes: int) -> None:
        theta = minutes / 30 * np.pi - np.pi/2
        ClockHand.draw(self, screen, theta)

class SecondHand(ClockHand):

    def __init__(self, outer_radius: int, center: ("x" , "y")):
        ClockHand.__init__(self, outer_radius / 100 * 95, center, (255, 0, 0), 1)

    def draw(self, screen: "pygame surface object", seconds: int) -> None:
        theta = seconds / 30 * np.pi - np.pi/2
        ClockHand.draw(self, screen, theta)
