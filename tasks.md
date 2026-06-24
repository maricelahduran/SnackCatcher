# Fase 3 SDD - Plan de tareas de desarrollo

## 1. Objetivo
Convertir los requisitos y el diseño en tareas de desarrollo con trazabilidad clara, priorizadas y listas para implementar en el proyecto Space Invaders.

## 2. Convención de trazabilidad
Cada tarea tiene:
- ID de tarea: TSK-XX
- Requisitos relacionados: RF-XX
- Secciones de diseño relacionadas: Sección X.Y
- Prioridad: Alta / Media / Baja
- Tipo: Funcional / Infraestructura / UI / QA

## 3. Epic 1 - Base del proyecto

### TSK-01: Crear estructura inicial del proyecto
- Descripción: Crear la estructura de carpetas y archivos base del proyecto según el diseño.
- Requisitos: RF-01, RF-02, RF-12
- Diseño: Sección 4, Sección 5, Sección 10
- Prioridad: Alta
- Tipo: Infraestructura
- Criterio de aceptación: El proyecto cuenta con los módulos principales creados y ejecutables desde main.py.

### TSK-02: Definir modelos de configuración y estado
- Descripción: Implementar las clases GameConfig y GameState con los campos definidos en el diseño.
- Requisitos: RF-03, RF-08, RF-09, RF-12
- Diseño: Sección 7.1, Sección 7.2, Sección 8
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: Los objetos permiten almacenar la configuración de partida y el estado del juego.

## 4. Epic 2 - Motor del juego y flujo de pantallas

### TSK-03: Implementar loop principal del juego
- Descripción: Crear el ciclo principal de ejecución con manejo de eventos, actualización, colisiones y renderizado.
- Requisitos: RF-12
- Diseño: Sección 10
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: El juego entra en ejecución y actualiza el estado correctamente en cada frame.

### TSK-04: Implementar gestión de estados de pantalla
- Descripción: Manejar transiciones entre pantalla de inicio, carga, configuración, juego, pausa y fin de partida.
- Requisitos: RF-01, RF-02, RF-03, RF-12
- Diseño: Sección 5, Sección 8
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: El juego cambia de estado correctamente según la interacción del usuario.

## 5. Epic 3 - Pantallas de usuario

### TSK-05: Implementar pantalla de inicio
- Descripción: Mostrar el título, el campo de nombre del jugador y los botones de iniciar y configuración.
- Requisitos: RF-01
- Diseño: Sección 5.1
- Prioridad: Alta
- Tipo: UI
- Criterio de aceptación: El usuario puede ingresar su nombre y entrar a la partida o la configuración.

### TSK-06: Implementar pantalla de carga
- Descripción: Mostrar una pantalla temporal de carga antes de iniciar la partida.
- Requisitos: RF-02
- Diseño: Sección 5.2
- Prioridad: Media
- Tipo: UI
- Criterio de aceptación: Se muestra la pantalla de carga y luego se inicia la partida.

### TSK-07: Implementar pantalla de configuración
- Descripción: Permitir seleccionar dificultad, enemigos, power-ups y modo aleatorio.
- Requisitos: RF-03, RF-09, RF-10, RF-11
- Diseño: Sección 5.3, Sección 7.3
- Prioridad: Alta
- Tipo: UI
- Criterio de aceptación: La configuración seleccionada se guarda y se aplica al iniciar la partida.

### TSK-08: Implementar pantalla de fin de juego
- Descripción: Mostrar el resultado final, la puntuación y opciones para reiniciar o volver al menú.
- Requisitos: RF-08, RF-12
- Diseño: Sección 5.5
- Prioridad: Media
- Tipo: UI
- Criterio de aceptación: El jugador puede reiniciar la partida o volver al menú desde esta pantalla.

## 6. Epic 4 - Jugabilidad principal

### TSK-09: Implementar movimiento de la nave
- Descripción: Controlar el movimiento horizontal de la nave con las flechas del teclado y limitar sus bordes.
- Requisitos: RF-04
- Diseño: Sección 6.1, Sección 11
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: La nave se mueve correctamente y no sale de los límites de la pantalla.

### TSK-10: Implementar disparo de la nave
- Descripción: Permitir disparar con la tecla espacio y crear balas que suben por la pantalla.
- Requisitos: RF-05
- Diseño: Sección 6.3, Sección 11
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: Al presionar espacio aparece un disparo y se elimina cuando sale de la pantalla.

