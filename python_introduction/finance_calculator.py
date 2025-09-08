income_str = input("Enter your monthly income: ")
expenses_str = input("Enter your total monthly expenses: ")

income = float(income_str)
expenses = float(expenses_str)

monthly_savings = income - expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings:g}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:g}.")
