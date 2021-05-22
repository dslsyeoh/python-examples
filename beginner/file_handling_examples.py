def read(file_path):
    try:
        f = open(file_path, "r")
        for line in f.readlines():
            print(line.strip())
    except IOError:
        print("An error was found. Either path is incorrect or file doesn't exist!")
    else:
        f.close()


def write(file_path, text):
    try:
        f = open(file_path, "w")
        f.write(text)
        f.flush()
    except IOError:
        print("An error was found. Either path is incorrect or file doesn't exist!")
    else:
        f.close()


def append(file_path, text):
    try:
        f = open(file_path, "a")
        f.write(text + "\n")
    except IOError:
        print("An error was found. Either path is incorrect or file doesn't exist!")
    else:
        f.close()


def read_write(file_path, text):
    try:
        f = open(file_path, "r+")
        f.write(text + "\n")
        f.seek(0)
        for line in f.readlines():
            print(line.strip())
    except IOError:
        print("An error was found. Either path is incorrect or file doesn't exist!")
    else:
        f.close()


def append_read(file_path, text):
    try:
        f = open(file_path, "a+")
        f.write(text + "\n")
        f.seek(0)
        for line in f.readlines():
            print(line.strip())
    except IOError:
        print("An error was found. Either path is incorrect or file doesn't exist!")
    else:
        f.close()


read("../resources/hello.txt")
write("../resources/my_text.txt", "I am fine!")
append("../resources/hello.txt", "I am fine!")
read_write("../resources/read_write.txt", "This is read write.")
append_read("../resources/append_read.txt", "This is append read.")
