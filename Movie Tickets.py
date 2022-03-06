#movie tickets program

def main_routine():
    adult = 0
    student = 0
    child = 0
    gift = 0
    total = 0
    sold = 0

    ticket_wanted = input("Would you like to buy tickets? (Y/N) ")
    while ticket_wanted != "N":
        input("What ticket do you want? \n"
              "A for adult, S for student, C for child, G for gift voucher.")

