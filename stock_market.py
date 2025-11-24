#imports random for price changes
import random

#initialize variables some as int others as float
price = 100.00
day = 1
cash = 1000.00
shares = 0.0    

#initialize list for market history
price_history = []


#loop for the simluation of each day of stock market
while True:
    #logs price for future reference
    price_history.append(price)

    #function to calculate market trend based on 5-day simple moving average
    def calculateTrend():
        if day <= 5:
            print(" Not enough data to determine trend yet. \n")
        else:
            sum = 0
            for i in range(5):
                sum += price_history[(day-1) - (i)]
            sma = sum / 5
            if price > sma:
                print(" The market is trending upwards. \n")
            elif sma > price:
                print(" The market is trending downwards. \n")
        

    #identifies the change that will be made in price (randomly generated)
    deltaPrice = random.randint( -10, 10)

    #displays basic information of users portfolio and stock price
    print(" ------- DAY " + str(day) + " -------\n")
    print(" Price: "+ str(price)+"\n")
    print(" Cash: "+ str(cash)+"\n")
    print(" Shares: "+ str(shares)+"\n")
    print("Trend: ")
    calculateTrend()

    #the user is prompted to make a decision for the day
    option = input(" Enter your action: (B)uy, (S)ell, (W)ait, or (A)nalyze\n ")

    #buy option logic
    if (option == "B" or option == "b"):

        #gets desired shares from user and converts to float
        desiredShares_str = input(" How many shares would you like to buy?\n ")
        desiredShares = float(desiredShares_str)
        
        #loop to check for sufficient funds
        #if sufficient funds, completes transaction and breaks loop
        #if insufficient funds, prompts user to re-enter desired shares
        while cash - desiredShares*price >= 0:
            cash = cash - desiredShares*price
            shares = desiredShares + shares
            print(" You have successfully bought "+ str(desiredShares) + " shares!")
            print()
            break
        else:
            print(" You do not have sufficient funds to purchase this many shares.")
            print()
            desiredShares_str = input(" How many shares would you like to buy?")
            desiredShares = float(desiredShares_str)

    #sell option logic
    if ((option == "S" or option == "s") and shares > 0):

        #gets desired shares from user and converts to float
        desiredShares_str = input(" How many shares would you like to sell?\n")
        desiredShares = float(desiredShares_str)

        #loop to check for sufficient shares
        #if sufficient shares, completes transaction and breaks loop
        #if insufficient shares, prompts user to re-enter desired shares
        while shares - desiredShares >= 0:
            cash = cash + desiredShares*price
            shares = shares - desiredShares
            print(" You have successfully sold "+ str(desiredShares) + " shares!")
            print()
            break
        else:
            print(" You do not have the sufficient amount of shares to sell.")
            print()
            desiredShares_str = input(" How many shares would you like to sell?")
            desiredShares = float(desiredShares_str)


    #wait option logic
    if (option == "W" or option == "w"):
        print(" You have chosen to wait. \n")
    


    #Analyze option logic
    if (option == "A" or option == "a"):
        print(" ------- Price History -------: \n")
        #loops through list to display each day
        for i in range(len(price_history)):
            print(" Day " + str(i+1) + ": " + str(price_history[i]) + "\n")



    #logic to update price randomly for next day
    if(price + deltaPrice < 1):
        price = 1
    else:
        price += deltaPrice
    day += 1

    