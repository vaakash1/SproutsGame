import math
"""
This file handles the current game events
"""
class GameEvent:
    def __init__(self, gs):
        self.mouse_events = []
        self.curr_event = 0
        self.key_events = []
        self.gs = gs

    def reset_events(self):
        self.mouse_events = []
        self.key_events = []

    def dist(self, dot, click_pos):
        return math.sqrt((dot.x - click_pos.pos[0])**2 + (dot.y - click_pos.pos[1])**2)

    def check_dot(self, click_pos):
        return [x for x in self.gs.get_dots() if self.dist(x, click_pos) <= 5]

    #Listens for events and adds them to the event list for later traversal
    def event_listener(self, e):
        dot_list = self.check_dot(e)
        if len(dot_list) > 0:
            self.mouse_events.append(self.select_dot(dot_list))

    def select_dot(self, dot_list):
        dot_list[0].color = (255, 0, 0)
        return True
    #Use 'iterator' on the event list --> keep track of past events, so its easier to do the undo method
    #Create several undo_events methods for each event
    def undo_event(self):
        pass







