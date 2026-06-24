import pygame

from config.settings import WIDTH


class PowerUp:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 18
        self.height = 18
        self.active = True
        self.speed = 120
        self.duration = 4.0

    def update(self, dt: float) -> None:
        self.y += self.speed * dt

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width, self.height))
