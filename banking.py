from database import get_connection

def create_account(name, initial_deposit, pin="0000"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
    "INSERT INTO accounts (name, balance, pin) VALUES (%s, %s, %s)",
    (name, initial_deposit, pin)
)
    conn.commit()
    print(f"Account created for {name} with ${initial_deposit:.2f}")
    cursor.close()
    conn.close()

def deposit(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE id = %s",
        (amount, account_id)
    )
    conn.commit()
    print(f"Deposited ${amount:.2f} into account {account_id}")
    cursor.close()
    conn.close()

def withdraw(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    row = cursor.fetchone()
    if row is None:
        print("Account not found")
    elif row[0] < amount:
        print(f"Insufficient funds. Current balance: ${row[0]:.2f}")
    else:
        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            (amount, account_id)
        )
        conn.commit()
        print(f"Withdrew ${amount:.2f} from account {account_id}")
    cursor.close()
    conn.close()

def check_balance(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, balance FROM accounts WHERE id = %s", (account_id,))
    row = cursor.fetchone()
    if row is None:
        print(" Account not found")
    else:
        print(f" {row[0]}'s balance: ${row[1]:.2f}")
    cursor.close()
    conn.close()

def list_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, balance FROM accounts")
    rows = cursor.fetchall()
    if not rows:
        print("No accounts found.")
    else:
        print("\n--- All Accounts ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Balance: ${row[2]:.2f}")
    cursor.close()
    conn.close()


def login(account_id, pin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, pin FROM accounts WHERE id = %s", (account_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row is None:
        print("Account not found.")
        return False
    if row[1] != pin:
        print("Incorrect PIN.")
        return False
    print(f"Welcome, {row[0]}!")
    return True

def close_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE id = %s", (account_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Account {account_id} closed successfully.")
    else:
        print("Account not found.")
    cursor.close()
    conn.close()

def modify_account(account_id, new_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET name = %s WHERE id = %s", (new_name, account_id))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Account {account_id} modified successfully.")
    else:
        print("Account not found.")
    cursor.close()
    conn.close()


def close_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM accounts WHERE id = %s", (account_id,))
    row = cursor.fetchone()
    if row is None:
        print("Account not found.")
    else:
        cursor.execute("DELETE FROM accounts WHERE id = %s", (account_id,))
        conn.commit()
        print(f"Account for {row[0]} has been closed.")
    cursor.close()
    conn.close()

def modify_account(account_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM accounts WHERE id = %s", (account_id,))
    row = cursor.fetchone()
    if row is None:
        print("Account not found.")
    else:
        cursor.execute("UPDATE accounts SET name = %s WHERE id = %s", (name, account_id))
        conn.commit()
        print(f"Account {account_id} updated to name: {name}")
    cursor.close()
    conn.close()
    


# test
if __name__ == "__main__":
    print("loading some tests...")
    create_account("TestUser", 500.00, "0000")
    print("PASS: create_account")
    deposit(1, 100.00)
    print("PASS: deposit")
    withdraw(1, 200.00)
    print("PASS: withdraw")
    withdraw(1, 99999.00)  # should fail with insufficient funds
    print("All tests complete.")