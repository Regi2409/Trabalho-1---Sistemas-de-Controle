import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import control as clt
from control import tf, feedback
import os

# --- 1. Controlador Fixo (Baseado no Projeto de 1ª Ordem) ---
# Parâmetros nominais que definiram o controlador
K_nominal = 0.20
tau_nominal = 20.0
theta_nominal = 5.0
ts_desejado = 60.0
tau_d = ts_desejado / 4.6

# Controlador PI calculado com a regra IMC para o alvo de 1ª ordem
# Este controlador será mantido FIXO
Kc = tau_nominal / (K_nominal * (tau_d + theta_nominal))
Ti = tau_nominal
C = Kc * (1 + tf([1], [Ti, 0]))
print("--- Controlador PI Fixo (Baseado no Projeto de 1ª Ordem) ---")
print(C)


# --- 2. Definir o Espaço de Parâmetros (Hipercubo) ---
# Amostrando os parâmetros com mais pontos para gerar uma visualização suave
num_pontos = 25
K_vals = np.linspace(0.15, 0.25, num_pontos)
theta_vals = np.linspace(3.0, 5.0, num_pontos)


# --- 3. Calcular os Polos para cada Ponto do Hipercubo ---
# Listas para armazenar as coordenadas dos polos
all_reals = []
all_imags = []
all_thetas_for_plot = []
all_ks_for_plot = []

print("\nCalculando polos para o controlador de 1ª ordem... Isso pode levar um momento.")
for k_param in K_vals:
    for theta_param in theta_vals:
        # Cria a planta "incerta"
        num_pade, den_pade = clt.pade(theta_param, 4) 
        G_incerta = clt.series(tf([k_param], [tau_nominal, 1]), tf(num_pade, den_pade))

        # Malha fechada com o controlador fixo C
        Gmf_incerta = feedback(C * G_incerta, 1)

        # Calcula os polos
        poles = clt.poles(Gmf_incerta)
        
        # Filtra e armazena apenas os polos dominantes (os mais próximos da origem)
        dominant_poles = sorted(poles, key=lambda p: abs(p.real), reverse=False)[:2]

        for p in dominant_poles:
            all_reals.append(p.real)
            all_imags.append(p.imag)
            all_thetas_for_plot.append(theta_param)
            all_ks_for_plot.append(k_param)

print("Cálculo finalizado. Gerando gráfico 3D.")


# --- 4. Plotagem 3D ---
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Gráfico de dispersão 3D dos polos
sc = ax.scatter(all_reals, all_imags, all_thetas_for_plot, c=all_ks_for_plot, cmap='coolwarm', s=15)

# Adiciona o plano de estabilidade (em Real = 0)
y_plane, z_plane = np.meshgrid(np.linspace(min(all_imags), max(all_imags), 2), np.linspace(min(all_thetas_for_plot), max(all_thetas_for_plot), 2))
x_plane = np.zeros_like(y_plane)
ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.2, color='r', label='Fronteira de Instabilidade')

ax.set_xlabel('Eixo Real (Estabilidade)')
ax.set_ylabel('Eixo Imaginário (Oscilação)')
ax.set_zlabel('Atraso de Tempo, θ (s)')
ax.set_title('Movimento 3D dos Polos (Controlador de 1ª Ordem)')
ax.view_init(elev=20, azim=-60) 

# Barra de cores para a variável K
cbar = plt.colorbar(sc)
cbar.set_label('Ganho, K')
plt.savefig(os.path.join("imagens", "hipercubo_controlador.png" ))
plt.show()