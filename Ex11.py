def fine_calc(days_overdue):
    base_charge = 0.5
    day_charge = 0.8 * day
    max_charge = 30
    price = base_charge + day_charge
    if price > max_charge:
        price = 30
    return price

#Main Routine
day = int(input("Enter days overdue: "))
print(f"You have a fine of ${fine_calc(day):.2f}")


