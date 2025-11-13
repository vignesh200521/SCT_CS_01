import tkinter as tk
from tkinter import messagebox

class CaesarCipherApp:
    def _init_(self, master):
        self.master = master
        master.title("Caesar Cipher Tool")
        master.geometry("450x350")
        master.config(bg="#f0f0f0")

        # --- Cipher Logic ---
        
        def caesar_cipher(text, shift, mode='encrypt'):
            """Encrypts or decrypts text using the Caesar Cipher."""
            result = ''
            shift = shift % 26 # Handle shifts greater than 26

            if mode == 'decrypt':
                shift = -shift

            for char in text:
                if 'a' <= char <= 'z':
                    start = ord('a')
                    # Apply shift: (current_position + shift) % 26
                    shifted_char_ord = (ord(char) - start + shift) % 26 + start
                    result += chr(shifted_char_ord)
                elif 'A' <= char <= 'Z':
                    start = ord('A')
                    # Apply shift: (current_position + shift) % 26
                    shifted_char_ord = (ord(char) - start + shift) % 26 + start
                    result += chr(shifted_char_ord)
                else:
                    # Keep non-alphabetic characters unchanged (spaces, punctuation, etc.)
                    result += char
            return result

        # --- GUI Functions ---

        def encrypt_message():
            """Gets input, performs encryption, and displays the result."""
            try:
                message = self.message_entry.get()
                shift = int(self.shift_entry.get())
                if shift < 0:
                     messagebox.showerror("Error", "Shift value must be non-negative.")
                     return

                encrypted_text = caesar_cipher(message, shift, mode='encrypt')
                self.result_text.set(encrypted_text)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer for the shift value.")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        def decrypt_message():
            """Gets input, performs decryption, and displays the result."""
            try:
                message = self.message_entry.get()
                shift = int(self.shift_entry.get())
                if shift < 0:
                     messagebox.showerror("Error", "Shift value must be non-negative.")
                     return

                decrypted_text = caesar_cipher(message, shift, mode='decrypt')
                self.result_text.set(decrypted_text)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer for the shift value.")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        
        # --- GUI Layout ---

        # 1. Message Input
        tk.Label(master, text="Message/Ciphertext:", bg="#f0f0f0", font=('Arial', 10, 'bold')).pack(pady=(10, 0))
        self.message_entry = tk.Entry(master, width=50, bd=2)
        self.message_entry.pack(pady=5, padx=10)

        # 2. Shift Value Input
        tk.Label(master, text="Shift Value (e.g., 3 for C):", bg="#f0f0f0", font=('Arial', 10, 'bold')).pack(pady=(5, 0))
        self.shift_entry = tk.Entry(master, width=10, bd=2)
        self.shift_entry.pack(pady=5)
        self.shift_entry.insert(0, "3") # Default shift value

        # 3. Buttons Frame
        button_frame = tk.Frame(master, bg="#f0f0f0")
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Encrypt", command=encrypt_message, 
                  bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'), width=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Decrypt", command=decrypt_message, 
                  bg="#f44336", fg="white", font=('Arial', 10, 'bold'), width=10).pack(side=tk.LEFT, padx=10)

        # 4. Result Output
        tk.Label(master, text="Result:", bg="#f0f0f0", font=('Arial', 10, 'bold')).pack(pady=(5, 0))
        self.result_text = tk.StringVar()
        self.result_label = tk.Label(master, textvariable=self.result_text, 
                                      bg="white", relief=tk.SUNKEN, width=40, height=3, 
                                      wraplength=350, justify=tk.LEFT)
        self.result_label.pack(pady=5, padx=10)


# Main application loop
if _name_ == "_main_":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
