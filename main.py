import pygame
import math
import graphics
import game_state
import game_events

pygame.init()

if __name__ == "__main__":
    WINDOW_SIZE = (800, 800)
    NUM_STARTING_DOTS = 4
    screen = graphics.Graphics(WINDOW_SIZE)
    gs = game_state.GameState(screen, NUM_STARTING_DOTS)
    ev = game_events.GameEvent(gs)
    game_over = False
    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:  # game ends when red x is pressed
                running = False
                pygame.quit()
            # event handlers
            if not game_over:
                    ev.event_listener(e)
        screen.draw_game_state(gs)

        pygame.display.flip()
