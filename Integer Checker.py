# Program which checks for a valid number

# Function
def int_check(question, low, high):
    error = "Whoops! Must be an integer\n"
    valid = False
    while not valid:
        try:
            response = int(input("{} {} and {}: ".format(question, low, high)))
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine
num_1 = int_check("Enter a number between", 1, 15)
num_2 = int_check("Enter a number between", 5, 10)
print("\n List number is {}; and \n2nd number is {}".formt(num_1, num_2))
