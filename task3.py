class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
        else:
            print("Insufficient balance or invalid amount.")
    
    def display_balance(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Name: {self.owner}")
        print(f"Current Balance: ₱{self.balance:.2f}")

account = BankAccount("12345678", "Rod Jette", 1000.0)

account.display_balance()

# Perform transactions
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

# Display final account details
account.display_balance()

