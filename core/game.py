import pygame

from config.settings import WIDTH, HEIGHT, FPS, BLACK, WHITE, load_font
from screens.start_screen import StartScreen
from screens.loading_screen import LoadingScreen
from screens.settings_screen import SettingsScreen
from screens.game_screen import GameScreen
from screens.game_over_screen import GameOverScreen


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Space Invaders")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_screen = "start"
        self.player_name = "Jugador"
        self.config = None
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.victory = False
        self.paused = False

        self.screens = {
            "start": StartScreen(self),
            "loading": LoadingScreen(self),
            "settings": SettingsScreen(self),
            "game": GameScreen(self),
            "game_over": GameOverScreen(self),
        }

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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.current_screen == "game":
                    self.paused = not self.paused
            else:
                self.screens[self.current_screen].handle_event(event)

    def update(self, dt: float) -> None:
        if self.current_screen == "game" and not self.paused:
            self.screens[self.current_screen].update(dt)
        else:
            self.screens[self.current_screen].update(dt)

    def render(self) -> None:
        self.screen.fill(BLACK)
        self.screens[self.current_screen].render(self.screen)
        pygame.display.flip()

    def transition_to(self, screen_name: str) -> None:
        self.current_screen = screen_name

    def start_game(self) -> None:
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.victory = False
        self.paused = False
        self.transition_to("loading")

    def finish_game(self, victory: bool) -> None:
        self.game_over = True
        self.victory = victory
        self.transition_to("game_over")
