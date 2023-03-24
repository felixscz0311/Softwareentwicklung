import math

#satz des Pythagoras mit eigener Eingabe des Benutzers

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

#input der zwei Zaheln von dem benutzer selbst

a = float(input("Bitte geben Sie den ersten Zahl ein: "))
b = float(input("Bitte geben Sie den zweiten Zahl ein: "))

#funktion zum Berechnung der Pythagoras mit der Eingabe des Benutzers

print("Die Pythagoras mit der Eingabe des Benutzers ist:", pythagoras(a, b))