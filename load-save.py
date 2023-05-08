#bool variables you want to save
boolA = False
boolB = True
boolC = True

#create a string with each bool in it
save = [boolA, boolB, boolC]


#SAVE INFORMATION:

#this creates a text file name "save.txt". The "w" means that you are writing to it
f = open("save.txt", "w")
f.write("") #this is creating the file/clearing it if it already exists
f.close() #closes the file

f = open("save.txt", "a") #opens the "save.txt" file, the "a" means that you are appending to it
for i in range(len(save)): #for loop going through the save list
    f.write(str(save[i]) + ",") #systematically saving each value in the save list to "save.txt" with a comma after it

f.close() #close the file



#LOAD INFORMATION:

f = open("save.txt", "r") #opens "save.txt", the "r" means that you are reading the file
line = f.readline() #saves the first line of "save.txt" as a variable
f.close() #close the file

save = line.split(",") #.split() save the line we loaded from "save.txt" into the save variable but splits it at each comma; 1,2,3 would become ["1","2","3"]

#sets the variable true or false
if save[0] == "True":
    boolA = True
else:
    boolA = False

#sets the variable true or false
if save[1] == "True":
    boolB = True
else:
    boolB = False

#sets the variable true or false
if save[2] == "True":
    boolC = True
else:
    boolC = False

#prints the bool values
print(str(boolA))
print(str(boolB))
print(str(boolC))
