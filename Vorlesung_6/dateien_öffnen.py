count = 0

with open("gutenberg.txt" , "rt") as file:
    for line in file:
        if "Ham." in line:
            print(line.strip())
            count += 1
        print ("Hamlet played", count, "times")