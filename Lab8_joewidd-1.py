"""
Lab8_joewidd-1.py,
Joe Widdifield,
a program that validates a 12-digit UPC-A code,
9/15/2026
"""
def find_upc():
    """find and validate upc-a code"""
while True:
    upc = input("Enter a 12-digit UPC: ")
    if len(upc) != 12 or not upc.isnumeric():
        print("Please enter a 12 digit number")
    else:
        print("the upc entered is " + f"{upc}")
        break

find_upc()