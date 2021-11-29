# Predict Yearly Income

def predict_yearly_income():
    #input monthly income and total monthly expenses for multiple months which is then averaged out to determine the average annual yearly income
    quest_3 = "y"
    months = 0.0
    m_total_income = 0.0
    m_total_expenses = 0.0
    while quest_3 == "y":  
        m_total_income += float(input("What was your total income for this month? "))
        m_total_expenses += float(input("What was your expenses amount for this month? "))
        months += 1.0
        quest_3 = input("Do you have more monthly data to input? y/n ")
    m_average_income = m_total_income/months
    m_average_expenses = m_total_expenses/months
    print("Your average income per month was $"+str(m_average_income)+" and your average monthly expenses were $"+str(m_average_expenses))
    a_average_income = m_average_income*12.0
    a_average_expenses = m_average_expenses*12.0
    print("Your average annual income is $"+str(a_average_income)+" and your average annual expenses are $"+str(a_average_expenses))
