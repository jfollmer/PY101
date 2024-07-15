# PY101-109 Small Problems, Easy 1, Problem 1:

# Write a function that takes one integer argument and returns True when 
# the number's absolute value is odd, False otherwise.

def abs_is_odd(integer):
    return abs(integer) % 2 == 1

print(abs_is_odd(3))
print(abs_is_odd(4))
print(abs_is_odd(-3))
print(abs_is_odd(-4))