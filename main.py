import sys
from pathlib import Path

from config.settings import WIDTH, HEIGHT, FPS
from core.game import Game


def main() -> None:
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
