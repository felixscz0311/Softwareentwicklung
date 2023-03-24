class Katze:
    def __init__(self, name): # initialisieren von Katze
        self.name = name
    
    def speak (self):
        print("Meow" + self.name)
    
    def walk(self):
        print("Walk" + self.name)


charlie = Katze("Charlie")
tom = Katze("Tom")

charlie.speak()
tom.walk()