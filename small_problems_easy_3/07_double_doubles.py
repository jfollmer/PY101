# PY101-109 Small Problems, Easy 3, Problem 7. "Double Doubles":

"""A double number is an even-length number whose left-side digits are 
exactly the same as its right-side digits. For example, 44, 3333, 
103103, and 7676 are all double numbers, whereas 444, 334433, and 107 
are not.

Write a function that returns the number provided as an argument 
multiplied by two, unless the argument is a double number. If the 
argument is a double number, return the double number as-is.

Examples:
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
"""


def twice(n):
    str_n = str(n)
    if len(str_n) % 2 == 0 and \
        str_n[0 : len(str_n) // 2] == str_n[len(str_n) // 2 : len(str_n)]:
        return n
    return n * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # 88 False
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # 206206 False
print(twice(3333) == 3333)              # 6666 False
print(twice(7676) == 7676)              # 15352 False


# Given solution splits this into two functions and uses a variable
# called center:

def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2
    left_number = string_number[:center]
    right_number = string_number[center:]

    return left_number == right_number

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2


# My second version, using a center variable and a comprehension like in
# one student solution:

def twice(n):
    str_n = str(n)
    center = len(str_n) // 2
    return n if str_n[:center] == str_n[center:] else n * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # 88 False
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # 206206 False
print(twice(3333) == 3333)              # 6666 False
print(twice(7676) == 7676)              # 15352 False