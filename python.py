class UserAccount:
    def_init_(self, account_type, balance=0):
       self.account_type account_type
       self.balance = balance 
       self.transaction_history = []
       
       
  def deposit(self, amount):
     if amount > 0:
          self.balance =+ amount 
          self.transaction_history.apppend(f"Deposited: £{amount}")
          else:
            raise ValueError("Deposit amount must be positive")
         def withdraw(self, amount):
          if amount > self.balance:
           raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: £{amount}")
        
 def get_balance(self):
    return self.balance
    
 def get_transaction_history(self):
     return self.transaction_history