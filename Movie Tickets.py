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
        amount = globals(amount)
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

        return("Here is your total number of tickets so far:\n"
               f"Adult = {adult}, Student = {student}, Child = {child}, Gift Voucher = {gift}")
    while ticket_wanted != "Y":
        c_price = 7 * amount
        s_price = 9 * amount
        a_price = 12.5 * amount
        g_price = 0
        total = c_price + s_price + a_price

        if gift == 0:
            return(f"Your total price is for\n"
           f"Adult tickets are {a_price}, child tickets are {c_price}, student tickets are {s_price}, and your total is")

        else:
            return("Because of gift")

# Main Routine
print(main_routine())



