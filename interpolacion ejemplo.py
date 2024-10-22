import numpy as np

# Datos de ejemplo (x, y, temperatura)
data = np.array([
    [1, 1, 2],
    [2, 2, 3],
    [3, 3, 5],
    [4, 4, 4]
])

# Función para calcular diferencias divididas de Newton
def newton_dif_div(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    return coef[0, :]

# Generar puntos interpolados (ejemplo)
x = data[:, 0]
y = data[:, 2]
coef = newton_dif_div(x, y)

# Interpolación
def newton_interpolation(x_data, coef, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Ejemplo de interpolación en nuevos puntos
new_points = np.linspace(1, 4, 100)
interpolated_temps = [newton_interpolation(x, coef, xi) for xi in new_points]

# Mostrar resultados
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(data[:, 0], data[:, 2], color='red', label='Datos Originales')
plt.plot(new_points, interpolated_temps, label='Interpolación de Newton')
plt.legend()
plt.xlabel('X')
plt.ylabel('Temperatura')
plt.title('Interpolación de Newton')
plt.show()
