# SCT_CS_01
Caesar Cipher Tool is a simple Python desktop application built using Tkinter that allows users to encrypt and decrypt messages using the classic Caesar Cipher technique. It provides an intuitive graphical interface for entering text, specifying a shift value, and viewing the encrypted or decrypted result instantly. 
# Caesar Cipher Tool 

A beginner-friendly GUI application to encrypt and decrypt messages using the Caesar Cipher algorithm. Built with Python and Tkinter.

Features

- Encrypt plain text using Caesar Cipher
- Decrypt cipher text back to original message
- Handles both uppercase and lowercase letters
- Preserves spaces, punctuation, and non-alphabetic characters
- User-friendly interface with input fields and buttons
- Error handling for invalid shift values

 GUI Preview

- Message input field
- Shift value input (default: 3)
- Encrypt and Decrypt buttons
- Result display area

 Installation

1. Make sure you have Python 3 installed.
2. Clone this repository:

```bash
git clone https://github.com/yourusername/caesar-cipher-tool.git
cd caesar-cipher-tool
- Click Encrypt to encode or Decrypt to decode.
- View the result in the output box.
 How It Works
 Usage
- Enter your message or ciphertext.
- Specify a non-negative shift value (e.g., 3).

The Caesar Cipher shifts each letter in the message by a fixed number of positions in the alphabet. For example, with a shift of 3:
- A → D
- B → E
- Z → C
Decryption reverses the shift.
 Known Issues
- Shift values must be non-negative integers.
- Only alphabetic characters are shifted; others remain unchanged.
 Notes
- This tool is for educational purposes and not suitable for secure communication.
- GUI built with Tkinter, no external dependencies required.

