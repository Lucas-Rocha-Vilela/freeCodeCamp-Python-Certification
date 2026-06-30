from itertools import zip_longest

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        balance = 0.0
        for operations in self.ledger:
            balance += float(operations['amount'])
        return balance

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.name}')
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def __str__(self):
        title = self.name.center(30, '*')
        result = title + '\n'
        for operation in self.ledger:
            result += operation['description'].ljust(23)[:23]
            result += f' {operation["amount"]:.2f}'
            result += '\n'
        result += f'Total: {self.get_balance()}'
        return result

def create_spend_chart(categories):
    spend_chart = 'Percentage spent by category'
    total_spent = 0

    for category in categories:
        for withdrawal in category.ledger:
            if withdrawal['amount'] < 0:
                total_spent += withdrawal['amount']
    
    words = []
    percentage = []
    margin_of_error = 0
    bigger = 0
    i = 0
    for category in categories:
        total_category = 0
        for withdrawal in category.ledger:
            if withdrawal['amount'] < 0:
                total_category += withdrawal['amount']

        percentage.append(10 * round(total_category/total_spent, 10))
        margin_of_error += round(percentage[i], 10)
        new_percentage = percentage[i] - int(percentage[i])
        percentage[i] = int(percentage[i])
        if(max(bigger, new_percentage) == new_percentage):
            bigger = new_percentage
            save = category.name
        i+=1

    i = 0
    for category in categories:
        if(10 - margin_of_error > 0.0000001 and save == category.name):
            percentage[i] += 1
        final_print = (10 - percentage[i])*' ' + (percentage[i] + 1)*'o' + category.name
        words.append(final_print)
        i+=1

    counter = 0
    for letters in zip_longest(*words, fillvalue=" "):
        if (counter <= 10):
            spend_chart += '\n' + ((str(100 - 10*counter) + '| ' +  "  ".join(letters)).rjust(3 + 3*len(categories)) + '  ')
            counter += 1
        else:
            spend_chart += '\n' + ("  ".join(letters).rjust(3 + 3*len(categories))) + '  '
        if counter == 11:
            spend_chart += ('\n    ' + '---'*len(categories) + '-')
            counter += 1
    return spend_chart
        

food = Category('Food')
food.deposit(1000, 'deposit')
#print(food.get_balance())
#print(food.check_funds(1000))
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

clothing = Category('Clothing')
clothing.deposit(500, 'deposit')
clothing.withdraw(100, 'suit')

auto = Category('Auto')
auto.deposit(10000, 'deposit')
auto.withdraw(50, 'maintainance')

categories = [food, clothing, auto]
print(create_spend_chart(categories))
