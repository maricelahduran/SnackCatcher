"""Configuración base para el juego Snack Catcher."""

# Pantalla y velocidad
WIDTH = 800
HEIGHT = 600
FPS = 60

# División de la pantalla: 85% área de juego izquierda, 15% panel derecho
PANEL_RATIO = 0.15
GAME_AREA_WIDTH = int(WIDTH * (1.0 - PANEL_RATIO))
PANEL_WIDTH = WIDTH - GAME_AREA_WIDTH

# Colores RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 30, 30)
GREEN = (80, 200, 120)
BLUE = (70, 130, 255)
YELLOW = (244, 208, 63)
GRAY = (40, 40, 40)
LIGHT_GRAY = (100, 100, 100)

# Valores de juego
START_LIVES = 3
START_SCORE = 0
START_LEVEL = 1
START_PROGRESS = 0.0

# Mecánica de caída y niveles
BASE_FALL_SPEED = 180
LEVEL_SPEED_MULTIPLIER = 1.15
PROGRESS_INCREMENT_PER_SECOND = 0.20

# Puntajes y vidas
SCORE_CLASSIC = 10
LIFE_LOSS_MISSED_CLASSIC = 1
LIFE_LOSS_BURNED_SNACK = 1

# Medidor de progreso del panel derecho
PROGRESS_BAR_PADDING = 20
PROGRESS_BAR_WIDTH = 40
PROGRESS_BAR_COLOR = BLUE
PROGRESS_BAR_BG = GRAY
