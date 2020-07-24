import pygame
import os

class Game:

    """
    A wrapper to make pygame games more easily.
    inherit this class and overwrite kbin and update fns

    """

    def __init__(self, caption: str = "Game", size: ('x', 'y') = (600, 600), clear_screen: bool = True):
        """TODO: initialize game"""
        os.environ['SDL_VIDEO_WINDOW_POS'] = "15,30"
        self.size = size
        self.clear_screen = clear_screen
        self.running = False
        pygame.display.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(size=self.size)

    def kbin(self, code: str, key: "pygame constant") -> None:
        """ function to be overwritten, handle keyboard interaction """
        print("Overwrite kbin")

    def update(self) -> None:
        """ function to be overwritten, run every frame """
        print("Overwrite update")

    def play(self) -> None:
        """Start the game"""
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.kbin(event.unicode, event.key)
            if self.clear_screen: self.screen.fill((0, 0, 0))
            self.update()
            pygame.display.update()
