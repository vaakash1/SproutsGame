import math
import pygame
from game_state import SELECTED_DOT_COLOR, DESELECTED_DOT_COLOR
from abc import ABC, abstractmethod
"""
This file handles the current game events
"""
class GameEvent:
    def __init__(self, gs):
        self.events = []
        self.currIndex = 0
        self.gs = gs

    def reset_events(self):
        self.events = []

    def dist(self, dot, click_pos):
        return math.sqrt((dot.x - click_pos.pos[0])**2 + (dot.y - click_pos.pos[1])**2)

    def check_dot(self, click_pos):
        unselected_dots = set(self.gs.get_dots()).difference(set(self.gs.get_selected()))
        return [x for x in unselected_dots if self.dist(x, click_pos) <= 5]

    #Listens for events and adds them to the a list of events triggered by the player
    def event_listener(self, e):
        """
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
    

    def handle_click(self, e):
        """
        If the user has clicked on a dot, select it
        """
        if(len(self.gs.get_selected()) < 2):
            for dot in self.check_dot(e):
                dot_event = SelectDot(dot)
                self.add_event(dot_event)
                self.gs.add_select_dot(dot)
                self.currIndex +=1
                dot_event.execute()
        pass

    def undo_event(self):
        if(len(self.events) > 0):
            past_event  = self.events.pop(self.currIndex - 1)
            past_event.undo()
            if(type(past_event) == SelectDot):
               self.gs.get_selected().pop(0)
            self.currIndex-=1
        pass


    
    def add_event(self, event):
        self.events.append(event)

class Action(ABC):
    """Used to represent an action that can be executed and undone"""
    @abstractmethod
    def execute(self):
        """Performs the action
        """
        pass

    @abstractmethod
    def undo(self):
        """Undoes the action
        """
        pass

class SelectDot(Action):
    def __init__(self, dot):
        self.dot = dot

    def execute(self):
        self.dot.color = SELECTED_DOT_COLOR

    def undo(self):
        self.dot.color = DESELECTED_DOT_COLOR

    def get_dot(self):
        return self.dot
    


