print("WARNING: When i tried this one i had to select each triangle() in desmos and hit CTRL+A for some reason. I don't know why!")
file = open(input("filename/path: "),"r")
lines = file.readlines()
final = ""
count = 0
for i in range(len(lines)):
    if count == 0:
        final += "triangle("
    if lines[i].startswith("v "):
        if count == 2:
            final += lines[i].replace("v ","(").strip("\n").replace(" ",", ")+")"
        else:
            final += lines[i].replace("v ","(").strip("\n").replace(" ",", ")+"),"
        count = count + 1
        if count >= 3:
            final += ")\n"
            count = 0

print(final)