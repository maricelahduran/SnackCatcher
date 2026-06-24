import pygame

from config.settings import WIDTH, HEIGHT, WHITE, BLACK, load_font


class StartScreen:
    def __init__(self, game) -> None:
        self.game = game
        self.font_title = load_font(48)
        self.font_text = load_font(28)
        self.font_small = load_font(20)
        self.input_active = False
        self.player_name = ""

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._button_rect(250, 320, 300, 50).collidepoint(event.pos):
                self.game.player_name = self.player_name or "Jugador"
                self.game.start_game()
            elif self._button_rect(250, 390, 300, 50).collidepoint(event.pos):
                self.game.transition_to("settings")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.player_name = self.player_name or "Jugador"
                self.game.start_game()
            elif event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            else:
                if event.unicode.isalnum() or event.unicode in {" ", "-", "_"}:
                    self.player_name += event.unicode

    def update(self, dt: float) -> None:
        self.player_name = self.player_name[:12]

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BLACK)
        title = self.font_title.render("SPACE INVADERS", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))

        prompt = self.font_text.render("Nombre del jugador:", True, WHITE)
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 220))

        name_surface = self.font_text.render(self.player_name or "Jugador", True, WHITE)
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 150, 260, 300, 40), 2)
        screen.blit(name_surface, (WIDTH // 2 - 140, 268))

        self._draw_button(screen, 250, 320, 300, 50, "Iniciar partida")
        self._draw_button(screen, 250, 390, 300, 50, "Configuración")

        hint = self.font_small.render("Presiona Enter para jugar", True, WHITE)
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 500))

    def _draw_button(self, screen: pygame.Surface, x: int, y: int, w: int, h: int, text: str) -> None:
        pygame.draw.rect(screen, WHITE, (x, y, w, h), 2)
        label = self.font_text.render(text, True, WHITE)
        screen.blit(label, (x + w // 2 - label.get_width() // 2, y + h // 2 - label.get_height() // 2))

    def _button_rect(self, x: int, y: int, w: int, h: int) -> pygame.Rect:
        return pygame.Rect(x, y, w, h)
