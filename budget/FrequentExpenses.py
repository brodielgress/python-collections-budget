from . import Expense

import collections

expenses.read_expenses(data/spending_data.csv) = Expense.Expenses() 

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
    spending_counter = collections.Counter(spending_categories)
