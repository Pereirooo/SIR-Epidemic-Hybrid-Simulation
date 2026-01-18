# Comparative Study of Epidemic Dynamics: Equation-Based Modeling (EBM) vs Agent-Based Modeling (ABM)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Course Project: Numerical Methods & Simulation**
> This project implements a hybrid simulation to analyze the spread of epidemics through two opposing paradigms: the deterministic macroscopic approach (Top-Down) and the stochastic microscopic approach (Bottom-Up).

---

## 📋 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [Visual Demo](#-visual-demo)
3. [Mathematical Foundation (EBM)](#-mathematical-foundation-ebm)
4. [Agent Logic (ABM)](#-agent-logic-abm)
5. [Comparative Analysis and Emergence](#-comparative-analysis-and-emergence)
6. [Project Structure](#-project-structure)
7. [Installation and Usage](#-installation-and-usage)

---

## 🚀 Executive Summary

The main objective is to model an **SIR** (Susceptible, Infected, Recovered) type epidemic by contrasting two methodologies:
1.  **Equation-Based Modeling (EBM):** Numerical resolution of a system of Ordinary Differential Equations (ODEs) using the **Euler Method**. It assumes a homogeneous ("well-mixed") population.
2.  **Agent-Based Modeling (ABM):** Simulation of autonomous individuals interacting in a 2D space. It introduces spatial heterogeneity and stochasticity.

The project demonstrates how global behavior (the infection curve) **emerges** from local interactions, validating the numerical approximation.

---

## 🎥 Visual Demo

### Real-Time Simulation (ABM)
*Visualization of agent interaction in a closed space. Red: Infected, Blue: Susceptible, Green: Recovered.*

![Agent Simulation GIF](assets/simulation.gif)
*(Ensure the simulation.gif file is located in the assets/ folder)*

### Cross-Validation (EBM vs ABM)
*Real-time comparison between the theoretical prediction (dashed line) and the simulated reality (solid line).*

![Comparative Chart](assets/comparison_chart.gif)
*(You can use the same GIF if it captures both, or a static screenshot here)*

---

## 📐 Mathematical Foundation (EBM)

The macroscopic model is governed by the SIR deterministic differential equation system:

$$
\begin{aligned}
\frac{dS}{dt} &= -\beta \cdot S \cdot I \\
\frac{dI}{dt} &= \beta \cdot S \cdot I - \gamma \cdot I \\
\frac{dR}{dt} &= \gamma \cdot I
\end{aligned}
$$

Where:
* $\beta$: Transmission rate (infection probability $\times$ contact rate).
* $\gamma$: Recovery rate ($1 / \text{infection days}$).

### Numerical Implementation
Given the continuous nature of the equations, we use the **Euler Method** to discretize time and solve the system computationally:

$$y_{n+1} = y_n + f(t_n, y_n) \cdot \Delta t$$

Although higher-order methods such as Runge-Kutta (RK4) exist, the Euler Method offers a suitable balance between **computational cost** and **accuracy** for the scale of this simulation, allowing for fast real-time iterations.

---

## 🤖 Agent Logic (ABM)

The microscopic model (Bottom-Up) simulates $N$ autonomous agents. Unlike EBM, there are no global equations here, but rather **local rules**:

1.  **State:** Each agent $a_i$ has a state $s \in \{0: \text{Susceptible}, 1: \text{Infected}, 2: \text{Recovered}\}$.
2.  **Kinematics:** Continuous vector movement in a bounded space with elastic bounce at borders (reflective boundary conditions).
3.  **Infection Mechanism:**
    If the Euclidean distance $d(a_i, a_j) < r$ (contact radius) and $a_j$ is infected:
    $$P(\text{infection}) = \alpha$$
    This introduces **stochasticity**: contact does not guarantee infection, simulating biological variability.
4.  **Recovery:** Individual internal timer. After $k$ time steps, $I \to R$.

---

## 📊 Comparative Analysis and Emergence

This project allows for the visualization of critical phenomena that distinguish both paradigms:

| Feature | Equation-Based (EBM) | Agent-Based (ABM) |
| :--- | :--- | :--- |
| **Approach** | Top-Down (Macroscopic) | Bottom-Up (Microscopic) |
| **Population** | Homogeneous (Perfect mixing) | Heterogeneous (Spatially distributed) |
| **Outcome** | Deterministic (Always the same) | Stochastic (Varies each run) |
| **Phenomena** | Ideal averages | **Emergence**, Local clusters, Noise |

**Key Conclusion:**
We observe that when $N \to \infty$ and agent density is high, the ABM curve **converges** toward the theoretical EBM solution. However, in early stages or low densities, ABM captures "spatial effects" (such as isolated outbreaks) that differential equations ignore.

---

## 📂 Project Structure

```text
SIR-Epidemic-Simulation/
├── assets/                 # Images and GIFs for this README
│   └── simulation.gif
├── src/                    # Source Code
│   ├── main.py             # Main execution script
│   ├── modelo_ebm.py       # Numerical solver (Euler)
│   ├── modelo_abm.py       # Agent Class definition
│   └── visualizacion.py    # Rendering engine (Matplotlib Animation)
├── .gitignore
├── requirements.txt        # Dependencies (numpy, matplotlib)
└── README.md               # Technical documentation
