def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("cannot divide by zero")
    except TypeError:
        print("Incorrect type")
    except:
        pass


def open_file(file_path):
    try:
        f = open(file_path, "r")
    except FileNotFoundError:
        print(f"{file_path} not found")
    else:
        f.close()


divide(10, 0)
divide("10", "10")
open_file("abc.txt")

try:
    _ = int(input("Enter a number: "))
except ValueError:
    print('You are supposed to enter a number.')
