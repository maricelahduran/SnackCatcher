# Requerimientos - Space Invaders

## 1. Objetivo del sistema
Desarrollar un videojuego tipo Space Invaders en Python utilizando Pygame, donde el jugador controle una nave, evite a los enemigos y pueda eliminarlos mediante disparos.

## 2. Alcance
El sistema debe incluir:
- Pantalla de inicio
- Pantalla de carga
- Pantalla de configuración
- Jugabilidad principal
- Sistema de vidas
- Sistema de disparos
- Selección de dificultad y enemigos
- Sistema básico de puntuación
- Modo pausa y reinicio de partida

## 3. Requisitos funcionales

### RF-01: Pantalla de inicio
El sistema debe mostrar una pantalla de inicio al iniciar la aplicación.
- Debe mostrar el nombre del juego.
- Debe permitir ingresar un nombre de jugador.
- Debe permitir iniciar una nueva partida.
- Debe permitir acceder a la configuración.
- Si el nombre del jugador está vacío, debe asignarse un valor por defecto como "Jugador".

### RF-02: Pantalla de carga
El sistema debe mostrar una pantalla de carga antes de iniciar una partida.
- Debe aparecer al iniciar una nueva partida.
- Debe indicar que el juego está cargando los recursos.
- Debe transicionar automáticamente a la pantalla de juego en un tiempo breve.

### RF-03: Pantalla de configuración
El sistema debe permitir al jugador configurar el juego antes de iniciar la partida.
- Debe permitir seleccionar la dificultad de los enemigos.
- Debe permitir seleccionar uno o varios enemigos para la partida.
- Debe permitir activar o desactivar power-ups.
- Debe permitir activar una opción de configuración aleatoria.
- Debe permitir guardar o aplicar la configuración seleccionada.
- Si no se selecciona ningún enemigo, el sistema debe usar una configuración por defecto con todos los enemigos disponibles.

### RF-04: Movimiento de la nave
El sistema debe permitir que la nave se mueva de izquierda a derecha.
- El movimiento debe controlarse con las flechas del teclado.
- La nave no debe salir de los límites horizontales de la pantalla.

### RF-05: Disparo de la nave
El sistema debe permitir que la nave dispare al presionar la tecla espacio.
- El disparo debe generarse desde la posición frontal de la nave.
- El disparo debe moverse hacia arriba.
- El disparo debe eliminar o dañar a los enemigos si colisiona con ellos.
- El disparo no debe atravesar indefinidamente la pantalla; debe eliminarse al salir de la misma.

### RF-06: Enemigos en pantalla
El sistema debe mostrar enemigos en la parte superior de la pantalla.
- Los enemigos deben aparecer en la zona superior del escenario.
- Deben moverse horizontalmente y descender progresivamente durante la partida.
- Deben afectar al jugador al colisionar con la nave.

### RF-07: Colisión con la nave
El sistema debe detectar colisiones entre los enemigos y la nave.
- Si un enemigo impacta con la nave, el jugador debe perder una vida.
- Si un enemigo alcanza la zona inferior de la pantalla, la partida debe terminar.
- Si el jugador se queda sin vidas, la partida debe terminar.

### RF-08: Sistema de vidas y puntuación
El sistema debe implementar un sistema de vidas y puntuación para el jugador.
- El jugador debe iniciar con 3 vidas.
- Cada colisión con un enemigo debe disminuir una vida.
- Cada enemigo destruido debe incrementar la puntuación del jugador.
- La partida debe terminar cuando el jugador pierda todas sus vidas o cuando se cumpla la condición de victoria definida.

### RF-09: Dificultad de los enemigos
El sistema debe permitir ajustar la dificultad de los enemigos.
- Debe existir al menos una opción de dificultad fácil, media y difícil.
- La dificultad debe modificar al menos los siguientes parámetros: velocidad de los enemigos, frecuencia de aparición y cantidad de daño recibido por la nave.

### RF-10: Selección de enemigos
El sistema debe permitir seleccionar los enemigos que participarán en la partida.
- Debe permitirse elegir un solo enemigo.
- Debe permitirse elegir varios enemigos.
- Debe existir un conjunto mínimo de enemigos disponibles: básico, rápido y resistente.
- Si no se selecciona ninguno, se usará la configuración por defecto con todos los enemigos disponibles.

### RF-11: Power-ups
El sistema debe permitir la activación de power-ups en la partida.
- En el MVP debe existir al menos un power-up: disparo doble.
- Si el power-up está habilitado, debe aparecer de forma aleatoria durante la partida.
- Al activarse, debe modificar temporalmente el comportamiento del disparo del jugador.

### RF-12: Juego principal
El sistema debe iniciar una partida válida una vez seleccionada la configuración.
- La partida debe mostrar la nave, los enemigos y los indicadores de estado del jugador.
- El juego debe mantenerse en ejecución hasta que el jugador pierda todas sus vidas, elimine a todos los enemigos o decida salir.
- El jugador debe poder pausar y reanudar la partida con la tecla Escape.
- El jugador debe poder reiniciar la partida desde la pantalla de fin de juego.

## 4. Reglas de negocio
- La nave solo puede moverse horizontalmente.
- Los disparos solo deben avanzar en una dirección.
- Los enemigos deben descender progresivamente durante la partida.
- La dificultad debe afectar la experiencia de juego.
- La configuración elegida debe aplicarse antes de iniciar la partida.
- La puntuación debe actualizarse en tiempo real durante la partida.
- La partida debe mostrar un estado claro de victoria o derrota al finalizar.

## 5. Requisitos no funcionales

### RNF-01: Tecnológico
- El juego debe desarrollarse en Python.
- Debe utilizar la librería Pygame.

### RNF-02: Rendimiento
- El juego debe ejecutarse de forma fluida en una computadora estándar.
- La lógica de movimiento y colisiones debe responder sin retrasos significativos.

### RNF-03: Usabilidad
- Los controles deben ser intuitivos.
- La interfaz debe ser clara para un jugador nuevo.
- Los textos de menú y juego deben ser legibles.

### RNF-04: Compatibilidad
- El juego debe poder ejecutarse en un entorno con Python y Pygame instalados.

## 6. Criterios de aceptación

### CA-01
Si el jugador inicia la aplicación, debe ver la pantalla de inicio.

### CA-02
Si el jugador selecciona iniciar partida, debe aparecer la pantalla de carga y luego el juego.

### CA-03
Si el jugador usa las flechas del teclado, la nave debe moverse de izquierda a derecha sin salir de los límites de la pantalla.

### CA-04
Si el jugador presiona espacio, debe aparecer un disparo desde la nave y este debe moverse hacia arriba.

### CA-05
Si un enemigo colisiona con la nave, el jugador debe perder una vida.

### CA-06
Si el jugador selecciona una dificultad, esa configuración debe aplicarse en la partida.

### CA-07
Si el jugador elige un enemigo específico o varios, esos enemigos deben aparecer en la partida.

### CA-08
Si el jugador elimina a todos los enemigos, debe mostrarse un estado de victoria y la partida debe finalizar.

### CA-09
Si el jugador presiona Escape durante la partida, el juego debe pausar o reanudar según el estado actual.

## 7. Versión propuesta de MVP
Para una primera versión, se recomienda implementar:
- Pantalla de inicio
- Pantalla de carga
- Pantalla de configuración básica
- Movimiento de la nave
- Disparos
- Enemigos con movimiento descendente
- Sistema de vidas
- Sistema de puntuación
- Dificultad simple
- Selección de enemigos
- Power-up de disparo doble
- Pausa y reinicio de partida