### TSK-11: Implementar enemigos y su movimiento
- Descripción: Crear enemigos en la parte superior, moverlos horizontalmente y hacer que desciendan progresivamente.
- Requisitos: RF-06, RF-09, RF-10
- Diseño: Sección 6.2, Sección 7.3
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: Los enemigos aparecen según la configuración y se mueven de forma continua.

### TSK-12: Implementar colisiones y eliminación de entidades
- Descripción: Detectar colisiones entre balas y enemigos, y entre enemigos y nave.
- Requisitos: RF-05, RF-07, RF-12
- Diseño: Sección 12
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: Las balas eliminan o dañan a los enemigos y las colisiones con la nave reducen vidas.

### TSK-13: Implementar sistema de vidas y puntuación
- Descripción: Mantener el contador de vidas y la puntuación del jugador durante la partida.
- Requisitos: RF-08, RF-12
- Diseño: Sección 7.2, Sección 7.3
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: La puntuación aumenta al destruir enemigos y las vidas disminuyen correctamente.

### TSK-14: Implementar condiciones de victoria y derrota
- Descripción: Finalizar la partida cuando se pierden todas las vidas, se eliminan todos los enemigos o un enemigo alcanza la parte inferior.
- Requisitos: RF-07, RF-08, RF-12
- Diseño: Sección 7.3, Sección 12
- Prioridad: Alta
- Tipo: Funcional
- Criterio de aceptación: La partida termina con un estado claro de victoria o derrota.

### TSK-15: Implementar pausa y reinicio de partida
- Descripción: Permitir pausar y reanudar con Escape, así como reiniciar la partida desde la pantalla final.
- Requisitos: RF-12
- Diseño: Sección 8, Sección 11
- Prioridad: Media
- Tipo: Funcional
- Criterio de aceptación: La partida se pausa y reanuda correctamente y el reinicio funciona.

## 7. Epic 5 - Funcionalidades extendidas del MVP

### TSK-16: Implementar power-up de disparo doble
- Descripción: Crear un power-up que aparezca aleatoriamente y modifique temporalmente el comportamiento del disparo del jugador.
- Requisitos: RF-11
- Diseño: Sección 6.4, Sección 12
- Prioridad: Media
- Tipo: Funcional
- Criterio de aceptación: Si está habilitado, el power-up aparece y activa el disparo doble durante un tiempo limitado.

### TSK-17: Implementar dificultad configurable
- Descripción: Aplicar diferentes niveles de dificultad al juego mediante velocidad, frecuencia de aparición y daño de enemigos.
- Requisitos: RF-09
- Diseño: Sección 7.3, Sección 9.2
- Prioridad: Media
- Tipo: Funcional
- Criterio de aceptación: La dificultad seleccionada modifica el comportamiento del juego de forma visible.

### TSK-18: Implementar selección de enemigos y modo aleatorio
- Descripción: Permitir elegir un conjunto de enemigos, usar configuración por defecto y activar la opción aleatoria.
- Requisitos: RF-03, RF-10
- Diseño: Sección 5.3, Sección 7.3
- Prioridad: Media
- Tipo: Funcional
- Criterio de aceptación: La partida usa la selección de enemigos indicada o la configuración por defecto cuando no hay selección.

## 8. Epic 6 - Calidad y validación

### TSK-19: Realizar pruebas funcionales del MVP
- Descripción: Validar que cada requisito principal funciona como se espera desde la experiencia del usuario.
- Requisitos: RF-01 a RF-12
- Diseño: Sección 16
- Prioridad: Alta
- Tipo: QA
- Criterio de aceptación: Se ejecutan las pruebas de aceptación y no quedan fallos críticos en el flujo principal.

## 9. Orden sugerido de implementación
1. TSK-01, TSK-02, TSK-03, TSK-04
2. TSK-05, TSK-06, TSK-07, TSK-08
3. TSK-09, TSK-10, TSK-11, TSK-12, TSK-13, TSK-14, TSK-15
4. TSK-16, TSK-17, TSK-18
5. TSK-19

## 10. Estado de seguimiento
- [ ] TSK-01
- [ ] TSK-02
- [ ] TSK-03
- [ ] TSK-04
- [ ] TSK-05
- [ ] TSK-06
- [ ] TSK-07
- [ ] TSK-08
- [ ] TSK-09
- [ ] TSK-10
- [ ] TSK-11
- [ ] TSK-12
- [ ] TSK-13
- [ ] TSK-14
- [ ] TSK-15
- [ ] TSK-16
- [ ] TSK-17
- [ ] TSK-18
- [ ] TSK-19
