import pygame
from piece import Piece
from config import RED, YELLOW, CELL_SIZE

class Game:
    def __init__(self, board):
        self.board = board
        self.turn = "Player 1"
        self.pieces = [
            Piece(10, 100, 600, RED, "Player 1"),
            Piece(20, 200, 600, RED, "Player 1"),
            Piece(30, 300, 600, RED, "Player 1"),
            Piece(10, 400, 600, YELLOW, "Player 2"),
            Piece(20, 500, 600, YELLOW, "Player 2"),
            Piece(30, 600, 600, YELLOW, "Player 2"),
        ]
        self.winner = None
        self.selected_piece = None

    def pick_piece(self, pos):
        for piece in reversed(self.pieces):
            if ((pos[0] - piece.x) ** 2 + (pos[1] - piece.y) ** 2) ** 0.5 < piece.size:
                if piece.player == self.turn:
                    self.selected_piece = piece
                    return piece
        return None

    def drop_piece(self, piece):
        if self.winner or not piece:
            return

        row, col = piece.y // CELL_SIZE, piece.x // CELL_SIZE
        if 0 <= row < len(self.board.grid) and 0 <= col < len(self.board.grid[0]):
            stack = self.board.grid[row][col]
            if not stack or piece.size > stack[-1].size:
                stack.append(piece)
                piece.x, piece.y = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2

                if self.check_winner():
                    self.winner = self.turn
                else:
                    self.turn = "Player 2" if self.turn == "Player 1" else "Player 1"
            else:
                piece.x, piece.y = piece.prev_x, piece.prev_y
            self.selected_piece = None
        else:
            piece.x, piece.y = piece.prev_x, piece.prev_y

    def check_winner(self):
        def get_top_player(row, col):
            if self.board.grid[row][col]:
                return self.board.grid[row][col][-1].player
            return None

        for i in range(3):
            if get_top_player(i, 0) == get_top_player(i, 1) == get_top_player(i, 2):
                return get_top_player(i, 0)
            if get_top_player(0, i) == get_top_player(1, i) == get_top_player(2, i):
                return get_top_player(0, i)

        if get_top_player(0, 0) == get_top_player(1, 1) == get_top_player(2, 2) and get_top_player(0, 0) is not None:
            return True
        if get_top_player(0, 2) == get_top_player(1, 1) == get_top_player(2, 0) and get_top_player(0, 2) is not None:
            return True

        return False

    def draw_winner(self, screen):
        if self.winner:
            font = pygame.font.Font(None, 50)
            text = font.render(f"{self.winner} Wins!", True, (0, 200, 0))
            screen.blit(text, (200, 50))

    def draw_pieces(self, screen):
        for piece in self.pieces:
            piece.draw(screen)
        self.draw_winner(screen)
