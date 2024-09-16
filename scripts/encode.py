import numpy as np

# Given parameters
ds_led = 4e-3  # spacing between neighboring LEDs in micrometers
z_led = 67.5e-3  # distance from the LED to the object in micrometers
dia_led = 19  # diameter of # of LEDs used in the experiment
lit_cenv = 13  # LED array center vertical index
lit_cenh = 14  # LED array center horizontal index

# Generate the LED grid
vled = np.arange(0, 32) - lit_cenv
hled = np.arange(0, 32) - lit_cenh
hhled, vvled = np.meshgrid(hled, vled)

# Calculate the radius and apply the LED selection mask
rrled = np.sqrt(hhled**2 + vvled**2)
LitCoord = rrled < dia_led / 2

# Get the indices of LEDs used in the experiment
Litidx = np.where(LitCoord)

# Convert indices to positions (in micrometers)
led_positions = np.column_stack((hhled[Litidx] * ds_led, vvled[Litidx] * ds_led))

led_positions.shape, led_positions[:5]  # Show the shape and first few positions

print("LED positions shape:", led_positions.shape)
print("First few LED positions:")
print(led_positions)
