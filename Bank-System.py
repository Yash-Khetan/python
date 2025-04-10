accounts = {}

def login_user():
    user_name = raw_input("Enter your name: ")
    if user_name not in accounts:
        print("Account not registered")
        return None

    for attempt in range(3):
        password = raw_input("Enter the password: ")
        if accounts[user_name]["password"] == password:
            print("Success!")
            return user_name
        else:
            print("Incorrect password. You have", 2 - attempt, "attempts remaining.")
    print("Too many failed attempts. Access denied.")
    return None


def createaccount():
    print("This is the create account!")
    user_name = raw_input("Enter your name: ")
    password = raw_input("Enter a password: ")
    accounts[user_name] = {
        "password": password,
        "balance": 1000,
        "transactions": []
    }
    print("Account created for", user_name)


def withdraw():
    user_name = login_user()
    if user_name:
        amount = int(raw_input("Enter amount to withdraw: "))
        if accounts[user_name]["balance"] >= amount:
            accounts[user_name]["balance"] -= amount
            print("Amount withdrawn:", amount)
            accounts[user_name]["transactions"].append("Withdrawn " + str(amount))
            print("Current balance:", accounts[user_name]["balance"])
        else:
            print("Not enough balance")


def deposit():
    user_name = login_user()
    if user_name:
        amount = int(raw_input("Enter amount to deposit: "))
        accounts[user_name]["balance"] += amount
        accounts[user_name]["transactions"].append("Deposited " + str(amount))
        print("Updated balance:", accounts[user_name]["balance"])


def checkbalance():
    user_name = login_user()
    if user_name:
        print("Balance is:", accounts[user_name]["balance"])


def printstatement():
    user_name = login_user()
    if user_name:
        print("Transaction History:")
        for entry in accounts[user_name]["transactions"]:
            print("-", entry)

def transfer():
    user_name = login_user()
    if user_name:
        receiver_name = raw_input("Enter the recipient's name: ")

        if receiver_name not in accounts:
            print("Recipient account not found.")
            return

        transfer_amt = int(raw_input("Enter the amount to be transferred: "))
        if transfer_amt > accounts[user_name]["balance"]:
            print("Cannot proceed with transaction: Insufficient funds.")
        else:
            # Deduct from sender
            accounts[user_name]["balance"] -= transfer_amt
            accounts[user_name]["transactions"].append(str(transfer_amt) + " transferred from your account to " + receiver_name)

            # Add to receiver
            accounts[receiver_name]["balance"] += transfer_amt
            accounts[receiver_name]["transactions"].append(str(transfer_amt) + " transferred to your account by " + user_name)

            print("Transfer successful!")
    else:
        print("Invalid credentials")

# Menu Loop
while True:
    print("\n--- Welcome to the Bank ---")
    print("1. Create an account")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Transfer money")
    print("7. Exit")
    choice = int(raw_input("Enter your choice: "))

    if choice == 1:
        createaccount()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        deposit()
    elif choice == 4:
        checkbalance()
    elif choice == 5:
        printstatement()
    elif choice == 6:
        transfer()
    elif choice == 7:
        print("Thank you for using the Bank!")
        break
    else:
        print("Invalid choice.")
