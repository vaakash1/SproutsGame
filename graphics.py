import pygame
"""
The graphics class handles anything that deals with graphics.
"""

class Graphics:
    def __init__(self, window_size=(512,512)) -> None:
        """
        When called, this creates the initial (empty) window
        """
        self.SCREEN_WIDTH = window_size[0]
        self.SCREEN_HEIGHT = window_size[1]
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Sprouts")
        self.screen.fill(pygame.Color("black"))

    def get_dimensions(self):
        """
        Returns the dimensions of the screen (width, height)
        """
        return (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def draw_game_state(self, gs):
        """
        Draws the gamestate (dots and lines) on the window
        """
        DOT_RADIUS = 5
        for dot in gs.get_dots():
            pygame.draw.circle(self.screen, self.WHITE, dot.get_position(), DOT_RADIUS)

    def draw_end_text(self, text:str):
        """
        Draws the given text on the screen
        """
        font = pygame.font.SysFont("Helvetica", 32, True, False)
        text_object = font.render(text, 0, pygame.Color('Gray'))
        text_location = pygame.Rect(0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT).move(self.SCREEN_WIDTH / 2 - text_object.get_width() / 2,
                                                                    self.SCREEN_HEIGHT / 2 - text_object.get_height() / 2)
        self.screen.blit(text_object, text_location)
        text_object = font.render(text, 0, pygame.Color('Black'))
        self.screen.blit(text_object, text_location.move(-2, -2))

        