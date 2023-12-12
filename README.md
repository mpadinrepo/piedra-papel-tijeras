# piedra-papel-tijeras
Práctica del Curso Especialización de Inteligencia Artificial y Big Data

Alumno MPADIN de IA y BigDATA TEIS (VIGO)


Tarea 3.23
Ejercicio:

Especifica as características do contorno de tarefas do RPS

--> Contorno de tarefas

| Contorno de tarefas | Observable | Axentes | Determinista | Episódico | Estático | Discreto | Coñecido |
|:---------------------:|:-----------:|:--------:|:--------------:|:-----------:|:----------:|:----------:|:----------:|
| Piedra Papel y Tijeras                           | No                     | Multi                | No                        | Sí                      | Sí                    | Sí                    | Sí                      |

Observable: El contorno de tareas RPS no es completamente observable, ya que los jugadores no conocen la elección del oponente hasta que se revela.

Axentes: En el juego RPS, hay múltiples agentes (jugadores) interactuando entre sí.

Determinista: No es determinista, ya que la elección de cada jugador (agente) no se puede predecir con certeza.

Episódico: Sí es episódico, ya que cada partida es independiente y no depende del historial de partidas anteriores.

Estático: Sí es estático, ya que las reglas del juego no cambian durante una partida.

Discreto: Sí es discreto, ya que hay un número finito y discreto de acciones posibles (piedra, papel o tijeras).

Coñecido: Sí es conocido, ya que las reglas del juego son conocidas por todos los jugadores.

Tarea 3.24
Ejercicio:
Debuxa un modelo adecuado ao contorno de tarefas e a un dos catro tipos de programas axente


Para el juego de "piedra, papel o tijeras", un agente reactivo puede ser una opción adecuada. Un agente reactivo toma decisiones basadas directamente en la percepción del entorno en un momento dado, sin mantener un historial de acciones anteriores. En este caso, el agente reacciona a la elección más reciente del oponente y elige una acción que tenga probabilidades de ser exitosa.

      +---[Piedra]---+
      |              |
      v              |
   [Agente] ------->|---------[ Tijeras ]
      |              |
      +---[Papel]----+


Características del Agente Reactivo:
1) Percepción: Observa el estado actual del juego, es decir, la última elección del oponente.
2) Acción: Decide la siguiente acción basándose en la elección del oponente actual.
    · Ejemplo de Lógica: Si el oponente eligió "piedra" en la última jugada, el agente podría elegir "papel" para ganar.
3) Sin Memoria: No mantiene un historial de las elecciones pasadas.
