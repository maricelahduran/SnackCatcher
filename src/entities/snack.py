import random
import pygame
from src.s_config import GAME_AREA_WIDTH, YELLOW, RED


class Snack(pygame.sprite.Sprite):
    """Falling snack sprite.

    snack_type: 'normal' or 'quemado'
    Normal: yellow, gives points. Quemado: red, obstacle.
    """

    SIZE = 24

    def __init__(self, snack_type: str = "normal", fall_speed: float = 180.0) -> None:
        super().__init__()
        self.snack_type = snack_type
        self.image = pygame.Surface((Snack.SIZE, Snack.SIZE))
        self.color = YELLOW if snack_type == "normal" else RED
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # spawn at random x inside game area, slightly above the screen
        max_x = max(0, GAME_AREA_WIDTH - Snack.SIZE)
        self.rect.x = random.randint(0, max_x)
        self.rect.y = -random.randint(Snack.SIZE, Snack.SIZE * 3)

        # speed in pixels per second
        self.fall_speed = fall_speed * random.uniform(0.8, 1.2)

    def update(self, dt: float, speed_multiplier: float = 1.0) -> None:
        """Update vertical position using dt and current speed multiplier."""
        self.rect.y += int(self.fall_speed * speed_multiplier * dt)
