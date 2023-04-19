import random

def aufgabe_15():
    range = int(input("Bitte gib eine Seitenzahl des Würfels ein: "))
    match range:
        case 4:
            option = random.randrange(1,4)
            print(f"Dein Würfelwurf: {option}")
        case 6:
            option = random.randrange(1,6)
            print(f"Dein Würfelwurf: {option}")
        case 8:
            option = random.randrange(1,8)
            print(f"Dein Würfelwurf: {option}")
        case 10:
            option = random.randrange(1,10)
            print(f"Dein Würfelwurf: {option}")
        case 12:
            option = random.randrange(1,12)
            print(f"Dein Würfelwurf: {option}")
        case 20:
            option = random.randrange(1,20)
            print(f"Dein Würfelwurf: {option}")
        case default:
            print("Bitte gib eine Seitenzahl von den genannten an: 4, 6, 8, 10, 12, 20")

aufgabe_15()