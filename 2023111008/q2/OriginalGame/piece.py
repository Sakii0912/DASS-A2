import pygame

class Piece:
    def __init__(self, size, x, y, color, number, player):
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.number = number
        self.player = player
        self.prev_x = x
        self.prev_y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
