class ATM:
    
    balance = 10000

    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return f"Your account balance is ${ATM.balance}"

    def deposit(self, amount):
        if amount > 0:
            ATM.balance += amount
            return f"${amount} has been deposited into your account."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= ATM.balance:
            ATM.balance -= amount
            return f"${amount} has been withdrawn from your account."
        else:
            return "Insufficient balance or invalid withdrawal amount."

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "PIN changed successfully."

# Example usage of the ATM class
if __name__ == "__main__":
    account = ATM("1234567890", "1234")
    
    while True:
        entered_pin = input("Enter your PIN: ")
        
        if account.verify_pin(entered_pin):
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(account.check_balance())
            elif choice == "2":
                amount = int(input("Enter the deposit amount: "))
                print(account.deposit(amount))
            elif choice == "3":
                amount = int(input("Enter the withdrawal amount: "))
                print(account.withdraw(amount))
            elif choice == "4":
                new_pin = input("Enter your new PIN: ")
                print(account.change_pin(new_pin))
            elif choice == "5":
                print("Thank you for using this ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        else:
            print("Incorrect PIN. Please try again.")
