# This is my ROI calculator.

class ROI_calculator():
    def __init__ (self):
        self.income = {}
        self.expenses = {}
        self.initial_costs = {}
        self.monthly_cash_flow = 0
        self.annual_cash_flow = 0
        self.roi_percent = 0
        # self.monthly_cash_flow
        # self.monthly_flow = self.income - self.expenses
        # self.ROI = (12 * self.monthly_flow)/self.buying_costs

    def addIncome(self):
        while True:

            dictionary_name = "monthly income"

            response = input(f"Please specify a source of {dictionary_name}.")
            if response == 'q':
                print(f'Your current {dictionary_name} consists of the following items: {self.income}')
                return False
            else:
                pass
            self.income[response] = None
            response_2 = input(f"What is the value in USD of {dictionary_name} {response}?")
            if response_2 == 'q':
                print(f'Your current {dictionary_name} consists of the following items: {self.income}')
                return False
            elif response_2.isdecimal() != True:
                print('Please enter the amount in digital form. For example, enter "1000" instead of "one thousand."')
                return
            else:
                pass
            self.income[response] = int(response_2)

    def reviewIncome(self):
        print(f'Your current monthly income consists of the following items: {self.income}')

    def addExpenses(self):
        while True:

            dictionary_name = "monthly expenses"

            response = input(f"Please specify a source of {dictionary_name}.")
            if response == 'q':
                print(f'Your current {dictionary_name} consist of the following items: {self.expenses}')
                return False
            else:
                pass
            self.expenses[response] = None
            response_2 = input(f"What is the value in USD of {dictionary_name} {response}?")
            if response_2 == 'q':
                print(f'Your current {dictionary_name} consist of the following items: {self.expenses}')
                return False
            elif response_2.isdecimal() != True:
                print('Please enter the amount in digital form. For example, enter "1000" instead of "one thousand."')
                return
            else:
                pass
            self.expenses[response] = int(response_2)

    def reviewExpenses(self):
        print(f'Your current monthly expenses consist of the following items: {self.income}')
    
    def showMonthlyCashFlow(self):
        self.monthly_cash_flow = sum(self.income.values()) - sum(self.expenses.values())
        print(f"Your monthly cash flow for this property is {self.monthly_cash_flow}.")

    def showAnnualCashFlow(self): 
        self.annual_cash_flow = 12 * (sum(self.income.values()) - sum(self.expenses.values()))
        print(f"Your annual cash flow for this property is {self.annual_cash_flow}.")

    def addInitialCosts(self):
        while True:

            dictionary_name = "up-front property costs"

            response = input(f"Please specify one of your {dictionary_name}.")
            if response == 'q':
                print(f'Your current {dictionary_name} consist of the following items: {self.initial_costs}')
                return False
            else:
                pass
            self.initial_costs[response] = None
            response_2 = input(f"What is the value in USD of {dictionary_name} {response}?")
            if response_2 == 'q':
                print(f'Your {dictionary_name} consist of the following items: {self.initial_costs}')
                return False
            elif response_2.isdecimal() != True:
                print('Please enter the amount in digital form. For example, enter "1000" instead of "one thousand."')
                return
            else:
                pass
            self.initial_costs[response] = int(response_2)

    def showRoi(self):
        if sum(self.initial_costs.values()) == 0 or sum(self.income.values()) == 0 or sum(self.expenses.values()) ==0:
            return print("Please enter your monthly income, monthly expenses, and initial costs for the property before calculating annual Return on Investment.")
        else:
            ROI_calculator.showMonthlyCashFlow(self)
            ROI_calculator.showAnnualCashFlow(self)
            self.roi_percent = self.annual_cash_flow / sum(self.initial_costs.values()) * 100
            print(f"Your calculated annual Return on Investment for this property is {self.roi_percent}%")


prospect_property = ROI_calculator()

def run():
    while True:
        response = (input("Welcome to ROI calculator. Select an option. '1' to add income, '2' to add expenses, '3' to show monthly cashflow, '4' to add up-front costs, '5' to show annual Return on Investment, 'q' to quit."))
        
        if response == '1':
            prospect_property.addIncome()
        if response == '2':
            prospect_property.addExpenses()
        if response == '3':
            prospect_property.showMonthlyCashFlow()
        if response == '4':
            prospect_property.addInitialCosts()
        if response == '5':
            prospect_property.showRoi()
        if response == 'q':
            break

run()


# def run():
#     while True:
#         prospect_property.addIncome()