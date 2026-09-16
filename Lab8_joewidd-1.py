"""
Lab8_joewidd-1.py,
Joe Widdifield,
a program that validates a 12-digit UPC-A code,
9/15/2026
"""
def find_upc():
    """find and validate upc code"""
    try:
        upc = input("Enter a 12-digit UPC: ")
        upc_check = int(upc)
        print("the upc entered is " + f"{upc_check}")
    except ValueError:
        print("Please enter a valid 12 digit UPC code")


find_upc()