import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import io

# Initialize the main window
root = tk.Tk()
root.title("Image Encryptor and Decryptor")
root.geometry("600x800")

# Global variables to store the key and encrypted data
encryption_key = None
encrypted_image_data = None
decrypted_image_data = None

def encrypt_image():
    global encryption_key, encrypted_image_data

    # Open file dialog to select an image
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if not image_path:
        return

    # Generate a key for encryption
    encryption_key = Fernet.generate_key()
    cipher = Fernet(encryption_key)

    with Image.open(image_path) as img:
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format)
        img_bytes = img_byte_arr.getvalue()

        encrypted_image_data = cipher.encrypt(img_bytes)

    # Display the original image
    display_image(image_path, "Original Image")

    # Create a preview of the encrypted image (just for visual representation)
    encrypted_preview = create_encrypted_image_preview(encrypted_image_data)
    display_image(encrypted_preview, "Encrypted Image Preview")

    # Display the encryption key
    key_label.config(text=f"Encryption Key: {encryption_key.decode()}")

    # Enable the save button
    btn_save_encrypted.config(state=tk.NORMAL)

def create_encrypted_image_preview(encrypted_data):
    # Convert encrypted data to an image for preview
    size = int(len(encrypted_data)**0.5) + 1  # Calculate the image size
    encrypted_preview = Image.new('L', (size, size))
    encrypted_preview.putdata(list(encrypted_data) + [0] * (size*size - len(encrypted_data)))  # Padding with zeros
    encrypted_preview = encrypted_preview.resize((300, 300), Image.Resampling.LANCZOS)
    return encrypted_preview

def save_encrypted_data():
    global encryption_key, encrypted_image_data

    # Save the encrypted image data
    encrypted_image_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc")])
    if encrypted_image_path:
        with open(encrypted_image_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_image_data)

    # Save the encryption key
    key_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key Files", "*.key")])
    if key_path:
        with open(key_path, 'wb') as key_file:
            key_file.write(encryption_key)

    messagebox.showinfo("Success", "Encrypted image and key saved successfully.")

def decrypt_image():
    global encryption_key, encrypted_image_data, decrypted_image_data

    # Open file dialog to select an encrypted image
    encrypted_image_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if not encrypted_image_path:
        return

    # Open file dialog to select the encryption key
    key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
    if not key_path:
        return

    # Read the encryption key from file
    with open(key_path, 'rb') as key_file:
        encryption_key = key_file.read()

    # Read the encrypted image data from file
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_image_data = encrypted_image_file.read()

    try:
        cipher = Fernet(encryption_key)
        decrypted_bytes = cipher.decrypt(encrypted_image_data)

        img_byte_arr = io.BytesIO(decrypted_bytes)
        img = Image.open(img_byte_arr)

        # Save the decrypted image data for saving
        decrypted_image_data = img

        # Display decrypted image
        display_image(img, "Decrypted Image")

        # Enable the save button
        btn_save_decrypted.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Decryption Error", f"An error occurred during decryption: {e}")

def save_decrypted_image():
    global decrypted_image_data

    # Save decrypted image to a file
    decrypted_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if decrypted_image_path:
        decrypted_image_data.save(decrypted_image_path)
        messagebox.showinfo("Success", f"Decrypted image saved to: {decrypted_image_path}")

def display_image(image, title):
    img = Image.open(image) if isinstance(image, str) else image
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)

    panel = tk.Label(root, image=img)
    panel.image = img
    panel.grid(row=1, column=0, columnspan=2, pady=10)

    label = tk.Label(root, text=title)
    label.grid(row=2, column=0, columnspan=2)

# Create buttons for encrypting and decrypting images
btn_encrypt = tk.Button(root, text="Encrypt Image", command=encrypt_image)
btn_encrypt.grid(row=0, column=0, padx=20, pady=20)

btn_decrypt = tk.Button(root, text="Decrypt Image", command=decrypt_image)
btn_decrypt.grid(row=0, column=1, padx=20, pady=20)

# Create a label to display the encryption key
key_label = tk.Label(root, text="Encryption Key: None")
key_label.grid(row=3, column=0, columnspan=2, pady=10)

# Create buttons to save encrypted and decrypted data
btn_save_encrypted = tk.Button(root, text="Save Encrypted Data", command=save_encrypted_data, state=tk.DISABLED)
btn_save_encrypted.grid(row=4, column=0, padx=20, pady=20)

btn_save_decrypted = tk.Button(root, text="Save Decrypted Image", command=save_decrypted_image, state=tk.DISABLED)
btn_save_decrypted.grid(row=4, column=1, padx=20, pady=20)

# Run the application
root.mainloop()
