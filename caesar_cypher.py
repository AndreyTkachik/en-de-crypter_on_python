import string
import constants as cnst

def caesar_encrypt(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


def frequency_analysis(text):
    alphabet = string.ascii_lowercase
    frequencies = {}
    for char in alphabet:
        frequencies[char] = 0
    total_chars = 0
    for char in text.lower():
        if char in alphabet:
            frequencies[char] += 1
            total_chars += 1
    for char in frequencies:
        frequencies[char] = frequencies[char] / total_chars
    return frequencies


def caesar_frequency_analysis_decrypt(text):
    alphabet = string.ascii_lowercase

    alphabet_frequency_boundary = sorted(cnst.alphabet_frequency,
                                         key=cnst.alphabet_frequency.__getitem__, reverse=True)[:cnst.boundary]

    encrypt_frequency = frequency_analysis(text)
    encrypt_frequency_boundary = sorted(encrypt_frequency,
                                        key=encrypt_frequency.__getitem__, reverse=True)[:cnst.boundary]
    decryption_keys = {key: 0.0 for key in range(len(alphabet))}
    for key in range(len(alphabet)):
        decrypt_frequency_boundary = {caesar_decrypt(char, key) for char in encrypt_frequency_boundary}
        decryption_keys[key] += (len(decrypt_frequency_boundary & set(alphabet_frequency_boundary)))
    decryption_keys = [key for key, step in decryption_keys.items() if step > cnst.minimal_step]
    return decryption_keys
