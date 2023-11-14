import string


def vigenere_encrypt(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    key_index = 0
    for char in text.lower():
        if char in alphabet:
            key_letter = alphabet[key_index % len(key)].lower()
            key_index += 1
            key_shift = alphabet.index(key_letter)
            char_index = alphabet.index(char)
            new_index = (char_index + key_shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_decrypt(text, key):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    key_index = 0
    for char in text.lower():
        if char in alphabet:
            key_letter = alphabet[key_index % len(key)].lower()
            key_index += 1
            key_shift = alphabet.index(key_letter)
            char_index = alphabet.index(char)
            new_index = (char_index - key_shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
    return decrypted_text
