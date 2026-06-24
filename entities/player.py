import pygame

from config.settings import WIDTH, HEIGHT


class Player:
    def __init__(self, x: int, y: int) -> None:
        self.width = 40
        self.height = 30
        self.x = x
        self.y = y
        self.speed = 300
        self.lives = 3
        self.is_alive = True
        self.double_shot = False

    def move(self, dx: float, dt: float) -> None:
        self.x += dx * self.speed * dt
        self.x = max(0, min(WIDTH - self.width, self.x))

    def shoot(self) -> list[dict]:
        if self.double_shot:
            return [
                {"x": self.x + 8, "y": self.y, "speed": 450, "direction": -1},
                {"x": self.x + self.width - 18, "y": self.y, "speed": 450, "direction": -1},
            ]
        return [{"x": self.x + self.width // 2 - 3, "y": self.y, "speed": 450, "direction": -1}]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
