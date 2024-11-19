import graphics
import math
"""
This file handles the current game state
"""

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self):
        return (self.x, self.y)
        
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class GameState:
    def __init__(self, screen:graphics, starting_dots:int=3):
        self.screen = screen
        self.list_of_dots = []
        self.generate_dots(starting_dots)
        self.list_of_lines = []
        self.turn = 1

    def generate_dots(self, starting_dots:int):
        """
        Generates the given number of dots at the start of the game in a circular pattern around the center of the screen
        """
        middle_x = self.screen.get_dimensions()[0]/2
        middle_y = self.screen.get_dimensions()[1]/2
        RADIUS = 100 #radius of the circle
        theta = 0
        for i in range(starting_dots):
            self.list_of_dots.append(Dot(middle_x + RADIUS * math.cos(theta), middle_y + RADIUS * math.sin(theta)))
            theta += (2 * math.pi) / starting_dots

    def get_dots(self):
        """
        Returns the list of dots
        """
        return self.list_of_dots
    
    def get_lines(self):
        """
        Returns the list of lines
        """
        return self.list_of_lines



