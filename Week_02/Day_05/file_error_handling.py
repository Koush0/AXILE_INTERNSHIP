try:
    file = open("nonexistent.txt", "r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("File not found! Please check the file name.")
