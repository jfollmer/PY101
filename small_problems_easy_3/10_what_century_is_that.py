# PY101-109 Small Problems, Easy 3, Problem 10. "What Century is That?":

"""Write a function that takes a year as input and returns the century. 
The return value should be a string that begins with the century number, 
and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 
comprise the 20th century.

Examples:
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
"""

def add_ordinal_suffix(n):
    ordinal = str(n).rjust(2, '0')
    if ordinal.endswith('1') and ordinal[-2] != '1':
        return ordinal.removeprefix('0') + 'st'
    elif ordinal.endswith('2') and ordinal[-2] != '1':
        return ordinal.removeprefix('0') + 'nd'
    elif ordinal.endswith('3') and ordinal[-2] != '1':
        return ordinal.removeprefix('0') + 'rd'
    else:
        return ordinal.removeprefix('0') + 'th'

def century(year):
    prefix = str(year).rjust(3, '0')[:len(str(year)) - 2]
    suffix = str(year).rjust(3, '0')[len(str(year)) - 2:]

    century = int(prefix) + 1 if suffix != '00' else int(prefix)
    
    return add_ordinal_suffix(str(century))

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True


def add_ordinal_suffix(century):
    ones_place = century % 10
    tens_place = century % 100 // 10
    if ones_place == 1 and tens_place != 1:
        return str(century) + 'st'
    elif ones_place == 2 and tens_place != 1:
        return str(century) + 'nd'
    elif ones_place == 3 and tens_place != 1:
        return str(century) + 'rd'
    else:
        return str(century) + 'th'

def century(year):
    prefix = year // 100
    century = prefix + 1 if year % 100 != 0 else prefix
    
    return add_ordinal_suffix(century)

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True