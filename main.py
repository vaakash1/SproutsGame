import pygame
import math
import graphics
import game_state

pygame.init()

if __name__ == "__main__":
    WINDOW_SIZE = (800,800)
    NUM_STARTING_DOTS = 4
    screen = graphics.Graphics(WINDOW_SIZE)
    gs = game_state.GameState(screen, NUM_STARTING_DOTS)
    game_over = False
    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            # mouse handlers
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    pass
                # key handlers
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:  # undo when 'z' is pressed
                    pass
                    
                if e.key == pygame.K_r:  # resets game when r is pressed
                    pass
        
        screen.draw_game_state(gs)

        pygame.display.flip()


"""
Copilot 90% Nonsense below
"""    
        
#     def __hash__(self) -> int:
#         return hash((self.start, self.end))
        
        
# class Game:
#     def __init__(self):
#         self.dots = set()
#         self.lines = []
#         self.running = True
#         self.screen = pygame.display.set_mode((800, 600))
                
#         for i in range(NUM_STARTING_DOTS):
#             # i dots in a circle
#             x = 100 + 50 * math.cos(i * 2 * math.pi / NUM_STARTING_DOTS)
#             y = 100 + 50 * math.sin(i * 2 * math.pi / NUM_STARTING_DOTS)

#             self.dots.add(Dot(x, y))
#     def draw(self):
#         for dot in self.dots:
#             pygame.draw.circle(self.screen, (255, 255, 255), (dot.x, dot.y), 5)
#         for line in self.lines:
#             pygame.draw.line(self.screen, (255, 255, 255), (line.start.x, line.start.y), (line.end.x, line.end.y))
#     def run(self):
#         while self.running:
#             selectedDots = []
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     x, y = pygame.mouse.get_pos()
#                     for dot in self.dots:
#                         if math.sqrt((x - dot.x) ** 2 + (y - dot.y) ** 2) < 5:
#                             selectedDots.append(dot)
#                         while(len(selectedDots) >= 2):
#                             selectedDots.pop(0)
#                         if len(selectedDots) == 2:
#                             # check if line is valid (e.g. not intersecting with other lines and both dots have less than 4 lines)
#                             valid = True
#                             for line in self.lines:
#                                 if (line.start == selectedDots[0] and line.end == selectedDots[1]) or (line.start == selectedDots[1] and line.end == selectedDots[0]):
#                                     valid = False
#                                 # check if line intersects with other lines
                                
#                             if valid:
#                                 self.lines.append(Line(selectedDots[0], selectedDots[1]))
#                                 self.update()
#                                 self.draw()
#                                 pygame.display.flip()
#                                 selectedDots.clear()
#                                 break
#             # highlight selected dots
#             if len(selectedDots) == 2:
#                 self.lines.append(Line(selectedDots[0], selectedDots[1]))
#             self.update()
#             self.draw()
#             pygame.display.flip()
            
#     def update(self):
#         pass
    
    


# g = Game()
# g.run()
# pygame.quit()
