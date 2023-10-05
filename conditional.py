""" 
Python Conditions and If statements

Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b 
"""
################ IF/ELIF/IFELSE STATEMENT ####################
a = int (input("Enter your age: "))
if a < 18 :
    print("You are an Child.")
elif 18 < a <= 40 :
    print("You are an Youth.")
else:
    print("You are an Old-Person.")

