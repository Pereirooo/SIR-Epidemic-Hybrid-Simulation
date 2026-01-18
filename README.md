# Simulación Híbrida de Propagación Epidémica: EBM vs ABM

## 1. Introducción
Este proyecto presenta un estudio comparativo de la dinámica de una epidemia utilizando dos filosofías de modelado distintas, tal como se discute en la asignatura de Métodos Numéricos:
1.  **Equation-Based Modeling (EBM):** Un enfoque *top-down* basado en ecuaciones diferenciales.
2.  **Agent-Based Modeling (ABM):** Un enfoque *bottom-up* basado en la interacción de agentes autónomos.

El objetivo es visualizar cómo las reglas locales de los agentes generan un comportamiento emergente que valida (o desafía) los modelos matemáticos tradicionales.

## 2. Modelado Matemático (EBM)
Para la resolución numérica, implementamos el modelo **SIR** (Susceptibles, Infectados, Recuperados). El sistema se rige por las siguientes ecuaciones diferenciales ordinarias (ODEs):

$$\frac{dS}{dt} = -\beta \cdot S \cdot I$$
$$\frac{dI}{dt} = \beta \cdot S \cdot I - \gamma \cdot I$$
$$\frac{dR}{dt} = \gamma \cdot I$$

### Algoritmo Numérico
Se ha utilizado el **Método de Euler** para aproximar la solución de las ecuaciones en cada paso de tiempo $\Delta t$:
$$y_{n+1} = y_n + f(t_n, y_n) \cdot \Delta t$$

Este método permite transformar un problema continuo en uno discreto ejecutable por el computador, manteniendo un equilibrio entre complejidad computacional y precisión.

## 3. Modelado Basado en Agentes (ABM)
A diferencia del modelo macro, el ABM simula 200 individuos con las siguientes propiedades:
* **Estado:** Cada agente posee un estado discreto $\{0: Sano, 1: Infectado, 2: Recuperado\}$.
* **Movimiento:** Implementado mediante vectores de velocidad aleatorios que simulan el desplazamiento humano en un entorno cerrado.
* **Emergencia:** La curva de contagio no está predefinida; surge de las colisiones y la proximidad física entre agentes infectados y sanos (radio de contagio).

## 4. Comparativa y Resultados
La simulación muestra en tiempo real cómo:
1.  El modelo **EBM** (línea discontinua) predice una curva suave y determinista.
2.  El modelo **ABM** (línea continua) presenta fluctuaciones estocásticas propias de sistemas reales.
3.  A medida que el número de agentes ($N$) aumenta, el comportamiento del ABM converge hacia la solución del EBM, validando la precisión de nuestros métodos numéricos.

## 5. Instalación y Ejecución
Para ejecutar esta simulación, asegúrese de tener instaladas las dependencias necesarias:

```bash
pip install numpy matplotlib
