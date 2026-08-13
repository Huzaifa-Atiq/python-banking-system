import sqlite3
import hashlib
connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        accountId INTEGER PRIMARY KEY,
        name TEXT,
        balance REAL,
        password TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transactionId INTEGER PRIMARY KEY,
        accountId INTEGER,
        type TEXT CHECK(type IN ('deposit', 'withdrawal')),
        amount REAL
    )
""")

connect.commit()

def create_account():
    while True:
        username = input("Create your username: ")

        cursor.execute(
            "SELECT * FROM accounts WHERE name = ?",
            (username,)
        )

        result = cursor.fetchone()

        if result is None:
            break

        print("Username already exists!")

    password = input("Create your password: ")


    hashed = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("""
    INSERT INTO ACCOUNTS (name, balance, password)
    VALUES(?, ?, ?)
    """, (username, 0, hashed))

    connect.commit()

    print("Account successfully created!")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute(
        "SELECT * FROM accounts WHERE name = ? AND password = ?",
        (username,hashed)
    )

    result = cursor.fetchone()

    if result:
        print("Login successful!")
        return result[0]   # accountId
    else:
        print("Wrong username/password")
        return None

def change_balance(account_id):
    opt = ""

    while not (opt == "d" or opt == "w"):
        opt = input("Type 'w' for withdrawal and 'd' for deposit: ").lower()

    amount = float(input("Enter the amount: "))

    if opt == "d":
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE accountId = ?",
            (amount, account_id)
        )

        cursor.execute(
            "INSERT INTO transactions (accountId, type, amount) VALUES (?, ?, ?)",
            (account_id, "deposit", amount)
        )

    elif opt == "w":
        cursor.execute(
            "SELECT balance FROM accounts WHERE accountId = ?",
            (account_id,)
        )

        balance = cursor.fetchone()[0]

        if amount > balance:
            print("Insufficient balance.")
            return

        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE accountId = ?",
            (amount, account_id)
        )

        cursor.execute(
            "INSERT INTO transactions (accountId, type, amount) VALUES (?, ?, ?)",
            (account_id, "withdrawal", amount)
        )

    connect.commit()
    print("Transaction successful!")





