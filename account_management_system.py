class BankAccount:
    account_id_counter = 1000  # Starting account number from 1000

    def __init__(self, holder_name):
        self.holder_name = holder_name
        self.account_number = BankAccount.generate_account_number()
        self.balance = 0.0

    @classmethod
    def generate_account_number(cls):
        cls.account_id_counter += 1
        return cls.account_id_counter

    def display_details(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("***Deposit amount must be greater than zero***")
            return
        self.balance += amount
        print(f"Deposited ₹{amount:.2f} successfully.")
        self.display_details()

    def withdraw(self, amount):
        if amount <= 0:
            print("***Withdrawal amount must be greater than zero***")
            return
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        print(f"Withdrew ₹{amount:.2f} successfully!!!")
        self.display_details()

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")

def main_menu():
    accounts = {}

    def create_account():
        name = input("Enter the account holder's name: ")
        account = BankAccount(name)
        accounts[account.account_number] = account
        print("Account created successfully!!!")
        account.display_details()

    def access_account():
        acc_number = int(input("Enter your account number: "))
        if acc_number in accounts:
            return accounts[acc_number]
        else:
            print("Account not found!!!")
            return None

    while True:
        print("\n--- Welcome to the Bank ---")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_account()

        elif choice == '2':
            account = access_account()
            if account:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)

        elif choice == '3':
            account = access_account()
            if account:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)

        elif choice == '4':
            account = access_account()
            if account:
                account.check_balance()

        elif choice == '5':
            print("Thank you for using the bank!!!Exited....")
            break

        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main_menu()
