# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power

# cube = to_power(3)
# print(cube(2))

# square = to_power(2)
# print(square(4))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
def decor(fun):
    def inner():
        a=fun()
        add = a+5
        return add
    return inner

@decor
def num():
    return 10

# result_fun = decor(num)
print(num())


'''

################################################################################

def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner    

@str_upper
def print_str():
    return "good morning"

print(print_str())

# d = str_upper(print_str)
# print(d())
