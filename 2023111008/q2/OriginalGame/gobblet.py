import pygame
from board import Board
from piece import Piece
from config import S_WIDTH, S_HEIGHT
from game import Game

pygame.init()
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Gobblet Jr.")

board = Board()
game = Game(board)

running = True
dragging_piece = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game.winner and not dragging_piece:
                dragging_piece = game.pick_piece(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_piece:
                game.drop_piece(dragging_piece)
                dragging_piece = None

        elif event.type == pygame.MOUSEMOTION:
            if dragging_piece:
                dragging_piece.x, dragging_piece.y = event.pos

    screen.fill((255, 255, 255))
    board.draw(screen)
    game.draw_pieces(screen)
    pygame.display.flip()

pygame.quit()
