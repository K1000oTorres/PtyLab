import h5py
import os

# Path to your .mat file
h5_file = "C:\\Users\\Dell\\Documents\\GitHub\\PtyLab.py\\example_data\\USAFTargetFPM.hdf5"

# New path for the .h5 file (change the extension)
mat_file = os.path.splitext(h5_file)[0] + '.mat'

# Open the .mat file
with h5py.File(h5_file, 'r') as h5:
    # Create a new .h5 file
    with h5py.File(mat_file, 'w') as mat:
        # Copy all data from .mat to .h5
        for key in mat.keys():
            if key == 'PG':
                h5.copy(key, mat, name='ptychogram')
            else:
                h5.copy(key, mat)

print(f"Conversion complete. New file saved as: {h5_file}")