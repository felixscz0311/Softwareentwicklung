# Übungsaufabe 0:
eingabe = input("Geben einen Text ein: ")
eingabe = eingabe.strip().upper()
print(eingabe)

# Übungsaufgabe 1:
text = input("Gebe einen Text ein: ")
ausgabe = text.replace(" ", "...").rstrip("...")
print(ausgabe)

# Übungsaufgabe 2:
# Eingabe
print("Gebe die Seite a deines Dreieckes an:", end=" ")
input_a = input()
print("Gebe die Seite b deines Dreieckes an:", end=" ")
input_b =input()

# casten in float
input_a = float(input_a)
input_b = float(input_b)

# Ausgabe
output = round((((input_a**2)+(input_b**2))**0.5),2)
print("Die Seite c deines Dreieckes ist:", end=" ")
print(output)