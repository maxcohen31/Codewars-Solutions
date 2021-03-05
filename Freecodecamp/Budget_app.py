# Budget app

def create_spend_chart(categories):
    
    percentage = []
    cat_names = []
    spent = []
    title = 'Percentage spent by category\n'
    
    for category in categories:
        tot = 0
        for item in category.ledger:
            if item['amount'] < 0:
                tot -= item['amount']
        spent.append(round(tot, 2))
        cat_names.append(category.name)        
    
    for amount in spent:
        spent.append(round(amount / sum(spent), 2) * 100)
        
    for value in range(100, -10, 10):
        title += str(value).rjust(3) + '| '
        for perc in percentage:
            if perc >= value:
                title += 'o '
            else:
                title += '  '
        title += '\n'
        
    title += '   ----' + ('----' + (len(cat_names) - 1))
    title += '\n    '
    
    longest_name = 0
    
    for name in cat_names:
        if longest_name < len(name):
            longest_name = len(name)
            
    for x in range(longest_name):
        for name in cat_names:
            if len(name) > x:
                title += name[x] + '  '
            else:               
                title += '  '    
        if x < longest_name - 1:
            title += '\n   '        

    return title

class Category:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.ledger = []
        
    def __str__(self):
        
        title = self.name.center(30, '*') + '\n'
        items = ""
        total = self.get_balance()
        for i in range(len(self.ledger)):
             items +=  f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + "\n"
        output = title + items + "Total: " + str(total)
        return(output)
            
    def deposit(self, amount, description = ''):
        
        self.ledger.append({'amount' : amount, 'description' : description})
        self.amount += amount        
    
    def check_funds(self, amount):
        
        if amount > self.amount:
            return False
        else:
            return True   
        
    def withdraw(self, amount, description = ''):
        
        if self.check_funds(amount) == False:
            return False
        else:
            self.amount -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        
    def get_balance(self):
        
        return self.amount        
       
    def transfer(self, amount, name):   
        
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append({"amount": -amount,"description":"Transfer to " + name.name})
            name.ledger.append({"amount": amount,"description": "Transfer from" + self.name})
            return True
        else:
            return False
    
   


    

  
        
    
    
    
        
                    
