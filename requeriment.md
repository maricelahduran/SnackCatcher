# Requerimientos - Snack Catcher (Recolector de Chips)

## 1. Objetivo del sistema
Desarrollar un videojuego casual tipo arcade en Python utilizando Pygame, donde el jugador controle un recolector en la parte inferior de la pantalla para atrapar los snacks que caen, evitando obstáculos y subiendo de nivel mediante un sistema de puntuación acumulativo.

## 2. Alcance
El sistema debe incluir:
- Pantalla de inicio (Menú principal con ingreso de nombre)
- Pantalla de carga de recursos
- Pantalla de configuración (Dificultad y selección de snacks activos)
- Jugabilidad principal en pantalla dividida (Área de juego y Barra de nivel)
- Sistema de vidas mediante corazones
- Mecánica de caída aleatoria de objetos (Snacks benéficos y obstáculos)
- Barra de progreso de nivel vertical a la derecha de la pantalla
- Modo pausa y reinicio de partida

## 3. Requisitos funcionales

### RF-01: Pantalla de inicio
El sistema debe mostrar una pantalla de inicio al iniciar la aplicación.
- Debe mostrar el nombre del juego (ej. *Snack Catcher*).
- Debe permitir ingresar el nombre del jugador. Si se deja vacío, se asignará "Invitado".
- Debe tener botones para "Iniciar Partida" y "Configuración".

### RF-02: Pantalla de carga
El sistema debe mostrar una pantalla de transición breve antes de la jugabilidad.
- Debe indicar de forma visual que los recursos (imágenes de los chips, sonidos) se están cargando.
- Pasará automáticamente al juego una vez completado el proceso.

### RF-03: Pantalla de configuración
El sistema debe permitir personalizar los parámetros de la partida.
- **Dificultad:** Modificará la velocidad inicial de caída y la frecuencia de los objetos.
- **Filtro de Snacks:** Permitirá activar o desactivar qué tipos de snacks aparecerán.
- **Opción Aleatoria:** Configura un ecosistema de juego con parámetros al azar.
- Si no se toca nada, el juego iniciará con la configuración estándar (todos los snacks activos en dificultad media).

### RF-04: El Recolector (Jugador)
El sistema debe permitir controlar el contenedor de snacks en la base de la pantalla.
- Se moverá únicamente de forma horizontal (izquierda/derecha) usando las flechas del teclado o el movimiento del mouse.
- No debe ser capaz de rebasar los límites laterales asignados al área de juego.

### RF-05: Generación y caída de Snacks
El sistema debe hacer caer objetos desde la parte superior de forma continua y aleatoria.
- Cada objeto aparecerá en una coordenada X al azar dentro del área de juego.
- Los objetos caerán verticalmente hacia abajo con velocidades independientes según su tipo.

### RF-06: Tipos de Objetos (Snacks y Obstáculos)
El sistema debe contar con al menos tres variantes de objetos con comportamientos distintos:
1. **Chip Clásico:** Caída a velocidad normal. Otorga +10 puntos al ser atrapado.
2. **Dorito de Fuego:** Caída rápida. Otorga +25 puntos al ser atrapado.
3. **Chip Quemado (Obstáculo):** Caída irregular. Si el jugador lo atrapa por accidente, resta 1 vida (un corazón).

### RF-07: Sistema de Vidas (Corazones) y Penalizaciones
El sistema debe controlar la salud del jugador mediante un límite de fallos.
- El jugador iniciará la partida con 3 vidas (representadas por corazones en la interfaz).
- **Penalización por descuido:** Si un chip válido (Clásico o Dorito) toca el suelo sin ser recolectado, el jugador pierde 1 vida.
- **Puntuación mínima:** Los puntos acumulados nunca podrán descender de cero (0).
- Si las vidas llegan a 0, la partida terminará inmediatamente enviando al usuario a la pantalla de Fin de Juego.

