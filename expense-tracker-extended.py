# Expense tracker: extended version
# By: Poyi Liu


# Append amount and category to dictionary
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Print fstring of amount and category entered
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Return sum of iterators in expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
# Return the category selected and associated expense value recorded in expenses. Looped. 
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def total_expenses_by_category(expenses, category):
    sum = 0
    converted_category = str(category)
    for expense in expenses:
        if expenses.keys() == category:
            sum += expenses[category]
        
def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Show total expenses by category')
        print('6. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
            
        elif choice == '5':
            category = input('Enter category to filter: ')
            total = (total_expenses_by_category(expenses, category))
            print('\nTotal Expenses for Category:', total)

    
        elif choice == '6':
            print('Exiting the program.')
            break

main()