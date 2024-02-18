files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    f = open(file, "r")
    fileval = f.read()
    print(fileval)
    f.close()