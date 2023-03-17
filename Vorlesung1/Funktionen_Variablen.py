# Funktionen
# Funktionen funktionieren auch ohne Argumente
print("Hello World")

# Variablen
a = "Hello" # Gleichzeichen Zuweisung --> == wenn Wert gleich sein soll
print(a)

name = input("Wie heißt du? ")
print("Hallo, " + name + "!") # Überladen einer Funktion (beliebig viele Argumente)

# end, um den Zeilenumbruch zu umgehen
fav_color = input("Was ist deine Lieblingsfarbe? ")
print(fav_color, end=',')
print (" finde ich auch super")

# Definieren von Funktionen
name = input("Wie heißt du? ")
name2 = input("Wer ist noch da? ")

def greet_user(name):
    print (f"Hallo, {name}") # formatierter String

greet_user(name)
greet_user(name2)

# Objekte haben bereits Funktionen
name = "Peter"
print (type(name))
print (name.upper())