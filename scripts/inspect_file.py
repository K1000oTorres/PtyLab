import h5py

def print_hdf5_structure(name, obj):
    print(name)
    for key, val in obj.attrs.items():
        print(f"    Attribute: {key}: {val}")
    if isinstance(obj, h5py.Dataset):
        print(f"    Shape: {obj.shape}")
        print(f"    Type: {obj.dtype}")

#file_path = "/Users/User/Documents/Ptychography/PtyLab.py/datasets/simu.hdf5"
#file_path = "/Users/User/Documents/Ptychography/PtyLab.py/datasets/LungCarcinomaFPM.hdf5"
file_path = "/Users/User/Desktop/FPM_INR-main/FPM_INR-main/data/sheepblood/sheepblood_r_2.hdf5"
#file_path = "/Users/User/Documents/Ptychography/PtyLab.py/datasets/USAFTargetFPM.hdf5"
with h5py.File(file_path, 'r') as f:
    # Imprimir estructura
    print("Estructura del archivo:")
    f.visititems(print_hdf5_structure)

    # Acceder a los valores directamente
    print("\nValores de los datos seleccionados:")
    datasets_to_read = ['NA', 'dxd', 'magnification', 'wavelength', 'zled', 'encoder']
    for dataset_name in datasets_to_read:
        if dataset_name in f:
            value = f[dataset_name][()]  # El [()] extrae el valor real del dataset
            print(f"{dataset_name}: {value}")
        else:
            print(f"{dataset_name} no encontrado en el archivo.")