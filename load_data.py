from banking import create_account
from database import get_connection

def load_dummy_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM accounts")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    if count > 0:
        print("Database already has accounts, skipping dummy data load.")
        return

    with open("test_data.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name = parts[0]
                balance = float(parts[1])
                pin = parts[2]
                create_account(name, balance, pin)
    print("Dummy data loaded successfully.")

if __name__ == "__main__":
    load_dummy_data()