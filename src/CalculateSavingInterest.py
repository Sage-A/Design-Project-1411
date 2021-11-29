# Calculates Saving Interests

def calc_savings_interest():
    principle = float(input("What is the starting amount in your savings account? "))
    quest_4 = input("Is your interest rate annual or monthly? ")

    # Let there be a selection to choose either annual or monthly
    if quest_4 == "annual":
        interest_rate = float(input("What is your percent interest rate? "))/100
        n = 1
    elif quest_4 == "monthly":
        interest_rate = float(input("What is your percent interest rate? "))/100
        n = 12
    total_years = float(input("How many years will this investment be growing? "))
    amount = principle*((1+(interest_rate/n))**(total_years*n))
    print("If you let your principle investment of "+str(principle)+" grow for "+str(total_years)+" years at a "+str(interest_rate)+" interest rate, you will end up with $"+str(amount))
