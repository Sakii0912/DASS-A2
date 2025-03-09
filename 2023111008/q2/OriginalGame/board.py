"""
This module contains the Board class which is responsible for drawing the grid on the screen.
"""

import pygame
from config import GRID_SIZE, CELL_SIZE, BLACK

class Board:
    """
    This class is responsible for drawing the grid on the screen.
    """
    def __init__(self):
        """
        Initializing the grid.
        """
        self.grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def draw(self, screen):
        """
        Draws the grid on the screen.
        """
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_SIZE * GRID_SIZE), 3)
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (CELL_SIZE * GRID_SIZE, i * CELL_SIZE), 3)
