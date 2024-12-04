import graphics
import math
import numpy as np
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
    
    def __eq__(self, value: object) -> bool:
        return (self.x == value.x) and (self.y == value.y)
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def get_position(self):
        return (self.x, self.y)

    def get_color(self):
        return self.color

        
class Line:
    def __init__(self, start:Dot, end:Dot):
        self.start = start
        self.end = end
    def __str__(self):
        return f"Line from {self.start} to {self.end}"
    
    def get_line(self):
        return (self.start, self.end)
    
    def get_matrix_equation(self, line):
        """
        Returns a matrix A and vector B representing the line in the form A = [[a1, b1], [a2, b2]] and B = [c1, c2] 
        where a1x + b1y = c1 and a2x + b2y = c2 are the equations of each line
        """
        a1 = self.end.y - self.start.y
        b1 = self.start.x - self.end.x
        a2 = line.end.y - line.start.y
        b2 = line.start.x - line.end.x

        
        c1 = a1 * self.start.x + b1 * self.start.y
        c2 = a2 * line.start.x + b2 * line.start.y
        
        A = np.array([[a1, b1], [a2, b2]])
        B = np.array([c1, c2])
        
        return (A, B)
    
    def get_equation(self):
        """
        Returns a list of coefficients in the equation of the line in the form ax + by = c
        """
        a = self.end.y - self.start.y
        b = self.start.x - self.end.x 
        c = a * self.start.x + b * self.start.y

        return [a, b, c]
        
    def dot_on_line(self, dot):
        """ Returns true if the dot is on the line (excluding the endpoints), false otherwise
        """
        eq = self.get_equation()
        return eq[0] * dot.x + eq[1] * dot.y == eq[2] and self.end != dot and self.start != dot
        
    def intersects(self, line):
        def check_consistency(A, B):
            augmented_matrix = np.column_stack((A, B))
            rank_A = np.linalg.matrix_rank(A)
            rank_augmented = np.linalg.matrix_rank(augmented_matrix)

            if rank_A == rank_augmented:
                try:
                    intersection = np.linalg.solve(A, B)
                    print("System has one solution.")
                    return 1
                except np.linalg.LinAlgError:
                    print("System has infinitely many solutions")
                    return 2
                # if rank_A < A.shape[1]:
                #     print("Infinitely many solutions.")
                #     return 2
                # else:
                #     print("Unique solution.")
                #     return 1
            else:
                print("System is inconsistent.")
                return 0
        def order_dots(self, line):
            # x1 = self.start.x
            # x2 = self.end.x
            # x3 = line.start.x
            # x4 = line.end.x
            # return [(min(x1, x2), min(y1, y2)), max(x1,x2)]
            line_direction = (line.end.x - line.start.x, line.end.y - line.start.y)
            a = [self.start, self.end, line.start, line.end]
            a.sort(key=lambda dot: line_direction[0] * dot.x + line_direction[1] * dot.y)
            return a
        
        A, B = self.get_matrix_equation(line)
        # try:
        #     intersection = np.linalg.solve(A, B)
        #     if (min(self.start.x, self.end.x) < intersection[0] < max(self.start.x, self.end.x) and
        #         min(self.start.y, self.end.y) < intersection[1] < max(self.start.y, self.end.y) and
        #         min(line.start.x, line.end.x) < intersection[0] < max(line.start.x, line.end.x) and
        #         min(line.start.y, line.end.y) < intersection[1] < max(line.start.y, line.end.y)):
        #         return True
        # except np.linalg.LinAlgError:
        #     pass
        # return False
        consistency = check_consistency(A, B)
        if consistency == 0:
            return False
        elif consistency == 2:
            #check if lines intersect or are just collinear
            # return (self.start.x <= line.end.x and self.start.y <= line.end.y) or (self.start.x >= line.end.x and self.start.y >= line.end.y)
            ord = order_dots(self, line)
            print([str(dot) for dot in ord])
            return not(ord[0] == self.start and ord[1] == self.end 
                       or ord[1] == self.start and ord[0] == self.end 
                       or ord[2] == self.start and ord[3] == self.end 
                       or ord[3] == self.start and ord[2] == self.end)
            #x1 <= x
        else:
            #check if intersection is at the endpoints
            solution = np.linalg.solve(A, B)
            solution_dot = Dot(solution[0], solution[1])
            print(solution)
            return self.dot_on_line(solution_dot) and line.dot_on_line(solution_dot)
    
    #copilot nonsense
    """def intersects(self, line):
        #returns true if the line intersects with another line, false otherwise
        
        def ccw(A, B, C):
            #Checks if points a, b, and c are in counter-clockwise order, using determinants
            return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)
        def intersect(A, B, C, D):
            #checks if line AB intersects line CD using the ccw function above. 
            if ((A == C) and (B != D)) or ((A != C) and (B == D)):
                # return dot product of the two lines
                dot_product = (B.x - A.x) * (D.y - C.y) + (B.y - A.y) * (C.x - D.x)
                mag_AB = math.sqrt((B.x - A.x)**2 + (B.y - A.y)**2) 
                mag_CD = math.sqrt((D.x - C.x)**2 + (D.y - C.y)**2)
                print(dot_product, mag_AB, mag_CD)
                return abs(mag_AB * mag_CD - dot_product) <= 1e-6
            return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
        return intersect(self.start, self.end, line.start, line.end)"""

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

    def get_selected(self):
        """
        Returns the list of selected dots
        """
        return self.selected_dots
    
    def add_select_dot(self, dot):
        """
        When the user clicks on a dot, add it to the list of selected dots
        """
        self.selected_dots.insert(0,dot)
