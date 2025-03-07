import pygame
from config import GRID_SIZE, CELL_SIZE, BLACK

class Board:
    def __init__(self):
        self.grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def draw(self, screen):
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_SIZE * GRID_SIZE), 3)
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (CELL_SIZE * GRID_SIZE, i * CELL_SIZE), 3)
