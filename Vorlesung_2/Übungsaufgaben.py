def aufgabe5 ():
    eingabe = input("Strings sind in Python veränderbar oder unveränderbar? ")
    print (eingabe)
    if eingabe == "unveränderbar" or eingabe == "unveraenderbar":
        print ("Richtig")
    elif eingabe == "veränderbar":
        print ("Falsch")
    else:
        print ("Bitte gebe 'unveränderbar' oder 'veränderbar' ein")

def aufgabe6 ():
    snackeingabe = input("Welchen Snack möchten sie haben? Zur Auswahl stehen: Mars, Snickers, Nüsse oder Äpfel! ")
    if snackeingabe == "Snickers" or snackeingabe == "Mars":
        print ("1 Euro")
    elif snackeingabe == "Nüsse":
        print("2 Euro")
    elif snackeingabe == "Äpfel":
        print("0.5 Euro")
    else:
        print ("Haben wir leider nicht im Sortiment")

def aufgabe7 ():
    def check_format():
        möglichkeiten = ['jpg', 'png', 'gif', 'jpeg']
        benutzereingabe = input("Geben Sie ihren Dateinamen ein: ")
        Dateiformat = benutzereingabe[-3:].lower()
        
        if Dateiformat in möglichkeiten:
            print ("image/" + Dateiformat)
        else:
            print ("application/octet-stream")
    check_format()

# aufgabe5()
# aufgabe6()
# aufgabe7()