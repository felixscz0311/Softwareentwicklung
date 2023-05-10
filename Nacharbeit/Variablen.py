# Erstellen von Variablen
x = 5
y = "Felix"

# Casting von Variablen (Spezifischen Datentyp festlegen)
z = int(4)

# Abfragen der Variablen
print (x)

# Variaben sind Case Sensitive (Groß- und Kleinschreibung beeinflussen (a und A ist nicht gleich))

# Viele Variablen gleichzeitig initalisieren
a, b = "Felix", "Tom"

# Unpacking von Variablen
früchte = ["Apfel", "Bananen", "Kirschen"]
A, B, C = früchte
print(A, B, C)

# Globale Variablen können außerhalb von Funktionen und in Funktionen benuzt werden
global x, y, z