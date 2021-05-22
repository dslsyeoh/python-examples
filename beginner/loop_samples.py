import random

sample_num_list = [1, 30, 12, 50, 100]
sample_str_list = ["Hello", "World", "How are you?"]


def generate_number_list(size):
    number_list = []
    for x in range(size):
        number_list.append(x)
    return number_list


def random_list_generator():
    number_list = []
    for _ in range(10):
        number_list.append(random.randint(1, 100))
    return number_list


def list_prime_number(my_list):
    result = []
    for value in my_list:
        if value == 0:
            continue
        if 1 <= value <= 3:
            result.append(value)
        else:
            counter = 0
            for index in range(2, len(my_list)):
                if value % my_list[index] == 0:
                    counter += 1
            if counter == 1:
                result.append(value)
    return result


def concat_words_from_list(my_list):
    result = ""
    for value in my_list:
        result += f"{value}, "
    return result


def concat_list():
    return sample_str_list + sample_num_list


def update_list(my_list, value, action=""):
    if action == "add":
        my_list.append(value)
    else:
        my_list.remove(value)
    return my_list


def reverse_list(my_list):
    return my_list[::-1]


def split_sentence(sentence):
    return sentence.split()


def filter_list(my_list, skip):
    filtered = []
    for value in my_list:
        if value == skip:
            continue
        filtered.append(value)
    return filtered


def find_longest_word(my_list):
    max_length = 0
    position = 0
    for index in range(len(my_list)):
        length = len(my_list[index])
        if index == 0:
            max_length = length
            position = index
            continue
        if length > max_length:
            max_length = length
            position = index

    return my_list[position]


def check_prime_number(my_list):
    prime_numbers = []
    for value in my_list:
        counter = 0
        for n in range(2, value + 1):
            if value % n == 0:
                counter += 1
        if counter == 1:
            prime_numbers.append(value)
    return prime_numbers


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_2(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    return fact


list_of_words = split_sentence("Hello World, How are haha you?")

print("Generate number list of size 10: {}".format(generate_number_list(10)))
print("Generate random list: {}".format(random_list_generator()))
print("Prime number in {}: {}".format(generate_number_list(10), list_prime_number(generate_number_list(10))))
print("Index of 30 in {}: {}".format(sample_num_list, sample_num_list.index(30)))
print("Index of World in {}: {}".format(sample_str_list, sample_str_list.index("World")))
print("Concat words from {}: {}".format(sample_str_list, concat_words_from_list(sample_str_list)))
print("Sum of {}: {}".format(sample_num_list, sum(sample_num_list)))
print("Concat {} {}: {}".format(sample_str_list, sample_num_list, concat_list()))
print("Add \"d\" into {}: {}".format(["a", "b", "c"], update_list(["a", "b", "c"], "d", "add")))
print("Remove \"c\" from {}: {}".format(["a", "b", "c"], update_list(["a", "b", "c"], "c")))
print("Reverse {}: {}".format(sample_num_list, reverse_list(sample_num_list)))
print("Repeat {} times of {}: {}".format(3, [1, 2, 3], [1, 2, 3] * 3))
print("Filter {} from {}: {}".format("haha", list_of_words, filter_list(list_of_words, "haha")))
print("Longest word in {}: {}".format(["Hello", "Max", "Nice to meet you", "Hello World"],
                                      find_longest_word(["Hello", "Max", "Nice to meet you", "Hello World"])))
print("Prime number in {}: {}".format([20, 3, 5, 100, 11], check_prime_number([20, 100, 3, 5, 11])))
print(f"factorial of 5: {factorial(5)}")
print(f"factorial of 5: {factorial_2(5)}")
