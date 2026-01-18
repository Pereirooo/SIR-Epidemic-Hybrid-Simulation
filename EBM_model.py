import numpy as np
import matplotlib.pyplot as plt

def resolver_sir_ebm(S0, I0, R0, beta, gamma, dias, dt):
    """
    Resuelve el modelo SIR usando el Método Numérico de Euler.
    """
    # Pasos de tiempo (N iteraciones)
    n_steps = int(dias / dt)
    t = np.linspace(0, dias, n_steps)
    
    # Arrays para guardar los datos
    S = np.zeros(n_steps)
    I = np.zeros(n_steps)
    R = np.zeros(n_steps)
    
    # Condiciones iniciales
    S[0], I[0], R[0] = S0, I0, R0
    
    # Bucle principal: Método de Euler
    # Nuevo_Valor = Valor_Actual + (Derivada * paso_tiempo)
    for i in range(1, n_steps):
        dS_dt = -beta * S[i-1] * I[i-1]
        dI_dt = (beta * S[i-1] * I[i-1]) - (gamma * I[i-1])
        dR_dt = gamma * I[i-1]
        
        S[i] = S[i-1] + dS_dt * dt
        I[i] = I[i-1] + dI_dt * dt
        R[i] = R[i-1] + dR_dt * dt
        
    return t, S, I, R

# --- Prueba rápida ---
if __name__ == "__main__":
    # Población total = 1.0 (100%)
    t, S, I, R = resolver_sir_ebm(S0=0.99, I0=0.01, R0=0.0, beta=0.5, gamma=0.1, dias=100, dt=0.1)
    
    # Visualización simple para comprobar
    plt.plot(t, S, label='Susceptibles')
    plt.plot(t, I, label='Infectados')
    plt.plot(t, R, label='Recuperados')
    plt.legend()
    plt.title("Modelo SIR - Solución Ecuación Diferencial (EBM)")
    plt.show()