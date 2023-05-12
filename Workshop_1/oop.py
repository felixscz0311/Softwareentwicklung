# Magic Methoden sind die Methoden mit zwei Unterstrichen
# Vererbungen lesen: Ein Mensch ist ein Lebewesen
class Lebewesen:
    alter = 0

    def atmen(self):
        print("Ich atme")

class Mensch(Lebewesen):
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def reden(self, schreien=False):
        text = f"Hallo, ich bin {self.name} und {self.alter} Jahre alt"
        if schreien:
            text.upper()
        print(text)

person1 = Mensch("Peter", 12)

person1.reden()
person1.atmen()