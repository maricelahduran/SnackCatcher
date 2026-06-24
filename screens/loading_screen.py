import pygame

from config.settings import BLACK, WHITE, load_font, WIDTH, HEIGHT


class LoadingScreen:
    def __init__(self, game) -> None:
        self.game = game
        self.font = load_font(36)
        self.timer = 0.0

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, dt: float) -> None:
        self.timer += dt
        if self.timer >= 1.0:
            self.game.transition_to("game")

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BLACK)
        text = self.font.render("Cargando partida...", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
