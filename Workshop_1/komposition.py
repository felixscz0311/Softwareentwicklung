# Komposition lesen: Ein Mensch hat ein Auto

class Mensch:
    alter = ""

class Car:
    ps = 400
    farbe = "rot"
    name = "Ferrari"

class Student(Mensch):
    studiengang = ""
    auto = None

auto1 = Car()

student1 = Student()
student1.auto = auto1

print(student1.auto.name)