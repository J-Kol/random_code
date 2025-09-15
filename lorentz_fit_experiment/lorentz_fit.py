import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
import numpy as np

df = pd.read_csv('data.txt', sep=',', header=None)  # Change sep to '\s+' for whitespace-separated values

X = df[0]
Y = df[1]

def func(x, p, t):
    return 1/((x**2-p**2)**2+t**2*p**2)

estimates = [0.8, 0.3]

bounds = ([0.01, 0.01], [np.inf, np.inf])

popt, _ = curve_fit(func, X, Y, p0 = estimates, maxfev=3000, bounds=bounds)
# summarize the parameter values
p, t = popt
print(f"P = {p}, T = {t}")
#func(popt)
plt.plot(X, Y, "+", linewidth = 4, color=(0, 0, 0),label="Your Data")
#plt.ylim(-10,10)

X_test = np.linspace(min(X), max(X), 500)
plt.plot(X_test, func(X_test, *popt), "-", linewidth = 4, color=(1, 0, 0),label="Fit Function")
#plt.ylim(-10,10)
plt.grid()
plt.xlabel("freq/f")
plt.ylabel("amplitude")
plt.title("Fitted Graph",fontsize = 18);

plt.legend()
plt.show()