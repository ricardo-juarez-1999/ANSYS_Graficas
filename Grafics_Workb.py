## Código: Gráfica Reynolds vs Nusselt estilo paper

import matplotlib.pyplot as plt
import numpy as np

print("Esta es la primera prueba de local a remoto")

## Datos (Parametro y valores pueden ser modificados)
# Valores de Reynolds
Re = np.array([
    5827,
    6992,
    8158,
    9323,
    10489,
    11654,
    12820,
    13895,
    15151
])

## Valores de Nusselt (Parametro y valores pueden ser modificados)
Nu = np.array([
    0.046487944,
    0.044179787,
    0.042194477,
    0.0404549,
    0.038900965,
    0.037564789,
    0.036400473,
    0.03535078,
    0.034412954
])

## Configuración de la Grafica

plt.figure(figsize=(8,6))

# Línea principal
plt.plot(
    Re,
    Nu,
    marker='o',
    linestyle='-',
    linewidth=2,
    markersize=7,
    label='Datos de Simulación'
)

# Etiquetas
plt.xlabel('Reynolds', fontsize=14)
plt.ylabel('Factor f', fontsize=14)

# Título
plt.title('Relación entre Reynolds y Factor de fricción', fontsize=16)

# Cuadrícula tipo paper
plt.grid(True, linestyle='--', alpha=0.6)

# Leyenda
plt.legend(fontsize=12)

# Ajuste de márgenes
plt.tight_layout()

# Descomenta la siguiente línea si quieres guardar la imagen automáticamente:
#plt.savefig('Re_vs_Nu.png', dpi=300)

# Mostrar gráfica
plt.show()