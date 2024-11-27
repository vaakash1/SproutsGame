import math
from game_state import SELECTED_DOT_COLOR, DESELECTED_DOT_COLOR
from abc import ABC, abstractmethod
"""
This file handles the current game events
"""
class GameEvent:
    def __init__(self, gs):
        self.events = []
        self.gs = gs

    def reset_events(self):
        self.events = []

    def dist(self, dot, click_pos):
        return math.sqrt((dot.x - click_pos.pos[0])**2 + (dot.y - click_pos.pos[1])**2)

    def check_dot(self, click_pos):
        return [x for x in self.gs.get_dots() if self.dist(x, click_pos) <= 5]

    #Listens for events and adds them to the a list of events triggered by the player
    def event_listener(self, e):
        self.handle_click(e)
        pass
    

    def handle_click(self, e):
        """
        If the user has clicked on a dot, select it
        """
        for dot in self.check_dot(e):
            dot_event = SelectDot(dot)
            self.events.append(dot_event)
            dot_event.execute()
            pass

    #Use 'iterator' on the event list --> keep track of past events, so its easier to do the undo method
    #Create several undo_events methods for each event
    def undo_event(self):
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
        self.dot.color = (255, 255, 255)
    


