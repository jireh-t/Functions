#movie tickets program

def main_routine():
    adult = 0
    student = 0
    child = 0
    gift = 0
    total = 0
    sold = 0

    ticket_wanted = input("do you want tickets? ").upper()
    while ticket_wanted != "N":
        ticket = sell_ticket()


        numT = int(input("How many? "))
        confirm = input("confirm?").upper()

        if confirm == "Y":
            price = numT * float(get_price(ticket))
            total += price
            sold += numT
            if ticket == "A":
                adult += numT
            elif ticket == "C":
                child += numT
            elif ticket == "S":
                student += numT
            else:
                gift += numT

            ticket_wanted = input("\nDo you want "
                                  "another ticket").upper()

            print("-------------------------------------------------")
            print(f"the total is {sold}\n"
                  f"this was made of: \n"
                  f"\t{adult} for adults\n"
                  f"\t{student} for students\n"
                  f"\t{child} for children\n"
                  f"\t{gift} gift vouchers \n")
            print(f"sales came to a ${total:.2f}")
            print("-------------------------------------------------")

def sell_ticket():
    ticket_type = input("what kind of ticket do you want: \n"
                        "\tA for adults, or\n"
                        "\tS for students, or\n"
                        "\tC for child, or\n"
                        "\tG for Gift Voucher\n").upper()
    return ticket_type


def get_price(type_):
    prices = [["A", 12.5],["S", 9],["C", 7],["G",0]]
    for price in prices:
        if price[0] == type_:
            return price[1]




#main routine
print("********* Fan Fair Movies Ticket Sales *********\n")
main_routine()
