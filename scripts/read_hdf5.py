import h5py

# Open the HDF5 file
file_path = 'C:\\Users\\Dell\\Documents\\GitHub\\PtyLab.py\\example_data\\LungCarcinomaFPM.hdf5'  # Replace with your file path
with h5py.File(file_path, 'r') as hdf5_file:
    # Access a specific group or dataset
    # For example, to access a dataset or group named 'my_dataset'
    dataset_or_group = hdf5_file['ptychogram']

    print(f'Name: {dataset_or_group.name}')
    print(f'Data: {dataset_or_group[0]}')
    
    data = dataset_or_group[0]

    # # Read the attribute
    # attribute_name = 'Type'  # Replace with the attribute name you want to read
    # attribute_value = dataset_or_group.attrs[attribute_name]

    # print(f'Attribute value: {attribute_value}')

import numpy as np
import matplotlib.pyplot as plt

# Apply the 2D Fourier Transform
fft_matrix = np.fft.fft2(data)

# Shift zero frequency component to the center
fft_matrix_shifted = np.fft.fftshift(fft_matrix)

# Compute the amplitude (magnitude) and phase
amplitude = np.abs(fft_matrix_shifted)
phase = np.angle(fft_matrix_shifted)

plt.figure(figsize=(12, 6))

# Plot amplitude
plt.subplot(1, 2, 1)
plt.imshow(np.log(1 + amplitude), cmap='gray', interpolation='nearest')
plt.colorbar()
plt.title('Amplitude')

# Plot phase
plt.subplot(1, 2, 2)
plt.imshow(phase, cmap='hsv', interpolation='nearest')
plt.colorbar()
plt.title('Phase')

plt.show()

