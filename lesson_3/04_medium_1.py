# PY101, Lesson 3, Assignment 5. "Practice Problems: Medium 1":

# Come back to / repeat questions 4, 7. Also still want a deeper 
# understanding of 5 but that seems like a deep-ish rabbithole for 
# later.

"""Question 1: Let's do some "ASCII Art": a stone-age form of nerd 
artwork from back in the days before computers had video screens.
For this practice problem, write a program that outputs The Flintstones 
Rock! 10 times, with each line prefixed by one more hyphen than the line 
above it. The output should start out like this:
-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
"""

string = "The Flinstones Rock!"
for num in range(1, 11):
    print(str('-' * num) + string)

# Question 2: Alan wrote the following function, which was intended to 
# return all of the factors of number:
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
"""Alyssa noticed that this code would fail when the input is a negative 
number, and asked Alan to change the loop. How can he make this work? 
Note that we're not looking to find the factors for negative numbers, 
but we want to handle it gracefully instead of going into an infinite 
loop.
Bonus Question: What is the purpose of number % divisor == 0 in that 
code?
"""

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(1))
print(factors(4))
print(factors(0))
print(factors(-1))

# Bonus answer: To determine which divisors evenly divide into number, 
# i.e. they have no remainders. In other words, the factors of number.

"""Question 3: Alyssa was asked to write an implementation of a rolling 
buffer. You can add and remove elements from a rolling buffer. However, 
once the buffer becomes full, any new elements will displace the oldest 
elements in the buffer.
She wrote two implementations of the code for adding elements to the 
buffer:
"""

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# Is there a difference between these implementations, other than the 
# way she is adding an element to the buffer?

"""The second function will use more memory, because the + operator
returns a new list, so the buffer list will be copied into a new object 
each time with new_element added to it each time the function is called, 
then the variable buffer will be reassigned to point to the new object.
The first function is less memory-intensive because the .append() method
mutates the list in place.
"""

# Question 4: What will the following two lines of code output?
print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)
# Don't look at the solution before you answer.

"""First line prints 0.9, the value returned by that expression, which
adds the numbers 0.3 and 0.6 together.
Second line prints True. The expression is evaluated left-to-right, so
the two numbers are added together first, then the result is compared 
for value equality to the number 0.9, and the two are equal.

Given solution: Due to floating point imprecision, the first line 
actually prints 0.8999999999999999, and the second line prints False.
"""

# Question 5: What do you think the following code will output?
nan_value = float("nan")
print(nan_value == float("nan"))
# Bonus Question: How can you reliably test if a value is nan?

"""This should print True. I'm not sure how to test it. Possibly 
float("NaN")? The Type Conversions assignment in Lesson 2 isn't clear.
After running this, looking at the hint, and testing some more, I still 
don't understand why it prints False. But the bonus answer is:
"""
import math
print(math.isnan(nan_value))

# Question 6: What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

"""This code outputs 34. Although we pass the value of answer to 
mess_with_it, which returns the value + 8 (50 in this case), we assign
its return value to a different variable, new_answer, instead of to the
original variable name, answer, so answer remains unaffected.
"""

# Question 7: One day, Spot was playing with the Munster family's home 
# computer, and he wrote a small program to mess with their demographic 
# data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:
mess_with_demographics(munsters)
# Before Grandpa could stop him, Spot hit the Enter key with his tail. 
# Did the family's data get ransacked? Why or why not?

"""Yes, because dictionary view objects are linked to the original 
dictionary, so when one is mutated, the other reflects the change.

The given solution does not mention dictionary view objects. Try again
later.
"""

"""Question 8: Function and method calls can take expressions as 
arguments. Suppose we define a function named rps as follows, which 
follows the classic rules of the rock-paper-scissors game, but with a 
slight twist: in the event of a tie, it just returns the choice made by 
both players.
"""
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

# What does the following code output?
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

"""This outputs "paper". The two innermost function calls' return values
are "paper" and "rock", so we're left with:
print(rps(rps("paper", "rock"), "rock))
The the innermost of those returns "paper", so we have:
print(rps("paper", "rock"))
Which returns "paper" to print().
"""

# Question 9: Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# What will the following function invocation return?
bar(foo())

"""The innermost function is called first, foo(). We pass no arguments,
and it doesn't do anything with the single parameter it defines anyway,
so it simply returns "yes", which is passed to bar(). Since we pass an
argument, the default value it defines for its parameter is overridden.
The expression after "return" evaluates as follows:
param == "no" => False
False and foo() => False
False or "no" => "no"
So "no" is the final value returned.
"""

"""Question 10: In Python, every object has a unique identifier that can 
be accessed using the id() function. This function returns the identity 
of an object, which is guaranteed to be unique for the object's 
lifetime. For certain basic immutable data types like short strings or 
integers, Python might reuse the memory address for objects with the 
same value. This is known as "interning".
Given the following code, predict the output:
"""
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# This should print True, because they are all pointing to the same 
# object, the interned integer 42.