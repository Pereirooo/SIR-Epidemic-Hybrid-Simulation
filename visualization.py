import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ABM_model import Agente

# Configuración inicial
N_AGENTES = 100
X_MAX, Y_MAX = 100, 100
RADIO_CONTAGIO = 5
PROB_CONTAGIO = 0.3
PASOS_RECUPERACION = 50

# Crear población
agentes = [Agente(i, X_MAX, Y_MAX, PROB_CONTAGIO, PASOS_RECUPERACION) for i in range(N_AGENTES)]
agentes[0].estado = 1  # El "Paciente Cero"

fig, ax = plt.subplots(figsize=(8,6))

def update(frame):
    ax.clear()
    ax.set_xlim(0, X_MAX)
    ax.set_ylim(0, Y_MAX)
    ax.set_title(f"Simulación ABM Epidemia - Paso {frame}")
    
    # Listas para dibujar por colores
    sanos_x, sanos_y = [], []
    infect_x, infect_y = [], []
    recup_x, recup_y = [], []

    for a in agentes:
        a.mover(X_MAX, Y_MAX)
        a.intentar_contagiar(agentes, RADIO_CONTAGIO)
        a.actualizar_salud()
        
        if a.estado == 0:
            sanos_x.append(a.x); sanos_y.append(a.y)
        elif a.estado == 1:
            infect_x.append(a.x); infect_y.append(a.y)
        else:
            recup_x.append(a.x); recup_y.append(a.y)

    ax.scatter(sanos_x, sanos_y, color='blue', label='Sanos', s=20)
    ax.scatter(infect_x, infect_y, color='red', label='Infectados', s=20)
    ax.scatter(recup_x, recup_y, color='green', label='Recuperados', s=20)
    ax.legend(loc='upper right')

ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
plt.show()