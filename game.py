# game.py

import pygame
import elements
import constants

pygame.init()

p1 = elements.Player("X", "Player 1")
p2 = elements.Player("O", "Player 2")


def game():
    board = elements.Board(4, 4)
    screen = pygame.display.set_mode([800, 800])
    noahthis = pygame.image.load("noahthis.png")


    pygame.display.set_caption("Anti-Newtonian Connect 4")
    pygame.display.set_icon(noahthis)

    ellipse_field = elements.Ellipse_Field(board.width, board.height).generate()
    print(ellipse_field)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(constants.L_GREEN)
        
        for ellipse in ellipse_field.values():
                pygame.draw.ellipse(screen, constants.D_GREEN, ellipse)

        # draw circles on board 
        # ask active player for selection
        #  - if human, use mouse input 
        #  - if bot, use alpha beta pruning + mcts 
        # place selection in board
        # check for a win. if so, end game
        
        
        pygame.display.flip()

        