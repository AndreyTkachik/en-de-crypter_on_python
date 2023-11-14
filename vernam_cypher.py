import string


def vernam_encrypt(text, key):
    alphabet = string.ascii_lowercase
    text = text.lower()
    key = key.lower()
    encrypted_text = ""
    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            char_index = alphabet.index(char)
            key_letter = alphabet[i % len(key)]
            key_index = alphabet.index(key_letter)
            new_index = (char_index + key_index) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text


def vernam_decrypt(text, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    decrypted_text = ""
    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            char_index = alphabet.index(char)
            key_letter = alphabet[i % len(key)]
            key_index = alphabet.index(key_letter)
            new_index = (char_index - key_index) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
    return decrypted_text
