import tkinter as tk
from tkinter import filedialog
import caesar_cypher as cc
import vigener_cypher as vic
import vernam_cypher as vec


def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as file:
        text = file.read()
    return text, file_path


def save_file(text, file_path):
    with open(file_path, "w") as file:
        file.write(text)


def caesar_encrypt(key):
    text, file_path = open_file()
    encrypted_text = cc.caesar_encrypt(text, key)
    save_file(encrypted_text, file_path)
    result_label.config(text="Encryption completed. Encrypted text in " + file_path)

def caesar_decrypt(key):
    text, file_path = open_file()
    decrypted_text = cc.caesar_decrypt(text, key)
    save_file(decrypted_text, file_path)
    result_label.config(text="Decryption completed. Decrypted text in " + file_path)


def vigenere_encrypt(key):
    text, file_path = open_file()
    encrypted_text = vic.vigenere_encrypt(text, key)
    save_file(encrypted_text, file_path)
    result_label.config(text="Encryption completed. Encrypted text in " + file_path)


def vigenere_decrypt(key):
    text, file_path = open_file()
    decrypted_text = vic.vigenere_decrypt(text, key)
    save_file(decrypted_text, file_path)
    result_label.config(text="Decryption completed. Decrypted text in " + file_path)


def vernam_encrypt(key):
    text, file_path = open_file()
    encrypted_text = vec.vernam_encrypt(text, key)
    save_file(encrypted_text, file_path)
    result_label.config(text="Encryption completed. Encrypted text in " + file_path)


def vernam_decrypt(key):
    text, file_path = open_file()
    decrypted_text = vec.vernam_decrypt(text, key)
    save_file(decrypted_text, file_path)
    result_label.config(text="Decryption completed. Decrypted text in " + file_path)


def caesar_frequency_analysis_decrypt():
    text, file_path = open_file()
    keys = cc.caesar_frequency_analysis_decrypt(text)
    decrypted_text = ""
    for key in keys:
        decrypted_text += "Key: " + str(key) + " Decrypted text:\n"
        decrypted_text += cc.caesar_decrypt(text, key)
    save_file(decrypted_text, file_path)
    result_label.config(text="Frequency analysis completed. Decrypted text in " + file_path)


root = tk.Tk()
root.title("Text Encryption/Decryption")

key_entry = tk.Entry(root)
key_entry.pack()

encrypt_button = tk.Button(root, text="Caesar Encrypt", command=lambda: caesar_encrypt(int(key_entry.get())))
encrypt_button.pack()

encrypt_button = tk.Button(root, text="Vigenere Encrypt", command=lambda: vigenere_encrypt(key_entry.get()))
encrypt_button.pack()

encrypt_button = tk.Button(root, text="Vernam Encrypt", command=lambda: vernam_encrypt(key_entry.get()))
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Caesar Decrypt", command=lambda: caesar_decrypt(int(key_entry.get())))
decrypt_button.pack()

decrypt_button = tk.Button(root, text="Vigenere Decrypt", command=lambda: vigenere_decrypt(key_entry.get()))
decrypt_button.pack()

decrypt_button = tk.Button(root, text="Vernam Decrypt", command=lambda: vernam_decrypt(key_entry.get()))
decrypt_button.pack()

decrypt_button = tk.Button(root, text="Frequency analysis Caesar Decrypt", command=lambda: caesar_frequency_analysis_decrypt())
decrypt_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
