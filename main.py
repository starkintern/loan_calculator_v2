if __name__ == '__main__':

    _loan_list = []

    usr_input = input("Would you like to enter a loan?")

    def loan(principal, interest_rate, period, num_periods):
        principal = principal
        interest_rate = interest_rate
        period = period
        num_periods = num_periods

    while "no" not in usr_input.lower():
        usr_principal = int(input("Please enter your total loan amount: "))
        usr_interest_rate = float(input("Please enter your loan interest rate as a percentage: "))
        usr_period_input = (input("Please enter your interest period frequency per year (365, 12, 6, 1): "))
        usr_num_periods = (input("Please enter how many years you have accrued interest for: "))

        _loan_list.append(loan(usr_principal, usr_interest_rate, usr_period_input, usr_num_periods))

        match usr_period_input.lower:
            case "day" | "days" | "365":
                usr_period_input = 365
            case "month" | "months" | "12":
                usr_period_input = 12
            case "semi-annually" | "bi-annually" | "6":
                usr_period_input = 6
            case "year" | "years" | "1":
                usr_period_input = 1

        usr_input = input("Would you like to enter another loan? ")

    def loan_interest(interest_rate, period, num_periods, principal):
        return ((1 + (interest_rate / period)) ** (
                period * num_periods) * principal) - principal

    def loan_total(_loan_list):
        total = 0
        for loans in _loan_list:
            total += ((loans.principal * loans.interest_rate) * loans.period * loans.num_periods) \
                     + loans.principal
        return total

    def monthly_budget(income, expenses):
        income = int(input("Please enter your monthly income: "))
        expenses = int(input("Please enter your monthly expenses: "))
        monthly_budget1 = income - expenses

        return monthly_budget1
