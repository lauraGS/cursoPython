fic = open("../files/LICENCIA.txt", "r")
file = open("../files/testfile.txt", "w")


i = 0
for line in fic:
    if i < 16:
        print(line)
    elif i >=15 and  i < 21 :
        file.write(line + "\n")
    i = i + 1


file.close() 
fic.close()
