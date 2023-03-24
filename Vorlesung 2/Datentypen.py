from decimal import Decimal as d
from fractions import Fraction as f

def true_devision ():
    a = 3 // 2    # rundet nach unten auf ganze Zahlen

def float_problem():
    a = 0.3-0.1*3
    print (a)
    a = d('0.3')-d('0.1')*3
    print(a)

def brüche():
    print(f(10,6)) # gekürzt

def strings():
    a = """Hello World""" # mehrzeilig
    a = "Hello Word\h\"" # Escape Caracters
    print (len(a))
    print (a)

def prints ():
    a = "123456789"
    b = "0123456789"
    c = "Meine Kontonummer ist {nummer1} und {nummer2}." # Keyword Arguments
    print (c.format(nummer1 = a,nummer2 = b))

def schleifen():
    a=5
    b=5
    if a==b:
        print("A ist gleich B") 
        a = a + 5
        print (a)
        print (b)
    else:
        print("A ist nicht gleich B")


# true_devision()
# float_problem()
# brüche()
# strings()
# prints()
schleifen()