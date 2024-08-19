
# Image Encryptor and Decryptor Application

The Image Encryptor and Decryptor application is a Python-based GUI tool that allows users to encrypt and decrypt image files using the `Fernet` symmetric encryption method from the `cryptography` library. This tool ensures that sensitive images are securely encrypted and can only be decrypted using the correct encryption key.


## Authors

- [@sonaliiiiiiiiii](https://github.com/sonaliiiiiiiiii)


## Tech Stack

### Tech Stack

The **Image Encryptor and Decryptor** application utilizes the following technologies:

- **Programming Language**: 
  - **Python 3.11.9**: The core programming language used to develop the application.

- **GUI Framework**:
  - **Tkinter**: The built-in Python library used to create the graphical user interface (GUI).

- **Encryption Library**:
  - **Cryptography (Fernet)**: A Python library used for symmetric encryption and decryption of image data.

- **Image Processing Library**:
  - **Pillow**: A Python Imaging Library (PIL) fork used to handle image file manipulation and processing.

- **File Handling**:
  - **os** and **filedialog**: Standard Python libraries used for file operations like saving and loading files.




## Features

1. **Image Encryption**:
   - **Secure Encryption**: Encrypts images using the `Fernet` symmetric encryption method, ensuring that the image data is securely protected.
   - **Encryption Key Generation**: Automatically generates a unique encryption key for each image encryption process, which is necessary for decryption.

2. **Image Decryption**:
   - **Decrypt Encrypted Images**: Decrypts images that were previously encrypted with the application, restoring them to their original form using the corresponding encryption key.

3. **User-Friendly Interface**:
   - **Simple GUI**: The application features an easy-to-use graphical user interface built with `Tkinter`, making it accessible for users without extensive technical knowledge.
   - **Scrollable Content**: The interface includes scrollable sections for easy navigation and viewing of content within the application.

4. **Image Preview**:
   - **Original Image Display**: Displays the original image before encryption.
   - **Encrypted Image Preview**: Shows a visual representation of the encrypted image data, providing an abstract view of the encryption result.

5. **File Management**:
   - **Save Encrypted Data**: Allows users to save the encrypted image data to a file, along with the encryption key, for future decryption.
   - **Save Decrypted Image**: Enables saving the decrypted image file once the decryption process is complete.

6. **Error Handling**:
   - **Error Alerts**: Displays error messages in case of any issues during the encryption or decryption process, such as file handling errors or decryption failures.

These features provide a comprehensive and secure way to encrypt and decrypt images, ensuring data privacy and integrity while maintaining ease of use.

## Deployment

To deploy the **Image Encryptor and Decryptor** application, follow these steps:

#### 1. **Local Deployment**

This method allows you to run the application on your local machine.

##### Prerequisites:
- Python 3.x installed on your machine.
- Required Python libraries (`cryptography`, `Pillow`, and `tkinter`).

##### Steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/image-encryptor-decryptor.git
   cd image-encryptor-decryptor
   ```

2. **Install Dependencies**:
   - Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install the required libraries:
   ```bash
   pip install cryptography pillow
   ```

3. **Run the Application**:
   - Execute the Python script to launch the GUI:
   ```bash
   python image_encryptor_decryptor.py
   ```
   - The application window should open, and you can start using the image encryption and decryption features.

#### 2. **Packaging as an Executable**

If you want to distribute the application without requiring users to have Python installed, you can package it as an executable file.

##### Using `PyInstaller`:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Create an Executable**:
   - Run the following command in the project directory:
   ```bash
   pyinstaller --onefile --windowed image_encryptor_decryptor.py
   ```
   - This will create a standalone executable in the `dist` directory.

3. **Distribute the Executable**:
   - You can now share the executable file with others. They can run the application without needing Python or the dependencies installed.

##### Optional - Custom Icon:
   - You can add a custom icon to the executable by including the `--icon=youricon.ico` option:
   ```bash
   pyinstaller --onefile --windowed --icon=youricon.ico image_encryptor_decryptor.py
   ```

#### 3. **Cross-Platform Deployment**

To make the application available on multiple operating systems:

- **Windows**: Follow the steps for local deployment or create a Windows executable using `PyInstaller`.
- **macOS**: Use `py2app` for macOS applications, or use `PyInstaller` with the `--windowed` flag.
- **Linux**: Use `PyInstaller` or distribute the Python script directly.

#### 4. **Cloud Deployment**

Deploying this application on the cloud (e.g., AWS, Heroku) is less common for a GUI-based tool. However, you can deploy it on a remote server with a GUI (e.g., using VNC) or convert it into a web application using `Flask` or `Django` for deployment.

### Notes

- **Dependencies**: Ensure all dependencies are correctly installed on the target machine.
- **Security**: Be cautious when handling encryption keys, especially in cloud environments. Store them securely.

This deployment guide should help you run and distribute the Image Encryptor and Decryptor application on various platforms.
## Usage


 1. **Secure Image Storage**
   - **Privacy Protection**: If you have sensitive images (e.g., personal photos, confidential documents scanned as images), this tool allows you to encrypt them, ensuring that only those with the correct decryption key can view them.
   - **Data Security**: Encrypting images before storing them on cloud services or external storage devices protects them from unauthorized access.

2. **Secure Image Transmission**
   - **Email or Messaging**: If you need to send an image over email or a messaging service, encrypting it first ensures that even if the communication is intercepted, the image data remains secure.
   - **Public Sharing**: You can share encrypted images publicly without revealing their contents, and only share the decryption key with trusted individuals.

3. **Compliance with Data Protection Regulations**
   - **Regulatory Compliance**: For businesses or professionals handling sensitive images (e.g., medical images, legal documents), encrypting these files helps comply with data protection laws like GDPR, HIPAA, etc.

4. **Personal Use**
   - **Digital Diary**: If you keep a digital photo diary or journal, encrypting your images adds an extra layer of privacy.
   - **Secure Memories**: Protect personal memories or sensitive photos from accidental exposure by encrypting them.

5. **Educational Purposes**
   - **Learning Cryptography**: This application can serve as a practical tool for students and enthusiasts to understand how encryption and decryption work in real-world applications.
   - **Demonstrating Security Concepts**: Teachers and trainers can use this tool to demonstrate the importance of data security and how cryptography can be applied to protect digital assets.

6. **Preventing Image Tampering**
   - **Integrity Check**: By encrypting images, you can ensure that the original image remains untampered. Any attempt to modify the encrypted file will corrupt it, making tampering evident.

## Support

For support, feedback, or suggestions, please contact [sos.glu16@outlook.com]. Contributions to the project are welcome via pull requests on GitHub.


## Acknowledgements

I extend my sincere thanks to my mentors for their valuable guidance throughout this project, which was crucial in bringing this project to life. Lastly, I thank the open-source community for providing the resources that made this project possible.
