#KDA Calculator
#This program calculates and evaluates the KDA (Kill/Death/Assist ratio) for League of Legends players.
#It practices basic Python concepts: print, input, conditional statements (if, else, elif).


print("\nWelcome to the KDA calculator 🧮")
name = input("What is your name? ") #User enters their name
lol = input("Do you play League of Legends? yes or no? ").lower() #User answers yes or no, using .lower() to ignore caps lock

#If the user answers "no" to the question above, the program won't welcome them or calculate the KDA

if lol == "no":
    print(f"Go home {name}! This calculator is only for LoL players. Other humans are not allowed 🚫")

#If the user answers "yes", a welcome message will appear, asking for kills, deaths and assists numbers

else:
    print(f"\nNice to meet you, {name}! 😄 Let’s evaluate your individual performance in League of Legends 🎮")

    kills = int(input("How many kills? ")) #Kills, deaths, and assists converted to integers
    deaths = int(input("How many deaths? "))
    assists = int(input("How many assists? "))

    if deaths == 0: #KDA won't be divided by deaths if deaths = 0 (division by zero is not possible)
        kda = kills + assists
        print(f"\nYour KDA of {kda:.2f} is puuurrrfect, {name}! 🙀🙀 Now stop playing and go study ⚠️")


    else:
        kda = (kills + assists) / deaths #If deaths > 0, then division is valid

        if kda < 1.5:
            print(f"\nI expected more from you, {name}! 😾... Your KDA of {kda:.2f} is horrible") #Print using :.2f to show only 2 decimal places

        elif kda >= 1.5 and kda < 2.5:
            print(f"\nMehh {name}! 😿 Your KDA of {kda:.2f} isn’t that bad, but... it’s not great either")

        elif kda >= 2.5 and kda < 4.0:
            print(f"\nI like it, {name}! 😺 Your KDA of {kda:.2f} is pretty decent")

        else:
            print(f"\nWow, {name}! 😸 Your KDA of {kda:.2f} is amazing! (don’t get too cocky, you’re not perfect yet)")

