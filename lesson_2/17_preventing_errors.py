# PY101, Lesson 2, assignment 17. 'Preventing Errors':


# Comment out whichever section you're not testing:


"""LBYL (look before you leap):
"""

# def lower_first(word):
#     # Ensure word is a string, and just return word as-is if not
#     if type(word) != str:
#         return word
    
#     # Ensure word contains at least one character, return as-is if not
#     if len(word) == 0:
#         return word
    
#     # We now know it's a string with at least one character. Thus the
#     # following code will run without raising an error:
#     return word[0].lower() + word[1:]

# print(lower_first("fOO"))   # fOO
# print(lower_first(32))      # 32
# print(lower_first(""))      # (prints nothing)
# print(repr(lower_first("")))    # ''


"""EAFP: It's easier to ask forgiveness than permission:
"""

# def lower_first(word):
#     try:
#         return word[0].lower() + word[1:]
#     except:
#         return word # handle exceptions by returning word as-is

# print(lower_first("FOO"))   # fOO
# print(lower_first(32))      # 32
# print(lower_first(""))      # (prints nothing)
# print(repr(lower_first("")))    # ''


"""Planning Your Code example:
Writing a function to insert a new element to a list in proper 
alphabetic sorted position (I went ahead and wrote the function; still
had to do some debugging but I knew what to debug for since we thought
about edge cases beforehand; I left in these debugging lines):
"""

def alpha_insert(lst, new_element):
    if not lst:
        lst.append(new_element)
        print(lst)
        return lst
    elif len(lst) == 1 and new_element <= lst[0]:
        # print('debug', lst, lst[0], new_element)
        lst.insert(0, new_element)
        print(lst)
        return lst
    else:
        for item in lst:
            if new_element >= item:
                # print(lst.index(item))
                # print(lst)
                lst.insert(lst.index(item) + 1, new_element)
                print(lst)
                return lst
            
def alpha_insert_v2(lst, new_element):
    lst.append(new_element)
    lst.sort()
    return lst

countries = ['Australia', 'Cuba', 'Senegal']

alpha_insert(countries, 'Brazil')

print(', '.join(countries)) # "Australia, Cuba, Senegal"

# Make sure it can handle:
alpha_insert([], 'Brazil')              # inserting into an empty list
alpha_insert(['Brazil'], 'Australia')   # at the beginning of a list
alpha_insert(['Brazil'], 'Cuba')        # at the end of a list
alpha_insert(['Brazil'], 'Brazil')      # duplicate entry
alpha_insert_v2([], 'Brazil')              # inserting into an empty list
alpha_insert_v2(['Brazil'], 'Australia')   # at the beginning of a list
alpha_insert_v2(['Brazil'], 'Cuba')        # at the end of a list
alpha_insert_v2(['Brazil'], 'Brazil')      # duplicate entry

# countries.insert(0, 'test')
# print(countries)
# print('Brazil' >= 'Australia')