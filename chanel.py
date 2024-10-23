import numpy as np
import imageio.v2 as imageio  # Menggunakan imageio v2 untuk menghindari peringatan
import matplotlib.pyplot as plt

def load_image(image_path):
    """Memuat gambar dari path yang diberikan."""
    img = imageio.imread(image_path)
    return img

def display_red_channel(image):
    """Menampilkan channel merah (Red) dari gambar."""
    R = image[:, :, 0]
    plt.imshow(R, cmap='Reds')
    plt.title('Channel R (Red)')
    plt.axis('off')
    plt.show()

def display_green_channel(image):
    """Menampilkan channel hijau (Green) dari gambar."""
    G = image[:, :, 1]
    plt.imshow(G, cmap='Greens')
    plt.title('Channel G (Green)')
    plt.axis('off')
    plt.show()

def display_blue_channel(image):
    """Menampilkan channel biru (Blue) dari gambar."""
    B = image[:, :, 2]
    plt.imshow(B, cmap='Blues')
    plt.title('Channel B (Blue)')
    plt.axis('off')
    plt.show()

def convert_to_grayscale(image):
    """Mengonversi gambar ke grayscale."""
    grayscale = np.dot(image[...,:3], [0.299, 0.587, 0.114])
    return grayscale

def convert_to_binary(grayscale_image, threshold=128):
    """Mengonversi gambar grayscale ke biner berdasarkan threshold."""
    binary_image = (grayscale_image > threshold) * 255
    return binary_image

def display_grayscale_and_binary(grayscale, binary):
    """Menampilkan gambar grayscale dan biner."""
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(grayscale, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(binary, cmap='gray')
    plt.title('Binary Image')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    # Ganti dengan path ke gambar Anda
    image_path = r"C:\\gambar\\garuda.jpg"
    
    # Memuat gambar
    image = load_image(image_path)

    # Menampilkan masing-masing channel warna
    display_red_channel(image)
    display_green_channel(image)
    display_blue_channel(image)

    # Konversi ke grayscale
    grayscale = convert_to_grayscale(image)

    # Konversi ke biner
    binary = convert_to_binary(grayscale, threshold=128)

    # Menampilkan hasil grayscale dan biner
    display_grayscale_and_binary(grayscale, binary)
    
