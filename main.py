import random
import pygame
from src.s_config import (
    WIDTH,
    HEIGHT,
    FPS,
    BLACK,
    WHITE,
    GRAY,
    LIGHT_GRAY,
    BLUE,
    YELLOW,
    RED,
    GAME_AREA_WIDTH,
    PANEL_WIDTH,
    BASE_FALL_SPEED,
    LEVEL_SPEED_MULTIPLIER,
    SCORE_CLASSIC,
    START_LIVES,
    PROGRESS_BAR_PADDING,
    PROGRESS_BAR_WIDTH,
)

from src.entities.player import Player
from src.entities.snack import Snack


SPAWN_EVENT = pygame.USEREVENT + 1
SPAWN_INTERVAL_MS = 1000


def reset_game_state(state: dict, player: Player, snack_group: pygame.sprite.Group) -> None:
    state["score"] = 0
    state["lives"] = START_LIVES
    state["level"] = 1
    state["speed_multiplier"] = 1.0
    state["game_over"] = False
    snack_group.empty()
    # reposition player
    player.reset_position(GAME_AREA_WIDTH // 2 - player.width // 2, HEIGHT - player.height - 10)
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_INTERVAL_MS)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snack Catcher")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    # create player and groups
    player = Player(GAME_AREA_WIDTH // 2 - 30, HEIGHT - 34)
    player_group = pygame.sprite.GroupSingle(player)
    snack_group = pygame.sprite.Group()

    # game state
    state = {
        "running": True,
        "paused": False,
        "game_over": False,
        "score": 0,
        "lives": START_LIVES,
        "level": 1,
        "speed_multiplier": 1.0,
    }

    # start spawn timer
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_INTERVAL_MS)

    while state["running"]:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["running"] = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state["paused"] = not state["paused"]
                elif event.key == pygame.K_SPACE and state["game_over"]:
                    # restart
                    reset_game_state(state, player, snack_group)
                elif event.key == pygame.K_q:
                    state["running"] = False
            elif event.type == SPAWN_EVENT and not state["paused"] and not state["game_over"]:
                # spawn a snack: 25% chance burned
                snack_type = "quemado" if random.random() < 0.25 else "normal"
                snack = Snack(snack_type, fall_speed=BASE_FALL_SPEED)
                snack_group.add(snack)

        keys = pygame.key.get_pressed()

        if not state["paused"] and not state["game_over"]:
            # update player
            player.update(keys, dt)

            # update snacks
            for s in list(snack_group.sprites()):
                s.update(dt, state["speed_multiplier"])
                # penalize missed normal snacks
                if s.rect.top > HEIGHT:
                    if s.snack_type == "normal":
                        state["lives"] -= 1
                    snack_group.remove(s)

            # check collisions: player catches snacks
            caught = pygame.sprite.spritecollide(player, snack_group, dokill=True)
            for s in caught:
                if s.snack_type == "normal":
                    state["score"] += SCORE_CLASSIC
                    # level up check (every 100 points)
                    while state["score"] >= state["level"] * 100:
                        state["level"] += 1
                        state["speed_multiplier"] *= LEVEL_SPEED_MULTIPLIER
                else:
                    state["lives"] -= 1

            if state["lives"] <= 0:
                state["game_over"] = True
                # stop spawn while game over
                pygame.time.set_timer(SPAWN_EVENT, 0)

        # render
        screen.fill(BLACK)

        # draw game area
        game_area_rect = pygame.Rect(0, 0, GAME_AREA_WIDTH, HEIGHT)
        pygame.draw.rect(screen, GRAY, game_area_rect)
        pygame.draw.rect(screen, WHITE, game_area_rect, 4)

        # draw panel
        panel_rect = pygame.Rect(GAME_AREA_WIDTH, 0, PANEL_WIDTH, HEIGHT)
        pygame.draw.rect(screen, LIGHT_GRAY, panel_rect)

        # draw progress bar background
        progress_x = GAME_AREA_WIDTH + (PANEL_WIDTH - PROGRESS_BAR_WIDTH) // 2
        progress_y = PROGRESS_BAR_PADDING
        progress_height = HEIGHT - 2 * PROGRESS_BAR_PADDING
        pygame.draw.rect(screen, GRAY, (progress_x, progress_y, PROGRESS_BAR_WIDTH, progress_height))

        # progress calculated from score modulo 100
        progress_ratio = (state["score"] % 100) / 100.0
        filled_height = int(progress_height * progress_ratio)
        filled_y = progress_y + progress_height - filled_height
        pygame.draw.rect(screen, BLUE, (progress_x, filled_y, PROGRESS_BAR_WIDTH, filled_height))

        # draw sprites
        snack_group.draw(screen)
        player_group.draw(screen)

        # HUD text
        hud_surf = font.render(f"Vidas: {state['lives']}   Puntaje: {state['score']}   Nivel: {state['level']}", True, WHITE)
        screen.blit(hud_surf, (12, 12))

        if state["paused"]:
            p = font.render("PAUSA - Presiona ESC para continuar", True, WHITE)
            screen.blit(p, (GAME_AREA_WIDTH // 2 - p.get_width() // 2, HEIGHT // 2 - 10))

        if state["game_over"]:
            go = font.render("GAME OVER - Presiona ESPACIO para reiniciar", True, RED)
            screen.blit(go, (GAME_AREA_WIDTH // 2 - go.get_width() // 2, HEIGHT // 2 - 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
