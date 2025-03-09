"""
This is the main file for the Game. It creates the board, game and handles the movement of the pieces in the game
"""

import pygame
from board import Board
from config import S_WIDTH, S_HEIGHT
from game import Game

pygame.init()

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Gobblet Jr.")

board = Board()
game = Game(board)

RUNNING = True
DRAGGING_PIECE = None

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game.winner and not DRAGGING_PIECE:
                DRAGGING_PIECE = game.pick_piece(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            if DRAGGING_PIECE:
                game.drop_piece(DRAGGING_PIECE)
                DRAGGING_PIECE = None

        elif event.type == pygame.MOUSEMOTION:
            if DRAGGING_PIECE:
                DRAGGING_PIECE.x, DRAGGING_PIECE.y = event.pos

    screen.fill((255, 255, 255))
    board.draw(screen)
    game.draw_pieces(screen)
    pygame.display.flip()
