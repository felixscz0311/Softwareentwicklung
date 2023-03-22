# # Übungsaufabe 0:
# eingabe = input("Geben einen Text ein: ")
# eingabe = eingabe.strip().upper()
# print(eingabe)

# # Übungsaufgabe 1:
# text = input("Gebe einen Text ein: ")
# ausgabe = text.replace(" ", "...").rstrip("...")
# print(ausgabe)

# # Übungsaufgabe 2:
# # Eingabe
# print("Gebe die Seite a deines Dreieckes an:", end=" ")
# input_a = input()
# print("Gebe die Seite b deines Dreieckes an:", end=" ")
# input_b =input()

# # casten in float
# input_a = float(input_a)
# input_b = float(input_b)

# # Ausgabe
# output = round((((input_a**2)+(input_b**2))**0.5),2)
# print("Die Seite c deines Dreieckes ist:", end=" ")
# print(output)

# def calculate_iban_checksum(iban):
#     iban = iban.upper().replace(" ", "") # Konvertiere IBAN zu Großbuchstaben
#     iban = iban.replace("44", "00")
#     iban = iban[4:] + iban[0:4] # Verschiebe die ersten 4 Zeichen ans Ende
#     iban = ''.join(str(int(ch, 36)) if ch.isalpha() else ch for ch in iban) # Ersetze Buchstaben durch Zahlen gemäß ihrem Alphabet-Index
#     remainder = int(iban) % 97 # Berechne den Rest bei der Division durch 97
#     return "{:02d}".format(98 - remainder) # Subtrahiere den Rest von 98 und gib die Prüfziffer zurück

# # Beispielaufruf
# iban = input()
# checksum = calculate_iban_checksum(iban)
# print("IBAN:", iban)
# print("Prüfziffer:", checksum)