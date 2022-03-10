# Program which checks for a valid number

# Function
def int_check(question, low, high):


# Main Routine
error = "Whoops! Must be an integer\n"
valid = False
while not valid:
    try:
        response = int(input("{} {} and {}: ".format(question, low, high)))
        if 1 <= response <= 10:
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
print(response)
