import math
import pygame
from game_state import SELECTED_DOT_COLOR, DESELECTED_DOT_COLOR
from game_state import Dot, Line
from abc import ABC, abstractmethod
"""
This file handles the current game events
"""
class GameEvent:
    def __init__(self, gs):
        self.events = []
        self.currIndex = 0
        self.gs = gs

    def dist(self, dot, click_pos):
        return math.sqrt((dot.x - click_pos.pos[0])**2 + (dot.y - click_pos.pos[1])**2)

    def check_dot(self, click_pos):
        unselected_dots = set(self.gs.get_dots()).difference(set(self.gs.get_selected()))
        return [x for x in unselected_dots if self.dist(x, click_pos) <= 5]

    #Listens for events and adds them to the a list of events triggered by the player
    def event_listener(self, e):
        """:
       Handles user induced events
        """
        #Handles Mouse Events
        if(e.type == pygame.MOUSEBUTTONDOWN):
            self.handle_click(e)
        # Handles Key Events
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:  # resets game when 'r' is pressed
               self.reset_events()
            if e.key == pygame.K_z:
                self.undo_event()
            if e.key == pygame.K_k:
                print(f"Lines: {[str(line) for line in self.gs.get_lines()]}") 
                print(f"Dots: {[str(dot) for dot in self.gs.get_dots()]}")
    

    def handle_click(self, e):
        """
        If the user has clicked on a dot, select it
        """
        if(len(self.gs.get_selected()) < 2):
            for dot in self.check_dot(e):
                dot_event = SelectDot(dot)
                self.add_event(dot_event)
                dot_event.execute(self.gs)
        if(len(self.gs.get_selected()) == 2):
            self.events.pop(0)
            self.events.pop(0)
            dot1 = self.gs.get_selected().pop(0)
            dot2 = self.gs.get_selected().pop(0)
            
            dot1.color = DESELECTED_DOT_COLOR
            dot2.color = DESELECTED_DOT_COLOR
            line = Line(dot1, dot2)
            for l in self.gs.get_lines():
                if(line.intersects(l)):
                    print("Line intersects")
                    print(line, "intersects", l)
                    return
            line_event = MakeLine(line)
            self.add_event(line_event)
            print("Line Made")
            line_event.execute(self.gs)
        pass

    def reset_events(self):
        self.events = []

    def undo_event(self):
        if(len(self.events) > 0):
            past_event  = self.events.pop(0)
            past_event.undo(self.gs)
        pass
 
    def add_event(self, event):
        self.events.insert(0, event)

class Action(ABC):
    """Used to represent an action that can be executed and undone"""
    @abstractmethod
    def execute(self, gs):
        """Performs the action
        """
        pass

    @abstractmethod
    def undo(self, gs):
        """Undoes the action
        """
        pass

class SelectDot(Action):
    def __init__(self, dot):
        self.dot = dot
    def __str__(self):
        return "dot event"

    def execute(self, gs):
        gs.add_select_dot(self.dot)
        self.dot.color = SELECTED_DOT_COLOR
    def undo(self, gs):
        self.dot.color = DESELECTED_DOT_COLOR
        return gs.get_selected().pop(0)

    def get_dot(self):
        return self.dot
    

class MakeLine(Action):
    def __init__(self, line):
        self.line = line
    def __str__(self):
        return "line event "
    def execute(self, gs):
        self.line.start.color = DESELECTED_DOT_COLOR
        self.line.end.color = DESELECTED_DOT_COLOR
        gs.get_lines().append(self.line)

    def undo(self, gs):
        print(gs.get_lines())
        gs.get_lines().pop()
        print(gs.get_lines())
