import graphics
import math
"""
This file handles the current game state
"""

DESELECTED_DOT_COLOR = (255, 255, 255)
SELECTED_DOT_COLOR = (77, 77, 255)

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = DESELECTED_DOT_COLOR 
    
    def get_position(self):
        return (self.x, self.y)

    def get_color(self):
        return self.color

        
class Line:
    def __init__(self, start:Dot, end:Dot):
        self.start = start
        self.end = end
    
    def intersects(self, line):
        """returns true if the line intersects with another line, false otherwise
        """
        def ccw(A, B, C):
            """
            Checks if points a, b, and c are in counter-clockwise order, using determinants
            """
            return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

        def intersect(A, B, C, D):
            """checks if line AB intersects line CD using the ccw function above
            """
            return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

        return intersect(self.start, self.end, line.start, line.end)

class GameState:
    def __init__(self, screen:graphics, starting_dots:int=3):
        self.screen = screen
        self.list_of_dots = []
        self.selected_dots = []
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
    
    def select_dot(self, dot):
        """
        When the user clicks on a dot, add it to the list of selected dots
        """
        dot.color = SELECTED_DOT_COLOR
        self.selected_dots.insert(0, dot)
        while(len(self.selected_dots) > 2):
            extra = self.selected_dots.pop()
            extra.color = DESELECTED_DOT_COLOR
