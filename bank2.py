import hashlib

class Bank:
    def __init__(self):
        self.accounts = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def account_creation(self):
        account_no = int(input("Enter Your Account Number: "))
        account_holder_name = input("Enter Account Holder Name: ")
        account_balance = int(input("Balance: "))
        user_name = input("Set a username for login: ")
        password = input("Set a password for login: ")

        self.accounts[account_no] = {
            "account number": account_no,
            "name": account_holder_name,
            "balance": account_balance,
            "username": user_name,
            "password": self.hash_password(password)
        }
        print("Account Created")

    def user_login(self):
        usr_name = input("Enter your username: ")
        usr_password = input("Enter your password: ")
        hashed_password = self.hash_password(usr_password)

        for account_no, user_details in self.accounts.items():
            if user_details["username"] == usr_name and user_details["password"] == hashed_password:
                print("Successful Login")
                return account_no
        print("Invalid username or password")
        return None

    def deposit(self, account_no):
        amount = int(input("Enter the amount you want to deposit: "))
        self.accounts[account_no]["balance"] += amount
        print("Deposited Successfully")

    def withdraw(self, account_no):
        withdraw = int(input("Enter the amount for withdrawal: "))
        if self.accounts[account_no]["balance"] >= withdraw:
            self.accounts[account_no]["balance"] -= withdraw
            print(f"Your account is debited {withdraw} successfully.")
        else:
            print("Insufficient balance")

    def check_balance(self, account_no):
        print(f"Your current balance is: {self.accounts[account_no]['balance']}")

bank = Bank()

while True:
    print("\n1. Account Creation\n2. Login\n3. Exit")
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        bank.account_creation()
    elif choice == 2:
        account_no = bank.user_login()
        if account_no:
            while True:
                print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                log_choice = int(input("Enter your choice: "))
                if log_choice == 1:
                    bank.deposit(account_no)
                elif log_choice == 2:
                    bank.withdraw(account_no)
                elif log_choice == 3:
                    bank.check_balance(account_no)
                elif log_choice == 4:
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice, try again.")
    elif choice == 3:
        print("Exiting the application.")
        break
    else:
        print("Invalid choice, try again.")
