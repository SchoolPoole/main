#Nick Poole CIST1305 9/7/23
#The main function
def main():
    print("Welcome to the program")
    monthlySales = getSales()
    isBonus(monthlySales)
    isDayOff(monthlySales)

# Get monthly sales
def getSales():
        monthlySales = float(input("Enter monthly sales $"))
        return monthlySales

#Determine Bonus should be awarded
def isBonus(monthlySales):
    if monthlySales>= 100000:
        print("You have earned a $5,000 bonus!!!")

#Determine if the empolyee gets day off
def isDayOff(monthlySales):
    if monthlySales>= 112500:
        print("All employees get one day off!!!")
#calls main
main()