file = open(input("filename/path: "),"r")
lines = file.readlines()
for i in range(len(lines)):
    if lines[i].startswith("v "):
        print(lines[i].replace("v ","(").strip("\n").replace(" ",", ")+")")