import pygame

from config.settings import WIDTH


class Enemy:
    def __init__(self, x: int, y: int, enemy_type: str = "básico") -> None:
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.enemy_type = enemy_type
        self.speed = 80 if enemy_type == "básico" else 120 if enemy_type == "rápido" else 60
        self.is_alive = True
        self.direction = 1

    def update(self, dt: float) -> None:
        self.x += self.direction * self.speed * dt
        if self.x <= 0 or self.x + self.width >= WIDTH:
            self.direction *= -1
            self.y += 20

    def draw(self, screen: pygame.Surface) -> None:
        color = (255, 0, 0) if self.enemy_type == "básico" else (255, 165, 0) if self.enemy_type == "rápido" else (128, 0, 128)
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
