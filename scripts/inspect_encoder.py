import h5py
import numpy as np
import matplotlib.pyplot as plt

def print_hdf5_structure(name, obj):
    if isinstance(obj, h5py.Dataset) and name != 'ptychogram':
        print(f"Dataset: {name}")
        print(f"    Shape: {obj.shape}")
        print(f"    Type: {obj.dtype}")
        if obj.size < 10:  # Print full data for small datasets
            print(f"    Data: {obj[()]}")
        else:  # Print first few elements for larger datasets
            print(f"    First few elements: {obj[0:5]}")
        print(f"    Attributes:")
        for key, val in obj.attrs.items():
            print(f"        {key}: {val}")
        print()
    elif isinstance(obj, h5py.Group):
        print(f"Group: {name}")
        print(f"    Attributes:")
        for key, val in obj.attrs.items():
            print(f"        {key}: {val}")
        print()

def print_file_info(file_path):
    with h5py.File(file_path, 'r') as f:
        print("File structure:")
        f.visititems(print_hdf5_structure)
        
        if 'encoder' in f:
            encoder = f['encoder'][()]
            print("Encoder details:")
            print("    Shape:", encoder.shape)
            print("    Dtype:", encoder.dtype)
            print("    First few values:", encoder[:5])
            
            if encoder.ndim == 2 and encoder.shape[1] == 2:
                print("    Represents [x, y] positions for each image")
                print("    Number of positions:", encoder.shape[0])
                print("    Range of x positions:", np.min(encoder[:, 0]), "to", np.max(encoder[:, 0]))
                print("    Range of y positions:", np.min(encoder[:, 1]), "to", np.max(encoder[:, 1]))
            
            return encoder
        else:
            print("No 'encoder' dataset found in the file.")
            return None

#file_path = "/Users/User/Documents/Ptychography/PtyLab.py/datasets/LungCarcinomaFPM.hdf5"
#file_path = "/Users/User/Documents/Ptychography/PtyLab.py/datasets/USAFTargetFPM.hdf5"
file_path = "/Users/User/Documents/Ptychography/PtyLab.py/FPM_generator-master/FPM_generator-master/datasets/2024_11_22/my_FPM_dataset.h5"

encoder = print_file_info(file_path)

if encoder is not None:
    x = encoder[:, 0]
    y = encoder[:, 1]

    x_diff = np.diff(x)
    y_diff = np.diff(y)
    print("\nDifference in x positions:", x_diff)
    print("Difference in y positions:", y_diff)

    # Calculate the range of your plot
    x_range = np.max(x) - np.min(x)
    y_range = np.max(y) - np.min(y)

    # Determine the plot size to correspond to 0.005 units
    plot_size = 3.45e-6

    # Calculate the appropriate marker size (s)
    size = (plot_size / np.mean([x_range, y_range])) ** 2 * 100000000000
    print("\nMarker size:", size)

    plt.figure(figsize=(10, 10))
    scatter = plt.scatter(x, y, c=range(len(x)), cmap='viridis', s=size)
    plt.colorbar(scatter, label='LED Index')
    plt.title('LED Positions (Encoder Values)')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# import numpy as np

# # Parameters from the MATLAB code
# lambda_ = 0.6292
# NA = 0.1
# mag = 8.1485
# dpix_c = 6.5
# ds_led = 4e3  # 4mm
# z_led = 67.5e3
# dia_led = 19

# # Set up LED coordinates
# lit_cenv = 13
# lit_cenh = 14
# vled = np.arange(32) - lit_cenv
# hled = np.arange(32) - lit_cenh
# hhled, vvled = np.meshgrid(hled, vled)
# rrled = np.sqrt(hhled**2 + vvled**2)
# LitCoord = rrled < dia_led/2

# # Create encoder
# encoder = []
# for v, h in zip(vvled[LitCoord], hhled[LitCoord]):
#     encoder.append([v, h])

# encoder = np.array(encoder)

# print("Encoder shape:", encoder.shape)
# print("First few encoder values:")
# print(encoder)