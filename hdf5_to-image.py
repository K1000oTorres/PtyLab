# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:08:23 2024

@author: User
"""
import h5py
import numpy as np
import matplotlib.pyplot as plt
import os

def save_image(data, output_filename):
    # Check if data contains complex values
    if np.iscomplexobj(data):
        # Save magnitude and phase separately
        magnitude = np.abs(data)
        phase = np.angle(data)
        
        # Normalize and save magnitude
        normalized_magnitude = 255 * (magnitude - np.min(magnitude)) / (np.max(magnitude) - np.min(magnitude))
        plt.imsave(output_filename.replace('.png', '_magnitude.png'), normalized_magnitude.astype(np.uint8))
        
        # Normalize and save phase
        normalized_phase = 255 * (phase - np.min(phase)) / (np.max(phase) - np.min(phase))
        plt.imsave(output_filename.replace('.png', '_phase.png'), normalized_phase.astype(np.uint8))
        print(f"Imagen de magnitud guardada como: {output_filename.replace('.png', '_magnitude.png')}")
        print(f"Imagen de fase guardada como: {output_filename.replace('.png', '_phase.png')}")
    else:
        # Continue with existing process for real data
        normalized_data = 255 * (data - np.min(data)) / (np.max(data) - np.min(data))
        plt.imsave(output_filename, normalized_data.astype(np.uint8))
        print(f"Imagen guardada como: {output_filename}")

def extract_images_from_hdf5(file_path):
    with h5py.File(file_path, 'r') as f:
        print(f"Archivos contenidos en {file_path}: {list(f.keys())}")

        output_dir = file_path.replace('.hdf5', '_images')
        os.makedirs(output_dir, exist_ok=True)

        for dataset_key in f.keys():
            data = np.array(f[dataset_key])
            print(f"Dataset: {dataset_key}, forma: {data.shape}")

            # Check if the dataset is a scalar
            if len(data.shape) == 0:  # Scalar value
                with open(os.path.join(output_dir, f"{dataset_key}.txt"), "w") as file:
                    file.write(str(data))
                print(f"Scalar value saved for dataset {dataset_key}")

            # Use squeeze to reduce unnecessary dimensions if needed
            elif len(data.shape) >= 2:
                data_squeezed = np.squeeze(data)
                if len(data_squeezed.shape) == 2:
                    output_filename = os.path.join(output_dir, f"{dataset_key}.png")
                    save_image(data_squeezed, output_filename)
                elif len(data_squeezed.shape) == 3:
                    for i in range(data_squeezed.shape[0]):
                        output_filename = os.path.join(output_dir, f"{dataset_key}_{i}.png")
                        save_image(data_squeezed[i], output_filename)
                else:
                    print(f"Formato de datos no reconocido para el dataset {dataset_key}: {data.shape}")

            # For 1D arrays
            elif len(data.shape) == 1:
                plt.figure()
                plt.plot(data)
                output_filename = os.path.join(output_dir, f"{dataset_key}.png")
                plt.savefig(output_filename)
                plt.close()
                print(f"Line plot saved for dataset {dataset_key}")


# Rutas de los archivos HDF5
filePath1 = "/Users/User/Documents/Ptychography/PtyLab.py/datasets/Brain_smoothBeam_poly_bin8.hdf5"
#filePath2 = "/Users/User/Documents/Ptychography/PtyLab.py/datasets/USAFTargetFPM.hdf5"
filePath2 = "/Users/User/Documents/Ptychography/PtyLab.py/FPM_generator-master/FPM_generator-master/datasets/2024_11_15/my_FPM_dataset.h5"

# Extraer imágenes de ambos archivos HDF5
extract_images_from_hdf5(filePath1)
extract_images_from_hdf5(filePath2)