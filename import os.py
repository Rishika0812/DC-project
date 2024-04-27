import os

# Step 1: Create project directory
project_directory = "cryptography_system"
os.makedirs(project_directory, exist_ok=True)
print(f"Created project directory: {project_directory}")

# Step 2: Create cryptography.py file
cryptography_code = """
# cryptography.py

# Implementation of cryptography algorithms

# Example function for Vigenère Cipher encryption
def vigenere_encrypt(plain_text, key):
    # Implementation goes here
    pass

# Example function for Vigenère Cipher decryption
def vigenere_decrypt(encrypted_text, key):
    # Implementation goes here
    pass

# Example function for Polybius Cipher encryption
def polybius_encrypt(plain_text):
    # Implementation goes here
    pass

# Example function for Polybius Cipher decryption
def polybius_decrypt(encrypted_text):
    # Implementation goes here
    pass
"""
cryptography_file_path = os.path.join(project_directory, "cryptography.py")
with open(cryptography_file_path, "w") as file:
    file.write(cryptography_code)
print(f"Created cryptography.py file: {cryptography_file_path}")

# Step 3: Create gui.py file
gui_code = """
import tkinter as tk
from tkinter import ttk
from cryptography import vigenere_encrypt, vigenere_decrypt, polybius_encrypt, polybius_decrypt

# Implementation of GUI using Tkinter

class CryptographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography System")

        # Input
        self.input_label = ttk.Label(root, text="Input Text:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.input_entry = ttk.Entry(root, width=50)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

        # Encryption Key
        self.key_label = ttk.Label(root, text="Encryption Key:")
        self.key_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.key_entry = ttk.Entry(root, width=50)
        self.key_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

        # Encrypt Button
        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=2, column=1, padx=5, pady=5)

        # Output
        self.output_label = ttk.Label(root, text="Encrypted Text:")
        self.output_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.output_text = tk.Text(root, width=50, height=5)
        self.output_text.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

    def encrypt(self):
        input_text = self.input_entry.get()
        key = self.key_entry.get()
        encrypted_text = vigenere_encrypt(input_text, key)  # Call encryption function
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted_text)

def main():
    root = tk.Tk()
    app = CryptographyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
"""
gui_file_path = os.path.join(project_directory, "gui.py")
with open(gui_file_path, "w") as file:
    file.write(gui_code)
print(f"Created gui.py file: {gui_file_path}")

# Step 4: Optionally, create README file
readme_text = """
# Cryptography System

This project contains the implementation of cryptography algorithms and a graphical user interface (GUI) using Tkinter.

## Files
- cryptography.py: Python script containing the implementation of cryptography algorithms.
- gui.py: Python script containing the GUI implementation using Tkinter.
"""
readme_file_path = os.path.join(project_directory, "README.md")
with open(readme_file_path, "w") as file:
    file.write(readme_text)
print(f"Created README.md file: {readme_file_path}")
