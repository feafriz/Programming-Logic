#Sushi Restaurant Menu
#This program provides a price calculator for a sushi restaurant.
#It demonstrates basic Python concepts: print, input, and while loops.

print("🧝 Welcome to the Frieren Salmon Restaurant 🧝")
print("\n------------------ 𝐌𝐄𝐍𝐔 ------------------")
print("【1】 - 🍣   Salmon Urumaki  🍣 - 0.25 USD")
print("【2】 - 🍣  Salmon Hossomaki 🍣 - 0.15 USD")
print("【3】 - 🍣   Salmon Tempura  🍣 - 0.35 USD")
print("【4】 - 🍣   Salmon Sashimi  🍣 - 1.00 USD")
print("【5】 - 🍣   Salmon Nigiri   🍣 - 0.85 USD")
print("【6】 - 🍣   Salmon Temaki   🍣 - 5.00 USD")

total = 0 #Variable to store the total price of the order

while True: #While the program is on
    option = int(input("\nEnter the number of the chosen sushi: ")) #Client inputs the sushi number
    units = int(input("How many units?: ")) #Client inputs the units

    if option not in [1, 2, 3, 4, 5, 6]: #Program only accepts numbers from 1 to 6
        print("\n𝐏𝐋𝐄𝐀𝐒𝐄 𝐄𝐍𝐓𝐄𝐑 𝐀 𝐕𝐀𝐋𝐈𝐃 𝐒𝐔𝐒𝐇𝐈 𝐍𝐔𝐌𝐁𝐄𝐑")
        continue #Loop will return

    elif option == 1: #Each condition corresponds to an item on the sushi menu
        subtotal = 0.25 * units
        total += subtotal #Updates the total with the new subtotal
        print(f"The price is {subtotal} USD")

    elif option == 2:
        subtotal = 0.15 * units
        total += subtotal
        print(f"The price is {subtotal} USD")

    elif option == 3:
        subtotal = 0.35 * units
        total += subtotal
        print(f"The price is {subtotal} USD")

    elif option == 4:
        subtotal = 1.00 * units
        total += subtotal
        print(f"The price is {subtotal} USD")

    elif option == 5:
        subtotal = 0.85 * units
        total += subtotal
        print(f"The price is {subtotal} USD")

    elif option == 6:
        subtotal = 5.00 * units
        total += subtotal
        print(f"The price is {subtotal} USD")


    more = input("\nDo you want to order more sushi? 𝐘𝐄𝐒 or 𝐍𝐎? ")
    if more.lower() == "yes":
        continue #Continue if the client wants to order more

    else:
        break #Ends the loop

print(f"\nThe total of your order is {total:.2f} USD! Thanks for buying at Frieren Salmon Restaurant!") #Message of total order price after loop stops

