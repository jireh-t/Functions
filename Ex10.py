def calc_gst(net_price):
    return net_price * 1.15

# Main Routine
price = float(input("What is the price? "))
print(f"Your price is ${calc_gst(price):.2f}, including GST")
