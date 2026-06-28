import pygame

from src.s_config import (
    WIDTH,
    HEIGHT,
    FPS,
    WHITE,
    BLACK,
    RED,
    GRAY,
    GAME_AREA_WIDTH,
    PANEL_WIDTH,
    START_LIVES,
    START_SCORE,
    START_LEVEL,
    START_PROGRESS,
    PROGRESS_BAR_PADDING,
    PROGRESS_BAR_WIDTH,
    PROGRESS_BAR_COLOR,
    PROGRESS_BAR_BG,
)


class SnackCatcherGame:
    MENU = "MENU"
    GAMEPLAY = "GAMEPLAY"
    GAMEOVER = "GAMEOVER"

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Snack Catcher")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = SnackCatcherGame.MENU
        self.lives = START_LIVES
        self.score = START_SCORE
        self.level = START_LEVEL
        self.progress = START_PROGRESS

        self.font = pygame.font.SysFont("arial", 24)

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.render()
        pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == SnackCatcherGame.GAMEPLAY:
                        self.state = SnackCatcherGame.MENU
                    elif self.state == SnackCatcherGame.MENU:
                        self.running = False
                    elif self.state == SnackCatcherGame.GAMEOVER:
                        self.state = SnackCatcherGame.MENU
                elif event.key == pygame.K_RETURN:
                    if self.state in (SnackCatcherGame.MENU, SnackCatcherGame.GAMEOVER):
                        self.start_game()

    def update(self, dt: float) -> None:
        if self.state == SnackCatcherGame.GAMEPLAY:
            self.progress = min(1.0, self.progress + dt * 0.1)
            if self.lives <= 0:
                self.state = SnackCatcherGame.GAMEOVER

    def render(self) -> None:
        self.screen.fill(BLACK)
        self.draw_game_area()
        self.draw_side_panel()
        self.draw_overlay_text()
        pygame.display.flip()

    def draw_game_area(self) -> None:
        game_area_rect = pygame.Rect(0, 0, GAME_AREA_WIDTH, HEIGHT)
        pygame.draw.rect(self.screen, GRAY, game_area_rect)
        border_rect = pygame.Rect(0, 0, GAME_AREA_WIDTH, HEIGHT)
        pygame.draw.rect(self.screen, WHITE, border_rect, 4)

    def draw_side_panel(self) -> None:
        panel_rect = pygame.Rect(GAME_AREA_WIDTH, 0, PANEL_WIDTH, HEIGHT)
        pygame.draw.rect(self.screen, BLACK, panel_rect)

        progress_x = GAME_AREA_WIDTH + (PANEL_WIDTH - PROGRESS_BAR_WIDTH) // 2
        progress_y = PROGRESS_BAR_PADDING
        progress_height = HEIGHT - 2 * PROGRESS_BAR_PADDING

        pygame.draw.rect(
            self.screen,
            PROGRESS_BAR_BG,
            (progress_x, progress_y, PROGRESS_BAR_WIDTH, progress_height),
        )

        filled_height = int(progress_height * self.progress)
        filled_y = progress_y + progress_height - filled_height
        pygame.draw.rect(
            self.screen,
            PROGRESS_BAR_COLOR,
            (progress_x, filled_y, PROGRESS_BAR_WIDTH, filled_height),
        )

        text = self.font.render("PROGRESO", True, WHITE)
        text_x = GAME_AREA_WIDTH + (PANEL_WIDTH - text.get_width()) // 2
        self.screen.blit(text, (text_x, progress_y + progress_height + 10))

    def draw_overlay_text(self) -> None:
        if self.state == SnackCatcherGame.MENU:
            title = self.font.render("SNACK CATCHER", True, WHITE)
            hint = self.font.render("Presiona ENTER para empezar", True, WHITE)
            self.screen.blit(title, (50, 100))
            self.screen.blit(hint, (50, 140))
        elif self.state == SnackCatcherGame.GAMEPLAY:
            status = self.font.render(
                f"Vidas: {self.lives}  Puntaje: {self.score}  Nivel: {self.level}", True, WHITE
            )
            self.screen.blit(status, (20, 20))
        elif self.state == SnackCatcherGame.GAMEOVER:
            title = self.font.render("GAME OVER", True, RED)
            hint = self.font.render("Presiona ENTER para reiniciar", True, WHITE)
            self.screen.blit(title, (50, 100))
            self.screen.blit(hint, (50, 140))

    def start_game(self) -> None:
        self.state = SnackCatcherGame.GAMEPLAY
        self.lives = START_LIVES
        self.score = START_SCORE
        self.level = START_LEVEL
        self.progress = START_PROGRESS


def main() -> None:
    game = SnackCatcherGame()
    game.run()


if __name__ == "__main__":
    main()
