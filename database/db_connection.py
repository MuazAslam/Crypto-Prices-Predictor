import pyodbc
import datetime

# Database connection setup
def get_db_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-ISD8BJH;"
            "DATABASE=StockPredictor;"
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        print("Database Connection Error:", e)
        return None
    
def authenticate_user(email, password):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "SELECT User_ID, User_Name FROM Users WHERE User_Email = ? AND User_Password = ?"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        conn.close()
        return user
    return None

def register_user(name, email, phone, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT User_Email FROM Users WHERE User_Email=?",email)
        existing_user=cursor.fetchone()
        if existing_user:
            return 'User_Exist'
        else:
            cursor.execute("""INSERT INTO Users (User_Name, User_Email,User_Phone,User_Password) VALUES (?, ?, ?, ?)""", (name, email, phone, password))
            return True
    except Exception as e:
        conn.rollback()
        return False
    finally:
        conn.commit()
        conn.close()

def recent_stock(user_id,symbol,Price_Date,open_price,close_price,high_price,low_price,volume):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Crypto_ID FROM Cryptocurrencies WHERE Symbol = ? ",(symbol,))
        crypto_id=cursor.fetchone()[0]
        #Insert into Recent
        Price_Date=Price_Date.date()
        cursor.execute("""INSERT INTO Recent_Stocks (Crypto_ID, Price_Date, Open_Price, Close_Price, High_Price, Low_Price, Volume) VALUES (?, ?, ?, ?, ?, ?, ?)""", (crypto_id,Price_Date,open_price,close_price,high_price,low_price,volume))
        conn.commit()
        cursor.execute("SELECT @@IDENTITY")
        recent_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO User_Recent_Views (User_ID, Recent_ID) VALUES (?, ?)",(user_id,recent_id))
    except Exception as e:
        conn.rollback()
        print(e)
        return False
    finally:
        conn.commit()
        conn.close()

def get_user_recent_stocks(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT TOP 12
                c.Symbol,
                r.Price_Date,
                r.Open_Price,
                r.Close_Price,
                r.High_Price,
                r.Low_Price,
                r.Volume,
                ur.Viewed_At
            FROM User_Recent_Views ur
            JOIN Recent_Stocks r ON ur.Recent_ID = r.Recent_ID
            JOIN Cryptocurrencies c ON r.Crypto_ID = c.Crypto_ID
            WHERE ur.User_ID = ?
            ORDER BY ur.Viewed_At DESC;
        """
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error fetching recent stocks:", e)
        return []
    finally:
        conn.close()

def get_stocks():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT TOP 31* FROM Cryptocurrencies")
    stocks=cursor.fetchall()
    conn.close()
    return stocks
