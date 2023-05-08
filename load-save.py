boolA = False
boolB = True
boolC = True

save = [boolA, boolB, boolC]

f = open("save.txt", "w")
f.write("")
f.close()

f = open("save.txt", "a")
for i in range(len(save)):
    f.write(str(save[i]) + ",")
    print(str(save[i]))

f.close()
print("\n\n")

f = open("save.txt", "r")
line = f.readline()
f.close()

save = line.split(",")
print(save)

if save[0] == "True":
    boolA = True
else:
    boolA = False

if save[1] == "True":
    boolB = True
else:
    boolB = False

if save[2] == "True":
    boolC = True
else:
    boolC = False

print(str(boolA))
print(str(boolB))
print(str(boolC))
