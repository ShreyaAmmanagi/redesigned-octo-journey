def swapper():
    file1 = input("enter a file's name: ")
    with open(file1,"r") as a:
        dataA = a.read()
    file2 = input("enter the other file's name: ")
    with open(file2,"r") as a:
        dataB = a.read()
    with open(file1,"w") as a:
        a.write(dataB)
    with open(file2,"w") as a:
        a.write(dataA)
    print("swapping done!")
swapper()
