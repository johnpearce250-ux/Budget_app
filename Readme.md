

# Budget Tracker Application
This Python program provides a robust system for managing multiple budget categories, tracking deposits/withdrawals, and generating visual spending reports. Designed with personal finance management in mind.

## Features
- **Category Management**
  - Create spending categories (e.g., Food, Rent, Entertainment)
  - Track deposits and withdrawals  - Check category balances  - Transfer funds between categories
- **Reporting**
  - Detailed ledger statements  - Visual spending chart  - Percentage-based expenditure analysis
## Class Documentation
### `Category(name)`
Creates a new budget category with:
- `name`: Category title (string)
- `ledger`: Transaction history (list)

#### Methods:
1. **`deposit(amount, description="")`**  
   Adds funds to category  
   *Example: `food.deposit(100, "Groceries")`*

2. **`withdraw(amount, description="")`**  
   Deducts funds if balance permits (returns bool)  
   *Example: `food.withdraw(20, "Restaurant")`*

3. **`get_balance()`**  
   Returns current balance  
   *Example: `print(food.get_balance())`*

4. **`transfer(amount, category)`**  
   Moves funds to another category (returns bool)  
   *Example: `food.transfer(30, rent)`*

5. **`check_funds(amount)`**  
   Returns `True` if amount ≤ balance  
   *Example: `if food.check_funds(50): ...`*

6. **`__str__()`**  
   Returns formatted ledger (auto-aligned columns):  
   ```
   *********Food*********
   Groceries        100.00   Restaurant       -20.00   Transfer to Rent -30.00   Total             50.00   ```

### `create_spend_chart(categories)`
Generates text-based spending visualization:  

```plaintextPercentage spent by category100|          
 90|          
 80| o        
 70| o        
 60| o o      
 50| o o      
 40| o o o    
 30| o o o    
 20| o o o    
 10| o o o o  
  0| o o o o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```


```

## Key Implementation Notes
1. Negative amounts represent withdrawals
2. Transfer transactions show source/destination names
3. Spending chart percentages rounded down to nearest 10%
4. Ledger entries auto-truncated to 23 characters5. Amounts displayed with 2 decimal places
---
Created by John Pearce with freeCodecamp on 2/5/2026

