print("=================== Variable ===================")
a = 10
b = "my text"

c, d = 20, 30

print("a: {}".format(a))
print("b: {}".format(b))
print("c: {}, d: {}".format(c, d))

print("swap c to d and d to c")
c, d = d, c
print("c: {}, d: {}".format(c, d))
print("=================== variable ===================\n")

print("=================== List ===================")
my_list = [1, 2, 3]
print("my list: {}".format(my_list))
my_list.append(10)
print("my list: {}".format(my_list))
my_list.remove(10)
print("my list: {}".format(my_list))
print("my list: {}".format(my_list.pop()))
print("my list: {}".format(my_list))
print("my list: {}".format(my_list.pop(1)))
print("my list: {}".format(my_list))
print("=================== List ===================\n")

print("=================== Dictionary ===================")
my_dict = {"key": "value"}
print("my dict: {}".format(my_dict))
my_dict["key2"] = "value 2"
print("my dict: {}".format(my_dict))
my_dict["key2"] = "updated value 2"
print("my dict: {}".format(my_dict))
print("my dict keys: {}".format(my_dict.keys()))
print("my dict values: {}".format(my_dict.values()))
print("my dict[\"key\"]: {}".format(my_dict["key"]))
print("my dict[\"key2\"]: {}".format(my_dict["key2"]))
print("=================== Dictionary ===================\n")

print("=================== Set ===================")
my_set = {1, 2, 3}
print("my set: {}".format(my_set))
my_set.add(10)
print("my set: {}".format(my_set))
my_set.remove(10)
print("my set: {}".format(my_set))
print("my set: {}".format(my_set.pop()))
print("my set: {}".format(my_set))
print("=================== Set ===================\n")

print("=================== Tuple ===================")
my_tuple = (10, "a")
print("my tuple: {}".format(my_tuple))
print("my tuple[0]: {}".format(my_tuple[0]))
print("my tuple[1]: {}".format(my_tuple[1]))
print("tuple: {}".format(("hello", "world")))
print("=================== Tuple ===================")
