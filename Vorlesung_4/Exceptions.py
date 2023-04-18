import random 
import sys
import cowsay

def exceptions():
    while True:     
        try:
            a = int(input("Nenne eine Zahl zwischen 1 und 10: "))
            b = 1/a
            print (b)
            break
        except ValueError:
            print ("Bitte ganze Zahl eingeben")
        else:
            if a >= 10 >1:
                raise print ("Nee")
            break
        finally:
            print ("Abbruch")

def random_library():
    # print(random.randint(10, 20))
    # print(random.choice(["a", "b"]))
    kandidaten = ["7", "8", "9", "Bube","König", "Ass"]
    random.shuffle(kandidaten)
    print(kandidaten)

def sys_library():
    if sys.argv[1] == "-formal":
        sys.exit("Sie")
    
    print("Ohne Formal")

def cowsay_library():
    print(cowsay.cow("Lol"))

cowsay_library()