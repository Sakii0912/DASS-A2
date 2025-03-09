"""
This file contains the main game logic for gobblet jr.
Initialising the board, pieces, and checking for the winner.
And also pick up and drop the pieces on the board.
"""

import pygame
from piece import Piece
from config import RED, YELLOW, CELL_SIZE

class Game:
    """
    This is the main game class containing all the functionality.
    """
    def __init__(self, board):
        self.board = board
        self.turn = "Player 1"
        self.pieces = [
            Piece(10, 50, 600, RED, 1, "Player 1"),
            Piece(20, 100, 600, RED, 1,  "Player 1"),
            Piece(30, 150, 600, RED, 1, "Player 1"),
            Piece(10, 200, 600, RED, 2, "Player 1"),
            Piece(20, 250, 600, RED, 2, "Player 1"),
            Piece(30, 300, 600, RED, 2, "Player 1"),
            Piece(10, 350, 600, YELLOW, 1, "Player 2"),
            Piece(20, 400, 600, YELLOW, 1, "Player 2"),
            Piece(30, 450, 600, YELLOW, 1, "Player 2"),
            Piece(10, 500, 600, YELLOW, 2, "Player 2"),
            Piece(20, 550, 600, YELLOW, 2, "Player 2"),
            Piece(30, 600, 600, YELLOW, 2, "Player 2"),
        ]
        self.winner = None
        self.selected_piece = None

    def pick_piece(self, pos):
        """
        This function is used to pick up the piece from the board.
        """
        for piece in reversed(self.pieces):
            if ((pos[0] - piece.x) ** 2 + (pos[1] - piece.y) ** 2) ** 0.5 < piece.size:
                row, col = piece.y // CELL_SIZE, piece.x // CELL_SIZE

                if (0 <= row < 3 and 0 <= col < 3 and self.board.grid[row][col]):
                    if self.board.grid[row][col][-1] is not piece:
                        continue

                if piece.player == self.turn:
                    self.selected_piece = piece
                    return piece
        return None

    def drop_piece(self, piece):
        """
        This is used to drop the piece on the board.
        """
        if self.winner or not piece:
            return

        row, col = piece.y // CELL_SIZE, piece.x // CELL_SIZE
        if 0 <= row < len(self.board.grid) and 0 <= col < len(self.board.grid[0]):
            stack = self.board.grid[row][col]

            if not stack or piece.size > stack[-1].size:
                previous_position = None
                if piece in self.pieces:
                    old_row = piece.prev_y // CELL_SIZE
                    old_col = piece.prev_x // CELL_SIZE
                    if 0 <= old_row < 3 and 0 <= old_col < 3:
                        previous_position = (old_row, old_col)

                stack.append(piece)
                piece.prev_x, piece.prev_y = piece.x, piece.y
                piece.x, piece.y = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2

                if previous_position and self.check_winner():
                    self.winner = "Player 2" if self.turn == "Player 1" else "Player 1"
                elif self.check_winner():
                    self.winner = self.turn
                else:
                    self.turn = "Player 2" if self.turn == "Player 1" else "Player 1"
            else:
                piece.x, piece.y = piece.prev_x, piece.prev_y

            self.selected_piece = None
        else:
            piece.x, piece.y = piece.prev_x, piece.prev_y

    def check_winner(self):
        """
        This function is used to check the winner of the game.
        """
        def get_top_player(row, col):
            if self.board.grid[row][col]:
                return self.board.grid[row][col][-1].player
            return None

        for i in range(3):
            if get_top_player(i, 0) == get_top_player(i, 1) == get_top_player(i, 2):
                if get_top_player(i, 0) is not None:
                    return True
            if get_top_player(0, i) == get_top_player(1, i) == get_top_player(2, i):
                if get_top_player(0, i) is not None:
                    return True

        if get_top_player(0, 0) == get_top_player(1, 1) == get_top_player(2, 2) and get_top_player(0, 0) is not None:
            return True
        if get_top_player(0, 2) == get_top_player(1, 1) == get_top_player(2, 0) and get_top_player(0, 2) is not None:
            return True

        return False

    def draw_winner(self, screen):
        """
        This function is used to draw the winner on the screen.
        """
        if self.winner:
            font = pygame.font.Font(None, 50)
            text = font.render(f"{self.winner} Wins!", True, (0, 200, 0))
            screen.blit(text, (200, 50))

    def draw_pieces(self, screen):
        """
        This function is used to draw the pieces on the screen.
        """
        for piece in self.pieces:
            piece.draw(screen)
        self.draw_winner(screen)
