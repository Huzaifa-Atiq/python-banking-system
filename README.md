# Python Banking System 🏦

A small **command-line banking system** built with Python and SQLite. This project was made as a simple logic-focused project to practice Python while also learning how to work with SQL databases.

## Features

* Create a bank account
* Automatically generate an account ID
* Prevent duplicate usernames
* Login using username and password
* Password hashing using SHA-256
* Deposit money
* Withdraw money
* Prevent withdrawals when the account has insufficient funds
* Store deposits and withdrawals as transactions
* Persist account data using SQLite

## Technologies Used

* **Python 3**
* **SQLite** — database for storing accounts and transactions
* **`sqlite3`** — Python's built-in SQLite module
* **`hashlib`** — used to SHA-256 hash passwords

No external Python packages are required.

## Project Structure

```text
.
├── main.py
├── database.py
├── .gitignore
└── bank.db
```

### `main.py`

Handles the **main command-line interface**.

It provides the user with options to:

* Create an account
* Login
* Logout
* Deposit or withdraw money
* Exit the program

### `database.py`

Handles the database and the banking logic.

It:

* Creates the SQLite database and tables
* Creates accounts
* Checks whether usernames already exist
* Handles user login
* Hashes passwords
* Updates account balances
* Records transactions

### `bank.db`

This is the SQLite database file containing the account and transaction data.

> `bank.db` is generated automatically and should **not be uploaded to GitHub** because it contains user data.

## Database Structure

The project uses two tables.

### `accounts`

| Column      | Type    | Description             |
| ----------- | ------- | ----------------------- |
| `accountId` | INTEGER | Unique account ID       |
| `name`      | TEXT    | Username                |
| `balance`   | REAL    | Current account balance |
| `password`  | TEXT    | SHA-256 password hash   |

### `transactions`

| Column          | Type    | Description                             |
| --------------- | ------- | --------------------------------------- |
| `transactionId` | INTEGER | Unique transaction ID                   |
| `accountId`     | INTEGER | Account associated with the transaction |
| `type`          | TEXT    | `deposit` or `withdrawal`               |
| `amount`        | REAL    | Amount involved in the transaction      |

## Passwords

Passwords aren't stored directly in the database.

When a user creates an account, their password is hashed using SHA-256:

```python
hashed = hashlib.sha256(password.encode()).hexdigest()
```

The hash is stored instead of the original password.

During login, the entered password is hashed again and compared with the stored hash.

> This is suitable for this learning project. A real banking application should use a password-specific hashing algorithm such as Argon2 or bcrypt instead of plain SHA-256.

## How to Run

### 1. Install Python

Make sure **Python 3** is installed on your computer.

You can check with:

```bash
python --version
```

### 2. Clone/download the project

Put the project files into the same folder:

```text
main.py
database.py
```

### 3. Initialize the database

**You must execute `database.py` first.**

Run:

```bash
python database.py
```

This creates `bank.db` and initializes the:

```text
accounts
transactions
```

tables.

You don't need to run `database.py` every time after that. Once the database has been initialized, you can run the main program.

### 4. Start the banking system

Run:

```bash
python main.py
```

You'll see:

```text
--WELCOME TO THE BANK SYSTEM--

select an action:
1. Create account
2. login
3. exit
```

Create an account, log in, and then you can deposit or withdraw money.

## Important

This is a **learning project**, not an actual banking application. It doesn't implement the security, validation, encryption, authentication protections, or financial safeguards required for a real banking system.

---

### Project Goal

The main purpose of this project is to practice:

* Python functions
* Loops and conditionals
* User input
* SQL queries
* SQLite databases
* CRUD-style database operations
* Password hashing
* Passing data between Python functions/files
* Basic program structure
