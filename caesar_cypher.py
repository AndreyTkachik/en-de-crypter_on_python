import string


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


def caesar_brute_force(text):
    alphabet = string.ascii_lowercase
    decrypted_texts = []
    for key in range(len(alphabet)):
        decrypted_text = caesar_decrypt(text, key)
        decrypted_texts.append(decrypted_text)
    return decrypted_texts


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
    boundary = 5
    minimal_step = 3

    alphabet = string.ascii_lowercase
    alphabet_frequency = {
        u'a': 0.08167, u'b': 0.01492, u'c': 0.02782, u'd': 0.04253, u'e': 0.12702, u'f': 0.02228, u'g': 0.02015,
        u'h': 0.06094, u'i': 0.06966, u'j': 0.00153, u'k': 0.00772, u'l': 0.04025, u'm': 0.02406, u'n': 0.06749,
        u'o': 0.07507, u'p': 0.01929, u'q': 0.00095, u'r': 0.05987, u's': 0.06327, u't': 0.09056, u'u': 0.02758,
        u'v': 0.00978, u'w': 0.0236, u'x': 0.0015, u'y': 0.01974, u'z': 0.00074,
    }
    alphabet_frequency_boundary = sorted(alphabet_frequency,
                                         key=alphabet_frequency.__getitem__, reverse=True)[:boundary]
    
    encrypt_frequency = frequency_analysis(text)
    encrypt_frequency_boundary = sorted(encrypt_frequency,
                                        key=encrypt_frequency.__getitem__, reverse=True)[:boundary]
    decryption_keys = {key: 0.0 for key in range(len(alphabet))}
    for key in range(len(alphabet)):
        decrypt_frequency_boundary = {caesar_decrypt(char, key) for char in encrypt_frequency_boundary}
        decryption_keys[key] += (len(decrypt_frequency_boundary & set(alphabet_frequency_boundary)))
    decryption_keys = [key for key, step in decryption_keys.items() if step > minimal_step]
    return decryption_keys
