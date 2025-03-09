"""
This file contains the piece class which is used to create the
pieces used in the game
"""

import pygame

class Piece:
    """
    This class is used in other parts of the game for pieces.
    """
    def __init__(self, size, x, y, color, number, player):
        """
        This function initializes the piece object
        """
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.number = number
        self.player = player
        self.prev_x = x
        self.prev_y = y

    def draw(self, screen):
        """
        This function is used to draw the circular piece on the screen
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
