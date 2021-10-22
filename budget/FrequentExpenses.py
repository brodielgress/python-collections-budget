from . import Expense

import collections

expenses = Expense.Expenses(data/spending_data.csv)
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
    spending_counter = collections.Counter(spending_categories)
    