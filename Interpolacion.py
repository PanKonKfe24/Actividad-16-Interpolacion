# -*- coding: utf-8 -*-

#           Autor:
#   Buitrago Rios Juan Pablo
#   argelpech098@gmail.com  
#   Version 1.01 : 11/03/2025
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pandas as pd

# Datos del ejercicio
longitud = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
deflexion = np.array([0.0, -1.5, -2.8, -3.0, -2.7, -2.0])

# Interpolaciones
interp_lineal = interp1d(longitud, deflexion, kind='linear')
interp_cuadratica = interp1d(longitud, deflexion, kind='quadratic')
interp_cubica = interp1d(longitud, deflexion, kind='cubic')

# Puntos intermedios para comparar
puntos_intermedios = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
y_lineal = interp_lineal(puntos_intermedios)
y_cuadratica = interp_cuadratica(puntos_intermedios)
y_cubica = interp_cubica(puntos_intermedios)

# Crear DataFrame para Excel
df = pd.DataFrame({
    'Longitud (m)': puntos_intermedios,
    'Lineal (mm)': y_lineal,
    'Cuadrática (mm)': y_cuadratica,
    'Cúbica (mm)': y_cubica
})

# Guardar en archivo Excel
df.to_excel('comparacion_interpolacion_viga.xlsx', index=False)

# Graficar
x_vals = np.linspace(0, 5, 200)
plt.figure(figsize=(10, 6))
plt.scatter(longitud, deflexion, color='red', label='Datos Originales')
plt.plot(x_vals, interp_lineal(x_vals), '--', label='Lineal', color='blue')
plt.plot(x_vals, interp_cuadratica(x_vals), '-.', label='Cuadrática', color='green')
plt.plot(x_vals, interp_cubica(x_vals), label='Cúbica', color='purple')
plt.xlabel('Longitud (m)')
plt.ylabel('Deflexión (mm)')
plt.title('Interpolación de Deflexión en una Viga')
plt.legend()
plt.grid(True)
plt.savefig('grafico_interpolacion_viga.png')
plt.show()
