def check_factor(num1, num2):
    if num1 % num2 == 0:
        return f"{num2} is a factor of {num1}"
    else:
        return f"{num2} is not a factor of {num1}"


# Main Routine
number_1 = int(input("Enter 1st number: "))
number_2 = int(input("Enter 2nd number: "))
print(check_factor(number_1, number_2))

