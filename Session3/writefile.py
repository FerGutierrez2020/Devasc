with open("test.txt", "a+") as data:
    data.write("\nEsta es una nueva linea agregada por Python123")

with open ("test.txt", "r") as data: 
    print(data.read())