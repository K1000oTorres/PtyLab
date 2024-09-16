import h5py
import os

# Path to your .mat file
mat_file = "C:\\Users\\Dell\\Documents\\GitHub\\PtyLab.py\\example_data\\.mat"

# New path for the .h5 file (change the extension)
h5_file = os.path.splitext(mat_file)[0] + '.h5'

# Open the .mat file
with h5py.File(mat_file, 'r') as mat:
    # Create a new .h5 file
    with h5py.File(h5_file, 'w') as h5:
        # Copy all data from .mat to .h5
        for key in mat.keys():
            if key == 'PG':
                mat.copy(key, h5, name='ptychogram')
            else:
                mat.copy(key, h5)

print(f"Conversion complete. New file saved as: {h5_file}")