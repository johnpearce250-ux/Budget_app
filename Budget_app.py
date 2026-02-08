class Category():
    def __init__(self, name):                                                   # Initialize the Category class with a name and an empty ledger
        self.name=name
        self.ledger=[]
    
    def deposit(self, amount, description=""):                                  # Add a deposit to the ledger with the specified amount and description
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):                         # Check if there are sufficient funds and add a withdrawal to the ledger if possible
        balance=sum(item["amount"] for item in self.ledger)
        if balance>=amount:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
    def get_balance(self):                                  # Calculate and return the current balance by summing the amounts in the ledger
        total=0
        for item in self.ledger:
            total+=item["amount"]
        return total
    
    def transfer(self, amount, category):               # Attempt to transfer funds from this category to another category by first withdrawing from this category and then depositing into the target category if the withdrawal is successful                                              
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def check_funds(self, amount):                           # Check if the specified amount is less than or equal to the current balance to determine if there are sufficient funds for a withdrawal or transfer
        if amount>self.get_balance():
            return False
        else:
            return True
    
    def __str__(self):          # Create a string representation of the category, including the title, ledger entries, and total balance
        title=f"{self.name:*^30}\n"
        items=""
        for entry in self.ledger:
            amount="{0:.2f}".format(entry["amount"])
            items+=f"{entry['description'][:23]:23}{amount:>7}\n"
        total=f"Total: {self.get_balance():.2f}"
        return title+items+total

def create_spend_chart(categories):          # Generate a bar chart representing the percentage of total spending for each category, formatted as a string
    res="Percentage spent by category\n"
    spent=[]
    names=[]
    for category in categories:
        total=0
        for item in category.ledger:
            if item["amount"]<0:
                total+=-item["amount"]
        spent.append(total)
        names.append(category.name)
    total_spent=sum(spent)
    percentages=[int((x/total_spent)*10)*10 for x in spent]
    for i in range(100, -1, -10):
        res+=f"{i:>3}| "
        for percent in percentages:
            if percent>=i:
                res+="o  "
            else:
                res+="   "
        res+="\n"
    res+="    "+"-"*(len(categories)*3+1)+"\n"
    max_len=max(len(name) for name in names)
    for i in range(max_len):
        res+="     "
        for name in names:
            if i<len(name):
                res+=name[i]+"  "
            else:
                res+="   "
        if i<max_len-1:
            res+="\n"
    return res