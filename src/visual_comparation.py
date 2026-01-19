import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ABM_model import Agente
from EBM_model import resolver_sir_ebm


# 1. Configuración
N_AGENTES = 200
PASOS = 200
K_RUNS = 30              
X_MAX, Y_MAX = 100, 100
RADIO_CONTAGIO = 5
PROB_CONTAGIO = 0.3
PASOS_RECUPERACION = 50
BETA, GAMMA = 0.5, 0.1


# 2. Modelo EBM (teórico)
t_ebm, S_ebm, I_ebm, R_ebm = resolver_sir_ebm(
    0.99, 0.01, 0, BETA, GAMMA, PASOS, 1
)

# 3. Ejecutar K simulaciones ABM

I_runs = np.zeros((K_RUNS, PASOS))

for k in range(K_RUNS):
    agentes = [
        Agente(i, X_MAX, Y_MAX, PROB_CONTAGIO, PASOS_RECUPERACION)
        for i in range(N_AGENTES)
    ]
    agentes[0].estado = 1  # paciente cero

    for t in range(PASOS):
        infectados = 0

        for a in agentes:
            a.mover(X_MAX, Y_MAX)
            a.intentar_contagiar(agentes, RADIO_CONTAGIO)
            a.actualizar_salud()
            if a.estado == 1:
                infectados += 1

        I_runs[k, t] = infectados / N_AGENTES

# 4. Estadística ABM

I_mean = np.mean(I_runs, axis=0)
I_std  = np.std(I_runs, axis=0)


# 5. Visualización
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Inicializamos una simulación ABM SOLO para visualizar agentes
agentes_vis = [
    Agente(i, X_MAX, Y_MAX, PROB_CONTAGIO, PASOS_RECUPERACION)
    for i in range(N_AGENTES)
]
agentes_vis[0].estado = 1

def update(frame):
    ax1.clear()
    ax2.clear()

    # ---------- ABM visual ----------
    sanos_x, sanos_y = [], []
    infect_x, infect_y = [], []
    recup_x, recup_y = [], []

    for a in agentes_vis:
        a.mover(X_MAX, Y_MAX)
        a.intentar_contagiar(agentes_vis, RADIO_CONTAGIO)
        a.actualizar_salud()

        if a.estado == 0:
            sanos_x.append(a.x); sanos_y.append(a.y)
        elif a.estado == 1:
            infect_x.append(a.x); infect_y.append(a.y)
        else:
            recup_x.append(a.x); recup_y.append(a.y)

    ax1.scatter(sanos_x, sanos_y, c='blue', s=10, label='Sanos')
    ax1.scatter(infect_x, infect_y, c='red', s=10, label='Infectados')
    ax1.scatter(recup_x, recup_y, c='green', s=10, label='Recuperados')

    ax1.set_xlim(0, X_MAX)
    ax1.set_ylim(0, Y_MAX)
    ax1.set_title(f"Simulación ABM (Paso {frame})")
    ax1.legend(loc='upper right')

    #Comparación estadística
    ax2.plot(t_ebm, I_ebm, 'r--', label='EBM (Infectados)')
    ax2.plot(I_mean[:frame], 'r-', label='ABM media')
    ax2.fill_between(
        range(frame),
        (I_mean - I_std)[:frame],
        (I_mean + I_std)[:frame],
        color='red',
        alpha=0.2,
        label='ABM ± σ'
    )

    ax2.set_title("ABM vs EBM (Media + Desviación)")
    ax2.set_xlabel("Tiempo")
    ax2.set_ylabel("Fracción población")
    ax2.legend()


# 6. Ejecutar animación
ani = animation.FuncAnimation(
    fig, update, frames=PASOS, interval=50, repeat=False
)

plt.show()
