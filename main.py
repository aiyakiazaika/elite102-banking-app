from load_data import load_dummy_data
from banking import create_account, deposit, withdraw, check_balance, list_accounts, login, close_account, modify_account
ADMIN_PIN = "admin123"

def user_menu(account_id):
    while True:
        print("\n--- User Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            check_balance(account_id)
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            deposit(account_id, amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            withdraw(account_id, amount)
        elif choice == "4":
            print("Logged out")
            break
        else:
            print("Invalid choice")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Open Account")
        print("2. Close Account")
        print("3. Modify Account")
        print("4. List All Accounts")
        print("5. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial deposit: "))
            pin = input("Set PIN for account: ")
            create_account(name, balance, pin)
        elif choice == "2":
            account_id = int(input("Enter account ID to close: "))
            close_account(account_id)
        elif choice == "3":
            account_id = int(input("Enter account ID to modify: "))
            name = input("Enter new name: ")
            modify_account(account_id, name)
        elif choice == "4":
           list_accounts()
        elif choice == "5":
            print("Logged out")
            break
        else:
            print("Invalid choice")

def main():
    load_dummy_data()
        
    while True:
        print("\n============================")
        print("   Welcome to Aiya Bank")
        print("============================")
        print("1. Login as User")
        print("2. Login as Admin")
        print("3. Exit")
        print("============================")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            account_id = int(input("Enter account ID: "))
            pin = input("Enter PIN: ")
            if login(account_id, pin):
                user_menu(account_id)
        elif choice == "2":
            pin = input("Enter admin PIN: ")
            if pin == ADMIN_PIN:
                print("Welcome, Admin!")
                admin_menu()
            else:
                print("Incorrect admin PIN")
        elif choice == "3":
            print("goodbye!")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()