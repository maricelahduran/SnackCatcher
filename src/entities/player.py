import pygame
from src.s_config import GAME_AREA_WIDTH, HEIGHT, BLUE


class Player(pygame.sprite.Sprite):
    """Player sprite: a blue basket in the lower game area.

    The player is represented as a basket-like surface with an arc and base.
    Movement is horizontal only and the sprite cannot leave the game area.
    """

    def __init__(self, x: int, y: int, width: int = 70, height: int = 26, speed: float = 350.0) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._draw_basket()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def _draw_basket(self) -> None:
        """Draw a more realistic wicker-style basket with shadow and rim."""
        self.image.fill((0, 0, 0, 0))
        base_color = BLUE
        rim_color = (30, 90, 180)
        shadow_color = (10, 10, 60, 120)

        # Main basket body
        pygame.draw.ellipse(self.image, base_color, (0, self.height // 4, self.width, self.height * 3 // 4))
        pygame.draw.rect(self.image, base_color, (0, self.height // 2, self.width, self.height // 2))

        # Basket rim and supports
        pygame.draw.rect(self.image, rim_color, (0, self.height // 2 - 4, self.width, 8))
        for x in range(8, self.width - 8, 12):
            pygame.draw.line(self.image, rim_color, (x, self.height // 2), (x, self.height - 4), 2)

        # Decorative texture lines
        for offset in range(8, self.width - 8, 10):
            pygame.draw.arc(self.image, (100, 170, 255), (offset - 4, self.height // 4 - 2, 16, 16), 3.14, 0, 1)

        # Shadow inside the basket
        shadow = pygame.Surface((self.width, self.height // 3), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, shadow_color, (0, 0, self.width, self.height // 2))
        self.image.blit(shadow, (0, self.height // 2))

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
