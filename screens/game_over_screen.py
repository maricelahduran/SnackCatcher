import pygame

from config.settings import BLACK, WHITE, RED, load_font, WIDTH, HEIGHT


class GameOverScreen:
    def __init__(self, game) -> None:
        self.game = game
        self.font_title = load_font(42)
        self.font_text = load_font(26)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.game.start_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.game.start_game()

    def update(self, dt: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BLACK)
        result = "¡Victoria!" if self.game.victory else "¡Derrota!"
        color = WHITE if self.game.victory else RED
        title = self.font_title.render(result, True, color)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))

        score = self.font_text.render(f"Puntuación final: {self.game.score}", True, WHITE)
        screen.blit(score, (WIDTH // 2 - score.get_width() // 2, 220))

        hint = self.font_text.render("Presiona Enter para reiniciar", True, WHITE)
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 320))