### RF-08: Barra de Nivel Vertical (Interfaz Derecha)
El sistema debe incluir un panel lateral derecho dedicado al progreso del nivel.
- La pantalla estará dividida: 85% para el área de juego y 15% para el panel de nivel.
- Contendrá una barra vertical que se rellenará proporcionalmente al puntaje actual del jugador.
- **Mecánica de Level Up:** Cada 100 puntos acumulados, el jugador sube de nivel, la barra se vacía y la velocidad general de caída de los snacks aumenta un 15%.

### RF-09: Juego Principal e Interfaz (HUD)
El sistema debe integrar todos los componentes en el bucle principal de juego.
- En la parte superior del área de juego se mostrarán de forma clara: el puntaje actual, el nivel alcanzado y los corazones restantes.
- Presionar la tecla **Escape** pausará el juego, congelando la caída de los objetos.
- Al perder, se mostrará la pantalla de derrotado con la puntuación final lograda y la opción de "Reiniciar Partida" o "Volver al Menú".

## 4. Reglas de negocio
- El recolector solo tiene permitido el desplazamiento en el eje horizontal.
- Los objetos que salgan de la pantalla por la parte inferior (hayan sido atrapados o no) deben ser destruidos de la memoria del sistema.
- Subir de nivel debe aplicar el incremento de velocidad de manera inmediata en los objetos activos en pantalla.
- Un obstáculo (Chip Quemado) que toque el suelo de forma limpia no penalizará al jugador; solo hace daño si es atrapado.

## 5. Requisitos no funcionales

### RNF-01: Tecnológico
- El juego se desarrollará en el lenguaje Python utilizando exclusivamente la librería Pygame para el motor de juego y renderizado.

### RNF-02: Rendimiento
- El juego debe mantener una tasa estable de 60 FPS en hardware comercial estándar, garantizando que el refresco de las colisiones sea preciso y fluido.

### RNF-03: Usabilidad
- La división de la pantalla debe ser intuitiva; la barra de nivel debe ser lo suficientemente vistosa (cambio de color o destello al subir de nivel) para alertar al jugador sin distraerlo de la caída de los chips.

## 6. Criterios de aceptación

### CA-01: Inicio y Registro
Al abrir el juego, se despliega el menú principal. Si el usuario da clic en jugar sin poner nombre, el HUD de juego debe mostrar el texto "Jugador: Invitado".

### CA-02: Movimiento Limitado
Al arrastrar el mouse o presionar las flechas hacia los extremos, el recolector debe detenerse en seco justo en los bordes del área de juego, sin invadir el panel de la barra de nivel a la derecha.

### CA-03: Detección de Colisiones
- Si la caja de colisión (hitbox) del recolector toca un *Chip Clásico*, el marcador debe sumar 10 puntos de inmediato.
- Si toca un *Chip Quemado*, el contador de corazones debe disminuir en 1.

### CA-04: Transición de Nivel
Al llegar exactamente a 100 puntos, la barra lateral debe vaciarse por completo, el indicador de nivel debe cambiar de "Nivel 1" a "Nivel 2" y los objetos en pantalla deben acelerar visiblemente su descenso.

### CA-05: Game Over por Descuido
Si el jugador permite que 3 snacks saludables toquen el fondo de la pantalla, el juego se detiene y redirige a la interfaz de puntuación final.

## 7. Alcance del MVP (Mínimo Producto Viable)
Para la primera versión funcional en desarrollo local, se priorizará:
1. Ventana de juego con la pantalla dividida (Área izquierda y contenedor de la barra derecha).
2. Movimiento fluido del recolector en la base.
3. Lógica de caída y colisión para el *Chip Clásico* y el *Chip Quemado*.
4. Sistema de puntuación, barra de nivel funcional que se llene hasta los 100 puntos y el contador de 3 vidas.
5. Pantalla básica de reinicio al perder las vidas.