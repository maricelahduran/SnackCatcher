import pygame
from src.s_config import GAME_AREA_WIDTH, HEIGHT, BLUE


class Player(pygame.sprite.Sprite):
    """Player sprite: a blue rectangle constrained to the left game area.

    Movement is horizontal only. Use `update(keys, dt)` from the main loop
    so we can pass the current pressed keys and delta time.
    """

    def __init__(self, x: int, y: int, width: int = 60, height: int = 24, speed: float = 350.0) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self, keys: pygame.key.ScancodeWrapper, dt: float) -> None:
        """Move the player horizontally according to arrow keys.

        The player is clamped inside [0, GAME_AREA_WIDTH - width].
        """
        dx = 0
        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1

        # Apply movement
        self.rect.x += int(dx * self.speed * dt)

        # Enforce strict bounds inside the game area (left area only)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > GAME_AREA_WIDTH:
            self.rect.right = GAME_AREA_WIDTH

    def reset_position(self, x: int, y: int) -> None:
        self.rect.topleft = (x, y)
