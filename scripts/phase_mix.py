import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the images
dog = cv2.imread("C:\\Users\\Dell\\Downloads\\dog-112-298x300.png")
car = cv2.imread("C:\\Users\\Dell\\Downloads\\Car.png")

# Check if images are loaded
if dog is None or car is None:
    raise ValueError("One or both image files could not be loaded. Check the file paths.")

# Resize the images to the same size
car = cv2.resize(car, (dog.shape[1], dog.shape[0]))

# Split the images into R, G, B channels
dog_channels = cv2.split(dog)
car_channels = cv2.split(car)

# Prepare arrays to hold transformed data
dog_amplitude_channels = []
dog_phase_channels = []
car_amplitude_channels = []
car_phase_channels = []

# Process each channel
for i in range(3):
    # Fourier Transform for each channel
    dog_fft = np.fft.fft2(dog_channels[i])
    car_fft = np.fft.fft2(car_channels[i])

    # Split into amplitude and phase
    dog_amplitude = np.abs(dog_fft)
    dog_phase = np.angle(dog_fft)
    car_amplitude = np.abs(car_fft)
    car_phase = np.angle(car_fft)

    # Store the results
    dog_amplitude_channels.append(dog_amplitude)
    dog_phase_channels.append(dog_phase)
    car_amplitude_channels.append(car_amplitude)
    car_phase_channels.append(car_phase)

# Merge amplitude of the dog with phase of the car and vice versa for each channel
dog_car_channels = []
car_dog_channels = []

for i in range(3):
    # Merge for each channel
    dog_car_fft = dog_amplitude_channels[i] * np.exp(1j * car_phase_channels[i])
    car_dog_fft = car_amplitude_channels[i] * np.exp(1j * dog_phase_channels[i])

    # Inverse Fourier Transform
    dog_car = np.real(np.fft.ifft2(dog_car_fft))
    car_dog = np.real(np.fft.ifft2(car_dog_fft))

    # Normalize the images for display
    def normalize_image(image):
        image_min = np.min(image)
        image_max = np.max(image)
        if image_max > image_min:
            return (image - image_min) / (image_max - image_min)
        else:
            return np.zeros_like(image)
    
    dog_car_channels.append(normalize_image(dog_car))
    car_dog_channels.append(normalize_image(car_dog))

# Merge the channels back into RGB images
dog_car_rgb = cv2.merge(dog_car_channels)
car_dog_rgb = cv2.merge(car_dog_channels)

# Convert RGB images from [0,1] to [0,255]
dog_car_rgb = (dog_car_rgb * 255).astype(np.uint8)
car_dog_rgb = (car_dog_rgb * 255).astype(np.uint8)

# Display the images
plt.figure(figsize=(12, 12))

# Original images
plt.subplot(3, 4, 1)
plt.imshow(cv2.cvtColor(dog, cv2.COLOR_BGR2RGB))
plt.title('Dog (Original)')
plt.axis('off')

plt.subplot(3, 4, 2)
plt.imshow(cv2.cvtColor(car, cv2.COLOR_BGR2RGB))
plt.title('Car (Original)')
plt.axis('off')

# Amplitude and Phase of Car
plt.subplot(3, 4, 3)
plt.imshow(np.log(1 + car_amplitude_channels[0]), cmap='gray')
plt.title('Car Amplitude (R Channel)')
plt.axis('off')

plt.subplot(3, 4, 4)
plt.imshow(car_phase_channels[0], cmap='hsv')
plt.title('Car Phase (R Channel)')
plt.axis('off')

# Display results of merging
plt.subplot(3, 4, 7)
plt.imshow(cv2.cvtColor(dog_car_rgb, cv2.COLOR_BGR2RGB))
plt.title('Dog with Car Phase')
plt.axis('off')

plt.subplot(3, 4, 8)
plt.imshow(cv2.cvtColor(car_dog_rgb, cv2.COLOR_BGR2RGB))
plt.title('Car with Dog Phase')
plt.axis('off')

plt.show()
