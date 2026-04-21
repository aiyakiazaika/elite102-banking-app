from database import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            balance DECIMAL(10, 2) NOT NULL,
            pin VARCHAR(10) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()