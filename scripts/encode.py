import numpy as np
import matplotlib.pyplot as plt

# Given parameters
ds_led = 4e-3  # spacing between neighboring LEDs in micrometers
z_led = 74e-3  # distance from the LED to the object in micrometers
dia_led = 10  # diameter of # of LEDs used in the experiment
lit_cenv = 20  # LED array center vertical index
lit_cenh = 20  # LED array center horizontal index

# Generate the LED grid
vled = np.arange(0, 32) - lit_cenv

hled = np.arange(0, 32) - lit_cenh

hhled, vvled = np.meshgrid(hled, vled)

# Calculate the radius and apply the LED selection mask
rrled = np.sqrt(hhled**2 + vvled**2)
LitCoord = rrled < dia_led / 2
# Get the indices of LEDs used in the experiment
Litidx = np.where(LitCoord)
true_indices = np.where(LitCoord)
false_indices = np.where(LitCoord == False)
#print("true: ",true_indices)
#print("false: ",false_indices)

# Convert indices to positions (in micrometers)
led_positions = np.column_stack((hhled[Litidx] * ds_led, vvled[Litidx] * ds_led))
print(led_positions.shape)
no_led_positions = np.column_stack((hhled[false_indices] * ds_led, vvled[false_indices] * ds_led))
#led_positions.shape, led_positions[:5]  # Show the shape and first few positions

plt.figure(figsize=(8, 8))
# LEDs seleccionados
plt.scatter(led_positions[:, 0], led_positions[:, 1], c='blue', marker='o', label='LEDs seleccionados')

# LEDs no seleccionados
plt.scatter(no_led_positions[:, 0], no_led_positions[:, 1], c='red', marker='x', label='Sin LEDs')

# Líneas de referencia
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Configuración del gráfico
plt.title('Distribución de LEDs seleccionados y no seleccionados')
plt.xlabel('Posición horizontal (micrómetros)')
plt.ylabel('Posición vertical (micrómetros)')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.axis('equal')
plt.show()
#print(led_positions)
