my_int = 5
my_float = 1.2
my_str = "Привет"
my_tuple = ('def', '456')
my_list = ['abc', '123']
my_dict = {'city': 'Moscow', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for a in super_list:
    print(f'{a} is {type(a)}')