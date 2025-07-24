try:
    file = open("testFile.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("closing the file...")
    try:
        file.close()
    except NameError:
        print("file was never opened, so nothing to close")