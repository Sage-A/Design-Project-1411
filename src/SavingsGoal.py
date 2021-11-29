# Savings Goal

# Fincancial planner for design project 2 in 1411
import math

# savings goal
def savings_goal():
    choice1 = 0
    # Set variables given by human
    s_goal = input("What is your savings goal? ") #decimals accepted
    m_cont = input("What is your monthly contribution? ") #decimals accepted
    s_time = input("What is your timeframe? ") #in months

    # set solving variables to 0
    savings = 0.0 
    contributions = 0.0
    timeframe = 0.0

    # Assign choice1 a value to decide what variable is being solved for
    # solve for whatever variable is set to ?
    if "?" in s_goal: 
        choice1 = 1
        m_cont = float(m_cont)
        s_time =float(s_time)
    elif "?" in m_cont:
        choice1 = 2
        s_goal = float(s_goal)
        s_time = float(s_time)
    elif "?" in s_time:
        choice1 = 3
        s_goal = float(s_goal)
        m_cont = float(m_cont)
    else:
        return print("Please only enter two parameters") #return an error if all 3 parameters are given
    
    # Solve for given variable
    # after solving, print sentence with variables included
    if choice1 == 1:
        print("Calculating how much savings you will after after timeframe given monthly contribution")
        savings = m_cont*s_time
        print ("If you contribute "+str(m_cont)+" per month, after "+str(s_time)+" months you will have " +str(savings))
    elif choice1 == 2:
        print("Calculating monthly contribution to reach savings goal in time frame")
        contributions = s_goal/s_time
        print("In order to save "+str(s_goal)+" in "+str(s_time)+ " months, you should contribute "+str(contributions)+" per month.")
    elif choice1 == 3:
        print("Calculating timeframe to reach savings goal given monthly contributions")
        timeframe = math.ceil(s_goal/m_cont)
        yearly_timeframe = timeframe/12
        print("You will reach your savings goal in " + str(timeframe) + " months or " + str(yearly_timeframe) + " years.")

# Print whitespace and begin savings goal function
print (" ")
print (" ")
print (" ")
print (" ")
savings_goal()
