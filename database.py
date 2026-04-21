import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yard_Slate_98$",  # replace with your actual root password
        database="banking"
    )
    return connection

# Test the connection
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connected to MySQL successfully!")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")