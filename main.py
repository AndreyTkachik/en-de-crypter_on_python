import sys
import caesar_cypher as cc
import vigener_cypher as vic
import vernam_cypher as vec


mode = sys.argv[1]
filename = sys.argv[2]

if mode == "caesar_encrypt":
    key = int(sys.argv[3])
    with open(filename, "r") as file:
        text = file.read()
    encrypted_text = cc.caesar_encrypt(text, key)
    with open(filename, "w") as file:
        file.write(encrypted_text)
    print("Encryption completed. Encrypted text in", filename)

elif mode == "caesar_decrypt":
    key = int(sys.argv[3])
    with open(filename, "r") as file:
        text = file.read()
    decrypted_text = cc.caesar_decrypt(text, key)
    with open(filename, "w") as file:
        file.write(decrypted_text)
    print("Decryption completed. Decrypted text in", filename)

elif mode == "vigenere_encrypt":
    key = sys.argv[3]
    with open(filename, "r") as file:
        text = file.read()
    encrypted_text = vic.vigenere_encrypt(text, key)
    with open(filename, "w") as file:
        file.write(encrypted_text)
    print("Encryption completed. Encrypted text in", filename)

elif mode == "vigenere_decrypt":
    key = sys.argv[3]
    with open(filename, "r") as file:
        text = file.read()
    decrypted_text = vic.vigenere_decrypt(text, key)
    with open(filename, "w") as file:
        file.write(decrypted_text)
    print("Decryption completed. Decrypted text in", filename)

elif mode == "vernam_encrypt":
    key = sys.argv[3]
    with open(filename, "r") as file:
        text = file.read()
    encrypted_text = vec.vernam_encrypt(text, key)
    with open(filename, "w") as file:
        file.write(encrypted_text)
    print("Encryption completed. Encrypted text in", filename)

elif mode == "vernam_decrypt":
    key = sys.argv[3]
    with open(filename, "r") as file:
        text = file.read()
    decrypted_text = vec.vernam_decrypt(text, key)
    with open(filename, "w") as file:
        file.write(decrypted_text)
    print("Decryption completed. Decrypted text in", filename)

elif mode == "caesar_brute_force":
    with open(filename, "r") as file:
        text = file.read()
    decrypted_texts = cc.caesar_brute_force(text)
    for key, decrypted_text in enumerate(decrypted_texts):
        print(f"Key: {key}, Decrypted text:")
        print(decrypted_text)

elif mode == "caesar_frequency_analysis_decrypt":
    with open(filename, "r") as file:
        text = file.read()
    keys = cc.caesar_frequency_analysis_decrypt(text)
    for key in keys:
        print(f"Key: {key} Decrypted text:")
        print(cc.caesar_decrypt(text, key))

else:
    print("Invalid mode specified.")
