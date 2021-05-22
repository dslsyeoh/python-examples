def greeting():
    print("Hello World")


def greeting_with_name_argument(name):
    print(f"Greeting {name}!")


def process_list(my_list):
    return filter_keywords(my_list, ["aaa", "bbb"])


def filter_keywords(my_list, keywords):
    filtered_list = []
    for value in my_list:
        if keywords.__contains__(value):
            continue
        filtered_list.append(value)
    return filtered_list


def function_with_default_argument_value(v1=10, v2=10):
    return f"{v1} + {v2} = {v1 + v2}"


greeting()
greeting_with_name_argument("John")
print(process_list(["Hello", "World", "aaa", "bbb", "John"]))
print(function_with_default_argument_value())
print(function_with_default_argument_value(20))
print(function_with_default_argument_value(20, 30))
