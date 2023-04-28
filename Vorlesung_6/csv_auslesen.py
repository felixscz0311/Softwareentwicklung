with open("name.csv") as file:
    for line in file:
        row = line.strip().split(",")
        print (f"{row[0]} wurde geboren im Jahr {row[1]}")