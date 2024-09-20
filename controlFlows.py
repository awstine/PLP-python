
def calculate_discount():
    price = float(input("enter original price: "))
    discount_percent = float(input("enter discount percentage: "))
    if discount_percent >= 20:
         final_price = price * (1-discount_percent/100)
         print(f"final price after discount{final_price}")
         return final_price
    else:
        print(f"no discount price remains {price}")
        return price

calculate_discount()

