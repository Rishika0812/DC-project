import tkinter as tk
from tkinter import ttk
from cryptography import vigenere_encrypt, vigenere_decrypt

class CryptographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography System")

        # Dark Mode Styling
        self.root.configure(bg="#222222")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#222222", foreground="#ffffff", font=("Arial", 12))
        self.style.configure("TEntry", fieldbackground="#333333", foreground="#ffffff", font=("Arial", 12))
        self.style.configure("TButton", background="#333333", foreground="#ffffff", font=("Arial", 12))
        self.style.configure("TFrame", background="#222222")

        # Input Frame
        self.input_frame = ttk.Frame(root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        self.input_label = ttk.Label(self.input_frame, text="Input Text:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.input_entry = ttk.Entry(self.input_frame, width=50)
        self.input_entry.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        # Key Frame
        self.key_frame = ttk.Frame(root)
        self.key_frame.grid(row=1, column=0, padx=10, pady=10)

        self.key_label = ttk.Label(self.key_frame, text="Encryption Key:")
        self.key_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.key_entry = ttk.Entry(self.key_frame, width=50)
        self.key_entry.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        # Encrypt & Decrypt Buttons
        self.button_frame = ttk.Frame(root)
        self.button_frame.grid(row=2, column=0, padx=10, pady=10)

        self.encrypt_button = ttk.Button(self.button_frame, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=0, column=0, padx=10, pady=5)

        self.decrypt_button = ttk.Button(self.button_frame, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=0, column=1, padx=10, pady=5)

        # Output Frame
        self.output_frame = ttk.Frame(root)
        self.output_frame.grid(row=3, column=0, padx=10, pady=10)

        self.output_label = ttk.Label(self.output_frame, text="Output Text:")
        self.output_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.output_text = tk.Text(self.output_frame, width=50, height=5)
        self.output_text.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    def encrypt(self):
        input_text = self.input_entry.get()
        key = self.key_entry.get()
        encrypted_text = vigenere_encrypt(input_text, key)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted_text)

    def decrypt(self):
        input_text = self.input_entry.get()
        key = self.key_entry.get()
        decrypted_text = vigenere_decrypt(input_text, key)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decrypted_text)

def main():
    root = tk.Tk()
    app = CryptographyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
