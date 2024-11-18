# Getting the prices for three items from the user
price1 = float(input("Enter the price of item 1: "))
price2 = float(input("Enter the price of item 2: "))
price3 = float(input("Enter the price of item 3: "))

# Print the entered values and Calculate the total price of the purchase items of the customer
print(f"Item 1: ${price1}, Item 2: ${price2}, Item 3: ${price3}")
totalPrice = price1 + price2 + price3
print(f"Total cost: ${totalPrice}")

#calculate the total price to know if its valid for a discount
if totalPrice > 100:
    discount = totalPrice * 0.10
    totalPrice = totalPrice - discount
    print("Congratulations! you're qualified for a 10% discount.")
else: 
    print("no discount available.")
    
#display the new discounted total price 
print (f"Your new total price is: ${totalPrice:}")

#Calculate the loyalty points  
loyaltyPoints = totalPrice// 10
print(f"congratulations you've also earned {loyaltyPoints} loyalty award points. ")


#Display the final ammount of price and loyalty points earned (rounded to two decimals)
print(f"The total price  of your purchase items: {totalPrice:.2f}")
print(f"The total amount of your loyalty points: {loyaltyPoints:.2f}")

#Accept payment and verification 
payment = float(input("Enter your money: "))
while payment < totalPrice:
    print(f"You're broke, please enter a valid amount of at least ${totalPrice}")
    payment = float(input("Enter your money: "))
print("Payment success")  

#Display the change of thec customer if applicable
change = payment - totalPrice
if payment > totalPrice:
    print(f"Your change: ${change}")
print("Thank you!")