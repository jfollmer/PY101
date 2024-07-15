# PY101-109 Small Problems, Easy 1, Problem 5. "Tip Calculator":

"""Create a simple tip calculator. The program should prompt for a bill 
amount and a tip rate. The program must compute the tip, then print both 
the tip and the total amount of the bill. You can ignore input 
validation and assume that the user will enter valid numbers.

What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00
"""


bill_amount = float(input("What is the bill? ").strip('$ '))
tip_percent = float(input("What is the tip percentage? ").strip('%. '))

tip = tip_percent * .01 * bill_amount
total = bill_amount + tip

print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")