#movie tickets program

def main_routine():
    adult = 0
    student = 0
    child = 0
    gift = 0
    total = 0
    sold = 0

    ticket_wanted = input("Would you like to buy tickets? (Y/N) ").upper()
    while ticket_wanted != "N":
        ticket = input("What ticket do you want? \n"
              "A for adult, S for student, C for child, G for gift voucher.").upper()
        amount = int(input("How many would you like? "))

        confirm = input("Would you like to confirm? (Y/N) ").upper()
        if confirm == "Y":
            if ticket == "A":
                adult += amount
            elif ticket == "S":
                student += amount
            elif ticket == "C":
                adult += amount
            else:
                gift += amount

        return("Here is your total so far:\n"
               f"Adult = {adult}, Student = {student}, Child = {child}, Gift Voucher = {gift}")



# Main Routine
print(main_routine())



