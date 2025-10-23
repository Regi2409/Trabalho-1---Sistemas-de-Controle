import numpy as np
import matplotlib.pyplot as plt
import control as ct

s = ct.tf('s')

Gs = -8 / (s**2 + 1.5*s - 1)

Kp = 10

Cs = -Kp*(1 + s + 1/s)
Ls = Cs * Gs
Ts = ct.feedback(Ls, 1)
t, y = ct.step_response(Ts)

plt.figure()
ct.rlocus(Ls, kvect=np.linspace(0, 100, 1000))
plt.axvline(x=-10, color='r', linestyle='--', label='Limite Re = -10')
plt.title("Root Locus com PID")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.grid(True)
plt.legend()
plt.show()

plt.figure()
plt.plot(t, y, 'b', label=f"Kp={Kp}")
plt.title("Resposta ao Degrau com PID Sintonia")
plt.xlabel("Tempo [s]")
plt.ylabel("Saída")
plt.grid(True)
plt.legend()
plt.show()