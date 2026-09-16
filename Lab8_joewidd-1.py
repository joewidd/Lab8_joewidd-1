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
    try:
        if len(upc) != 12:
            print("Please enter exactly 12 digits")
            break
        upc_check = int(upc)
        print("the upc entered is " + f"{upc_check}")
        break
    except ValueError:
        print("Please enter a 12 digit number")
        break



find_upc()