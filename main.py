from database import create_account, login_user, change_balance

print("--WELCOME TO THE BANK SYSTEM--")


while True:
    print("""
    select an action:
    1. Create account
    2. login
    3. exit
    """)

    #select the option
    option = input("Enter the number: ")

    if option == "1":
        create_account()

    elif option == "2":
        AccountID = login_user()
        if AccountID:
            
            while True:
                print("\nSelect an option: ")
                print("1. logout")
                print("2. deposit or withdraw")

                selection = input("Enter your choice: ") 

                if selection == "1":
                    break
                elif selection == "2":
                    change_balance(AccountID)

    elif option == "3":
        break

   