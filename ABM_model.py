import numpy as np

class Agente:
    def __init__(self, id, x_max, y_max, prob_contagio, pasos_recuperacion):
        self.id = id
        # Posición aleatoria
        self.x = np.random.rand() * x_max
        self.y = np.random.rand() * y_max
        # Velocidad aleatoria (dirección)
        self.vel_x = (np.random.rand() - 0.5) * 2
        self.vel_y = (np.random.rand() - 0.5) * 2
        
        self.estado = 0  # 0: Sano, 1: Infectado, 2: Recuperado
        self.tiempo_infectado = 0
        self.prob_contagio = prob_contagio
        self.pasos_recuperacion = pasos_recuperacion

    def mover(self, x_max, y_max):
        # Movimiento simple
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Rebotar en las paredes
        if self.x <= 0 or self.x >= x_max: self.vel_x *= -1
        if self.y <= 0 or self.y >= y_max: self.vel_y *= -1

    def intentar_contagiar(self, otros_agentes, radio_contagio):
        if self.estado == 1:  # Solo si yo estoy infectado puedo contagiar
            for otro in otros_agentes:
                if otro.estado == 0:  # Solo contagio a los sanos
                    distancia = np.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
                    if distancia < radio_contagio:
                        if np.random.rand() < self.prob_contagio:
                            otro.estado = 1

    def actualizar_salud(self):
        if self.estado == 1:
            self.tiempo_infectado += 1
            if self.tiempo_infectado >= self.pasos_recuperacion:
                self.estado = 2  # Recuperado e inmune