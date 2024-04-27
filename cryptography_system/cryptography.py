# cryptography.py

# Implementation of cryptography algorithms

# Vigenère Cipher Encryption
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)].upper()) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

# Vigenère Cipher Decryption
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)].upper()) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

# Polybius Cipher Encryption
def polybius_encrypt(plain_text):
    key = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
           'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24',
           'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34',
           'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44',
           'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54',
           'Z': '55'}
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            encrypted_text += key[char.upper()] + " "
        elif char == ' ':
            encrypted_text += ' '
    return encrypted_text.strip()

# Polybius Cipher Decryption
def polybius_decrypt(encrypted_text):
    key = {'11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E',
           '21': 'F', '22': 'G', '23': 'H', '24': 'I', '25': 'J',
           '31': 'L', '32': 'M', '33': 'N', '34': 'O', '35': 'P',
           '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U',
           '51': 'V', '52': 'W', '53': 'X', '54': 'Y', '55': 'Z'}
    encrypted_text = encrypted_text.split()
    decrypted_text = ""
    for code in encrypted_text:
        if code in key:
            decrypted_text += key[code]
        elif code == ' ':
            decrypted_text += ' '
    return decrypted_text
