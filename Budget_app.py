class Category():
    def __init__(self, name):
        self.name=name
        self.ledger=[]
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        balance=sum(item["amount"] for item in self.ledger)
        if balance>=amount:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
    def get_balance(self):
        total=0
        for item in self.ledger:
            total+=item["amount"]
        return total
    
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount>self.get_balance():
            return False
        else:
            return True
    
    def __str__(self):
        title=f"{self.name:*^30}\n"
        items=""
        for entry in self.ledger:
            amount="{0:.2f}".format(entry["amount"])
            items+=f"{entry['description'][:23]:23}{amount:>7}\n"
        total=f"Total: {self.get_balance():.2f}"
        return title+items+total

def create_spend_chart(categories):
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