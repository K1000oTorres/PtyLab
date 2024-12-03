import mat73
import h5py
import numpy as np

def leer_pticograma(ruta_archivo):
    try:
        # Cargar el archivo .mat
        data_struct = mat73.loadmat(ruta_archivo)

        # Extraer variables específicas
        ptychograma = data_struct.get("I_low", "No disponible")
        ptychograma = np.transpose(ptychograma, (2, 0, 1))  
        wavelength = 6.32e-07  # Luz roja, expresada en metros
        encoder = data_struct.get("na_design", "No disponible")  
        dxd = data_struct.get("dpix_c", "No disponible")
        dxd = dxd/1e6 if dxd != "No disponible" else "No disponible"
        zled = data_struct.get("h", "No disponible") 
        zled = zled/1e6 if dxd != "No disponible" else "No disponible"
        magnification = data_struct.get("mag", "No disponible")
        na = data_struct.get("NA", "No disponible")

        # Devolver los datos en un diccionario
        return {
            "ptychogram": ptychograma,
            "wavelength": wavelength,
            "encoder": encoder,
            "dxd": dxd,
            "zled": zled,
            "magnification": magnification,
            "NA": na
        }

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def convertir_a_hdf5(datos, ruta_hdf5):
 
     try:
        with h5py.File(ruta_hdf5, "w") as hdf5_file:
            for key, value in datos.items():
                if isinstance(value, str) and value == "No disponible":
                    continue  # Ignorar valores no disponibles

                # Convertir listas o tuplas a arrays de numpy si es necesario
                if isinstance(value, (list, tuple)):
                    value = np.array(value)

                # Crear el dataset
                dataset = hdf5_file.create_dataset(
                    key,
                    data=value,
                    dtype="float64"  # Convertir todo a float64
                )
                
                # Añadir atributos al dataset
                dataset.attrs["CLASS"] = b'ARRAY'
                dataset.attrs["FLAVOR"] = b'numpy'
                dataset.attrs["TITLE"] = b'Empty(dtype=dtype(\'S1\'))'  # Atributo vacío
                dataset.attrs["VERSION"] = b'2.4'
            
        print(f"Archivo HDF5 guardado exitosamente en {ruta_hdf5}")
    
     except Exception as e:
         print(f"Error al crear el archivo HDF5: {e}")


ruta_archivo = "/Users/User/Desktop/FPM_INR-main/FPM_INR-main/data/sheepblood/sheepblood_r.mat"
datos_pticograma = leer_pticograma(ruta_archivo)

if datos_pticograma:
    ruta_hdf5 = "/Users/User/Desktop/FPM_INR-main/FPM_INR-main/data/sheepblood/sheepblood_r_2.hdf5"  # Ruta para guardar el archivo HDF5
    convertir_a_hdf5(datos_pticograma, ruta_hdf5)
