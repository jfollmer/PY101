# PY101, Lesson 2, assignment 24. 'Variable Scope':

"""Question 1: What will the following code print and why? Don't run it 
until you have tried to answer.
"""

num = 5

def my_func():
    print(num) # 5

my_func()

"""Prints 5 because the function my_func() is able to access the variable
num from the global scope.
"""


"""Question 2: What will the following code print and why? Don't run it 
until you have tried to answer.
"""

num = 5

def my_func():
    num = 10

my_func()
print(num) # 5

"""The variable num is initialized on line 23. When my_func() is called 
on line 26, it creates a new local variable num, which shadows the 
global variable. However, it doesn't do anything with this variable, and
it is discarded after the function finishes executing. When we pass num
to print() on line 29, it prints the global variable's value, 5.
"""


"""Question 3: What will the following code print and why? Don't run it 
until you have tried to answer.
"""

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num) # 10

"""The variable num is initialized on line 42 in the global scope. On 
line 46, the global keyword instructs the function to use the global 
variable. When num is assigned on the next line of the function body, 
it is actually reassignment of the global variable. So when num is 
passed to print() on line 50, the value it was reassigned to, 10,
prints.
"""


"""Question 4: What will the following code print and why? Don't run it 
until you have tried to answer.
"""

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var) # Hello World

    inner()

outer()

"""In the function outer(), a local variable outer_var is initialized
with the value 'Hello'. Then a nested function, inner(), is defined, 
which is called on the last line of outer(). This function initializes
its own local variable inner_var with the value 'World', the calls
print() with each of these values passed as arguments. The nonlocal
variable outer_var is accessible within inner(), so the values are both
printed on one line with a space between: 'Hello World'.
"""


"""Question 5: What will the following code print and why? Don't run it 
until you have tried to answer.
"""

def my_func():
    num = 10

my_func()
print(num) # NameError

"""my_func() initializes a local variable num, however nothing is done
with it, and it's discarded when the function finishes executing. When
we try to print num on line 94, a NameError is raised, since there is no
global variable num.

The given solution describes this more concisely: 'This code raises a
NameError since the variable num is defined within the function my_func
and is not accessible outside of its scope.'
"""


"""Question 6: What will the following code print and why? Don't run it 
until you have tried to answer.
"""

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x) # Inner 1: 25

    def inner_func2():
        print("Inner 2:", x) # Inner 2: 15

    inner_func1()
    inner_func2()

my_func()

"""The function my_func() contains two nested functions: inner_func1 and
inner_func2(). The variable x is initialized in the outer function 
(my_func()) with the value 15. inner_func1() initialized its own local
variable x with the value 25, which shadows the outer variable and is 
printed when we call print within that function. inner_func2() does not
define any local variables and is able to access the outer variable x, 
so the value assigned in the outer function, 15, is printed when we pass
x to print() within inner_func2().
"""