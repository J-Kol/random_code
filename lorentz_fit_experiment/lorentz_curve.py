import numpy as np
import matplotlib.pyplot as plt

p = 0.9
t = 0.7
A = 1.0 / 2.0

n_pnt = 100
x_start = 0
x_end = 3.0

X = np.linspace(x_start, x_end, n_pnt)
Y = A/((X**2-p**2)**2+t**2*p**2)

with open("lorentz_curve.txt", "w") as f:
    for x, y in zip(X, Y):
        f.write(f"{x}, {y}\n")
    #print(X, Y, file=f)

plt.plot(X, Y, "+", linewidth = 4, color=(0, 0, 0),label="Data Sampling")

plt.grid()
plt.xlabel("frequence f/f0")
plt.ylabel("amplitude")
plt.title("Lorenz fit",fontsize = 18);
plt.legend()
plt.show()
