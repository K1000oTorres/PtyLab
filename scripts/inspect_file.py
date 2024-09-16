import h5py

def print_hdf5_structure(name, obj):
    print(name)
    for key, val in obj.attrs.items():
        print(f"    Attribute: {key}: {val}")
    if isinstance(obj, h5py.Dataset):
        print(f"    Shape: {obj.shape}")
        print(f"    Type: {obj.dtype}")

file_path = "C:\\Users\\Dell\\Documents\\GitHub\\PtyLab.py\\example_data\\stained_histology_1LED.hdf5"
file_path = "C:\\Users\\Dell\\Documents\\GitHub\\PtyLab.py\\example_data\\USAFTargetFPM.hdf5"
file_path = "C:\\Users\\Dell\\Documents\\GitHub\\PtyLab.py\\example_data\\simu.hdf5"
with h5py.File(file_path, 'r') as f:
    f.visititems(print_hdf5_structure)