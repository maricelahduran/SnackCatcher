import random
import pygame

from config.settings import WIDTH, HEIGHT, BLACK, WHITE, RED, load_font
from entities.player import Player
from entities.enemy import Enemy
from entities.powerup import PowerUp


class GameScreen:
    def __init__(self, game) -> None:
        self.game = game
        self.font = load_font(24)
        self.player = Player(WIDTH // 2 - 20, HEIGHT - 60)
        self.enemies = []
        self.bullets = []
        self.powerups = []
        self.cooldown = 0.0
        self.spawn_timer = 0.0
        self.init_level()

    def init_level(self) -> None:
        self.enemies.clear()
        enemies_to_spawn = ["básico", "rápido", "resistente"]
        for row in range(3):
            for col in range(8):
                enemy_type = enemies_to_spawn[(row + col) % len(enemies_to_spawn)]
                self.enemies.append(Enemy(40 + col * 90, 60 + row * 50, enemy_type))
        self.player.lives = 3
        self.player.double_shot = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bullets.extend(self.player.shoot())
            elif event.key == pygame.K_ESCAPE:
                self.game.paused = not self.game.paused

    def update(self, dt: float) -> None:
        if self.game.paused:
            return
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        self.player.move(dx, dt)

        self.cooldown -= dt
        self.spawn_timer += dt
        if self.spawn_timer >= 3.0 and random.random() < 0.3:
            self.powerups.append(PowerUp(random.randint(40, WIDTH - 40), 0))
            self.spawn_timer = 0.0

        for bullet in self.bullets[:]:
            bullet["y"] -= 450 * dt
            if bullet["y"] < -10:
                self.bullets.remove(bullet)

        for enemy in self.enemies:
            enemy.update(dt)
            if enemy.y >= HEIGHT - 80:
                self.game.lives = 0
                self.game.finish_game(False)
                return

        for powerup in self.powerups[:]:
            powerup.update(dt)
            if powerup.y > HEIGHT:
                self.powerups.remove(powerup)
            elif powerup.x < self.player.x + self.player.width and powerup.x + powerup.width > self.player.x and powerup.y < self.player.y + self.player.height and powerup.y + powerup.height > self.player.y:
                self.player.double_shot = True
                self.powerups.remove(powerup)

        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if (
                    bullet["x"] < enemy.x + enemy.width
                    and bullet["x"] + 6 > enemy.x
                    and bullet["y"] < enemy.y + enemy.height
                    and bullet["y"] + 10 > enemy.y
                ):
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.game.score += 100
                    break

        for enemy in self.enemies:
            if (
                enemy.x < self.player.x + self.player.width
                and enemy.x + enemy.width > self.player.x
                and enemy.y < self.player.y + self.player.height
                and enemy.y + enemy.height > self.player.y
            ):
                self.game.lives -= 1
                self.enemies.remove(enemy)
                if self.game.lives <= 0:
                    self.game.finish_game(False)
                    return
                break

        if not self.enemies:
            self.game.finish_game(True)

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BLACK)
        self.player.draw(screen)
        for bullet in self.bullets:
            pygame.draw.rect(screen, WHITE, (bullet["x"], bullet["y"], 6, 10))
        for enemy in self.enemies:
            enemy.draw(screen)
        for powerup in self.powerups:
            powerup.draw(screen)
        score_surface = self.font.render(f"Puntuación: {self.game.score}", True, WHITE)
        lives_surface = self.font.render(f"Vidas: {self.game.lives}", True, RED)
        screen.blit(score_surface, (20, 20))
        screen.blit(lives_surface, (20, 50))
        if self.game.paused:
            pause_surface = self.font.render("PAUSA", True, WHITE)
            screen.blit(pause_surface, (WIDTH // 2 - pause_surface.get_width() // 2, HEIGHT // 2 - pause_surface.get_height() // 2))
