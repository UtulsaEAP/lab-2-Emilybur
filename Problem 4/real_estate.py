
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())

    change = current_price - last_month_price
    monthly_mortgage = (current_price * 0.051) / 12.

    print(f'This house is ${current_price}. The change is ${change} since last month.') 
    print(f'The estimated monthly mortgage is ${monthly_mortgage :.2f}.')
    # Your code goes here
if __name__ == "__main__":
    real_estate()