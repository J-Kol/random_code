import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

p = 0.9993775545226538
t = 0.2722592910959406
A = 1 / 1831.5

n_put = 50
x_start = 0
x_end = 1.8

X = np.linspace(x_start, x_end, n_put)
Y = A/((X**2-p**2)**2+t**2*p**2)

with open("data.txt", "w") as f:
    for x, y in zip(X, Y):
        f.write(f"{x}, {y}\n")
    #print(X, Y, file=f)

plt.plot(X, Y, "+", linewidth = 4, color=(0, 0, 0),label="Your Data")

plt.grid()
plt.xlabel("freq/f")
plt.ylabel("amplitude")
plt.title("Fitted Graph",fontsize = 18);
plt.legend()
plt.show()