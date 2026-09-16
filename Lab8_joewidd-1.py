"""
Lab8_joewidd-1.py,
Joe Widdifield,
a program that validates a 12-digit UPC-A code,
9/15/2026
"""
upc = input("Enter a 12-digit UPC: ")

def find_upc(upc):
    """find and validate upc-a code"""
while True:
    check_sum = 0
    if len(upc) != 12 or not upc.isnumeric():
        print("Please enter a 12 digit number")
        upc = input("Enter a 12-digit UPC: ")
    else:
        check_digit = int(upc[11]) #12th digit
        first_11_digits = int(upc[:11])
        print("\nthe first 11 digits are: " + str(first_11_digits) + ".")
        print("The provided check digit is: " + str(check_digit) + ".")
        upc_digits = list(map(int, upc))
        for i, digit in enumerate(upc_digits[:11]):
            if i % 2 == 0 :
                check_sum = check_sum + (3 * digit)
            else :
                check_sum += digit
        computed_check_digit = 10 - (check_sum % 10)
        if computed_check_digit == 10 :
            computed_check_digit = 0
        final_digit = upc_digits[-1]
        if computed_check_digit == final_digit :
            print("\nCalculating...")
            print("The expected check digit is " + str(final_digit) + ".")
            print("Valid")
        else :
            print("\nCalculating...")
            print("The expected check digit is " + str(final_digit) + ".")
            print("Invalid")
        break

find_upc(upc)