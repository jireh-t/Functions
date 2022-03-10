# Program which checks for a valid number

# Ask user for a number
error = "Whoops! Please enter an integer\n"
valid = False
while not valid:
    try:
        response = int(input("Enter a number between 1 and 10: "))
        if low <= response <= high:
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
print(response)
