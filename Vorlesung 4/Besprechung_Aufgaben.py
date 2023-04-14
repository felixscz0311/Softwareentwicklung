ciphertext = input("Bitte Text eingeben: ")

def aufgabe12 (plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    for char in plaintext:
        if char in plaintext:
            index = alphabet.index(char)
            index_neu = index + key
            ciphertext += alphabet[index_neu % len(alphabet)]
        else:
            ciphertext += char
    return ciphertext   