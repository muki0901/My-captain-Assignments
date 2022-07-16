file_name = input("Enter the file name: ")
f = file_name.split(".")
print(f)    # printing as list
g = f[1]    
print(g)    #printing extension name
if g=="py":
    print("The extension of the file is python")

