# Expenses Goal

# Input expenses and income to find total spare money and transform data into a graph
def expenses_calc():
    
    # Initialize variables
    quest_1 = "y"
    total_expenses = 0.0
    i = 1
    quest_2 = 0
    s_goal_2 = 0.0
    s_time_2 = 0.0
    m_cont_2 = 0.0
    initial_balance = 0.0

    # Input monthly expenses
    print("Input monthly expenses")
    while quest_1 == "y":
        total_expenses = total_expenses + float(input("Expense #"+str(i)+ " : "))
        quest_1 = input("Do you have more expenses? y/n > ")
        i+=1
    print("Your total monthy expenses are " + str(total_expenses))

    # Input total income to calculate net income
    total_income = float(input("What is your total monthly income? "))
    net_income = total_income - total_expenses
    print("Your net income is " + str(net_income))

    # Calculate number of months or monthly contribution
    s_goal_2 = float(input("What is your savings goal? "))
    quest_2 = int(input("Do you want to find how many months till you reach your goal (1) or your monthly contribution (2)? "))
    
    # Calculate number of months to reach goal
    if quest_2 == 1:
        m_cont_2 = (float(input("What percent of your net income do you want to contribute each month (No percent sign)? ")))/100
        initial_balance = float(input("Current balance of savings account: "))
        months_needed = (s_goal_2-initial_balance)/((m_cont_2*net_income))
        print("If you contribute "+str(m_cont_2*100)+"% of your net monthly income ($"+str(m_cont_2*net_income)+"), you will reach your goal in "+str(months_needed)+" months.")
    
    #Calculate monthly contribution
    elif quest_2 == 2:
        s_time_2 = float(input("How many months till you want to reach your goal? "))
        initial_balance = float(input("Current balance of savings account: "))
        interest = input("Do you want to calculate with interest? (y/n) ")
        print(" ")

        #calculate monthly with compound interest
        if interest == "y":
            i_rate_m = (float(input("What is your annual interest rate (no percent sign)? "))/100.0)/12.0
            contribution_needed = (i_rate_m*(s_goal_2-(initial_balance*((1.0+i_rate_m)**s_time_2))))/(((1.0+i_rate_m)**s_time_2)-1.0)
            print("In order to save "+str(s_goal_2)+" in "+str(s_time_2)+" months with interest, you need to save "+str(contribution_needed)+" per month")
       
        #calculate monthly payments without interest
        elif interest == "n": 
            contribution_needed = (s_goal_2-initial_balance)/s_time_2
            print("In order to save "+str(s_goal_2)+" in "+str(s_time_2)+" months without interest, you need to save "+str(contribution_needed)+" per month")
        if net_income >= contribution_needed:
            print("You have enough net income to save the needed amount each month")
        elif net_income < contribution_needed:
            print("You do not have enough net income to save the needed amount each month")
