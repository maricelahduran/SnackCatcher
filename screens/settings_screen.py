import pygame

from config.settings import BLACK, WHITE, load_font, WIDTH, HEIGHT


class SettingsScreen:
    def __init__(self, game) -> None:
        self.game = game
        self.font = load_font(24)
        self.options = ["Fácil", "Media", "Difícil"]
        self.selected_difficulty = 0
        self.selected_enemies = ["Básico"]
        self.enable_powerups = True
        self.random_mode = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.transition_to("start")
            elif event.key == pygame.K_RETURN:
                self.game.config = {
                    "difficulty": self.options[self.selected_difficulty],
                    "selected_enemies": self.selected_enemies,
                    "enable_powerups": self.enable_powerups,
                    "random_mode": self.random_mode,
                }
                self.game.transition_to("start")
            elif event.key == pygame.K_LEFT:
                self.selected_difficulty = (self.selected_difficulty - 1) % len(self.options)
            elif event.key == pygame.K_RIGHT:
                self.selected_difficulty = (self.selected_difficulty + 1) % len(self.options)
            elif event.key == pygame.K_p:
                self.enable_powerups = not self.enable_powerups
            elif event.key == pygame.K_r:
                self.random_mode = not self.random_mode

    def update(self, dt: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BLACK)
        title = self.font.render("Configuración", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        diff = self.font.render(f"Dificultad: {self.options[self.selected_difficulty]}", True, WHITE)
        screen.blit(diff, (120, 180))

        enemies = self.font.render(f"Enemigos: {', '.join(self.selected_enemies)}", True, WHITE)
        screen.blit(enemies, (120, 240))

        powerups = self.font.render(f"Power-ups: {'Sí' if self.enable_powerups else 'No'}", True, WHITE)
        screen.blit(powerups, (120, 300))

        random_mode = self.font.render(f"Aleatorio: {'Sí' if self.random_mode else 'No'}", True, WHITE)
        screen.blit(random_mode, (120, 360))

        help_text = self.font.render("Esc para volver, Enter para guardar", True, WHITE)
        screen.blit(help_text, (120, 500))
