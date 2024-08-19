import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import io
import os

class ImageEncryptorDecryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor and Decryptor")
        self.root.geometry("600x800")
        self.root.config(bg="#e6e6e6")

        self.encryption_key = None
        self.encrypted_image_data = None
        self.decrypted_image_data = None

        self.setup_ui()

    def setup_ui(self):
        # Main Frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas for scrollable content
        canvas = tk.Canvas(main_frame, bg="#e6e6e6")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Content Frame inside Canvas
        content_frame = ttk.Frame(canvas, padding=10)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Control Frame for buttons
        control_frame = ttk.Frame(content_frame, padding=10)
        control_frame.pack(pady=20)

        # Image Display Frame
        self.image_frame = ttk.Frame(content_frame, padding=10)
        self.image_frame.pack(pady=20)

        # Key Display Frame
        key_frame = ttk.Frame(content_frame, padding=10)
        key_frame.pack(pady=20)

        # Buttons
        btn_encrypt = ttk.Button(control_frame, text="Encrypt Image", command=self.encrypt_image)
        btn_encrypt.grid(row=0, column=0, padx=20, pady=10)

        btn_decrypt = ttk.Button(control_frame, text="Decrypt Image", command=self.decrypt_image)
        btn_decrypt.grid(row=0, column=1, padx=20, pady=10)

        # Encryption Key Display Label
        self.key_label = tk.Label(key_frame, text="Encryption Key: None", font=("Arial", 12), bg="#e6e6e6")
        self.key_label.pack(pady=10)

        # Save Buttons
        self.btn_save_encrypted = ttk.Button(key_frame, text="Save Encrypted Data", command=self.save_encrypted_data, state=tk.DISABLED)
        self.btn_save_encrypted.pack(side=tk.LEFT, padx=20, pady=10)

        self.btn_save_decrypted = ttk.Button(key_frame, text="Save Decrypted Image", command=self.save_decrypted_image, state=tk.DISABLED)
        self.btn_save_decrypted.pack(side=tk.RIGHT, padx=20, pady=10)

    def encrypt_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if not image_path:
            return

        self.encryption_key = Fernet.generate_key()
        cipher = Fernet(self.encryption_key)

        try:
            with Image.open(image_path) as img:
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format=img.format)
                img_bytes = img_byte_arr.getvalue()

            self.encrypted_image_data = cipher.encrypt(img_bytes)

            # Display the original and encrypted images
            self.display_image(image_path, "Original Image")
            encrypted_preview = self.create_encrypted_image_preview(self.encrypted_image_data)
            self.display_image(encrypted_preview, "Encrypted Image Preview")

            # Display the encryption key
            self.key_label.config(text=f"Encryption Key: {self.encryption_key.decode()}", fg="blue")

            # Enable the save button
            self.btn_save_encrypted.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Encryption Error", f"An error occurred during encryption: {e}")

    def create_encrypted_image_preview(self, encrypted_data):
        size = int(len(encrypted_data)**0.5) + 1
        encrypted_preview = Image.new('L', (size, size))
        encrypted_preview.putdata(list(encrypted_data) + [0] * (size*size - len(encrypted_data)))
        encrypted_preview = encrypted_preview.resize((300, 300), Image.Resampling.LANCZOS)
        return encrypted_preview

    def save_encrypted_data(self):
        encrypted_image_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc")])
        if not encrypted_image_path:
            return

        key_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key Files", "*.key")])
        if not key_path:
            return

        try:
            with open(encrypted_image_path, 'wb') as encrypted_file:
                encrypted_file.write(self.encrypted_image_data)

            with open(key_path, 'wb') as key_file:
                key_file.write(self.encryption_key)

            messagebox.showinfo("Success", "Encrypted image and key saved successfully.")
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving: {e}")

    def decrypt_image(self):
        encrypted_image_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
        if not encrypted_image_path:
            return

        key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
        if not key_path:
            return

        try:
            with open(key_path, 'rb') as key_file:
                self.encryption_key = key_file.read()

            with open(encrypted_image_path, 'rb') as encrypted_image_file:
                self.encrypted_image_data = encrypted_image_file.read()

            cipher = Fernet(self.encryption_key)
            decrypted_bytes = cipher.decrypt(self.encrypted_image_data)

            img_byte_arr = io.BytesIO(decrypted_bytes)
            img = Image.open(img_byte_arr)

            self.decrypted_image_data = img
            self.display_image(img, "Decrypted Image")

            self.btn_save_decrypted.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Decryption Error", f"An error occurred during decryption: {e}")

    def save_decrypted_image(self):
        decrypted_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not decrypted_image_path:
            return

        try:
            self.decrypted_image_data.save(decrypted_image_path)
            messagebox.showinfo("Success", f"Decrypted image saved to: {decrypted_image_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving: {e}")

    def display_image(self, image, title):
        img = Image.open(image) if isinstance(image, str) else image
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)

        panel = ttk.Label(self.image_frame, image=img, background="#e6e6e6")
        panel.image = img
        panel.pack(pady=10)

        label = ttk.Label(self.image_frame, text=title, background="#e6e6e6", font=("Arial", 12))
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorDecryptorApp(root)
    root.mainloop()
