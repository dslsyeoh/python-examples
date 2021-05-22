def is_empty(text):
    if text:
        print(text)
    else:
        print("Empty")


def find_largest(x, y):
    if x > y:
        return x
    else:
        return y


my_set = {1, 2, 3}
my_dict = {"key": "value1"}

is_empty("Hello World")
is_empty("")
print(find_largest(10, 20))
print(10 if 10 > 20 else 20)
print(f"is set empty: { True if not my_set else False }")
print(f"is dict empty: { True if not dict() else False }")
print(f"is dict empty: { True if not my_dict else False }")
print(f'is 10 type int: { True if type(10) is int else False }')
print(f'is "10" type int: { True if type("10") is not int else False }')
print(f'is abc == abc: { True if "abc" == "abc" else False }')
print(f'is 10 != 11: { True if 10 != 11 else False }')
