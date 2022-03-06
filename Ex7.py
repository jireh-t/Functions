def print_name(name, number):
    for item in range(0, number):
        print(name)


#Main Routine
person_name = input("What is your name? ")
print_number = int(input("How many times would you like us to print it? "))
print_name(person_name.upper(), print_number)


