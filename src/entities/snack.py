import random
import pygame
from src.s_config import GAME_AREA_WIDTH, YELLOW, RED


class Snack(pygame.sprite.Sprite):
    """Falling snack sprite.

    snack_type: 'normal' or 'quemado'
    Normal: yellow chip. Quemado: red burned chip.
    """

    SIZE = 28

    def __init__(self, snack_type: str = "normal", fall_speed: float = 180.0) -> None:
        super().__init__()
        self.snack_type = snack_type
        self.size = Snack.SIZE
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.color = YELLOW if snack_type == "normal" else RED
        self._draw_chip()
        self.rect = self.image.get_rect()

        # spawn at random x inside game area, slightly above the screen
        max_x = max(0, GAME_AREA_WIDTH - self.size)
        self.rect.x = random.randint(0, max_x)
        self.rect.y = -random.randint(self.size, self.size * 2)

        # speed in pixels per second
        self.fall_speed = fall_speed * random.uniform(0.9, 1.15)

    def _draw_chip(self) -> None:
        """Draw a chip with a crunchy shape and small holes."""
        self.image.fill((0, 0, 0, 0))
        pygame.draw.ellipse(self.image, self.color, (0, 0, self.size, self.size))
        inner_rect = pygame.Rect(4, 4, self.size - 8, self.size - 8)
        pygame.draw.ellipse(self.image, (255, 255, 255, 50), inner_rect, 2)
        hole_color = (255, 215, 0) if self.snack_type == "normal" else (200, 80, 80)
        hole_positions = [
            (self.size * 0.3, self.size * 0.2),
            (self.size * 0.7, self.size * 0.3),
            (self.size * 0.4, self.size * 0.65),
            (self.size * 0.75, self.size * 0.7),
        ]
        for x, y in hole_positions:
            pygame.draw.circle(self.image, hole_color, (int(x), int(y)), 3)

    def update(self, dt: float, speed_multiplier: float = 1.0) -> None:
        """Update vertical position using dt and current speed multiplier."""
        self.rect.y += int(self.fall_speed * speed_multiplier * dt)
