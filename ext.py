file_name = input("Enter the file name: ")
f = file_name.split(".")
print(f)
g = f[1]
print(g)
if g=="py":
    print("The extension of the file is python")

