from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("=== Automated Teller Machine ===")
name = input("Enter Name to register: ")
pin = input("Enter Pin: ")
balance = 0
print(name)
print(str(balance))
print("Login")
while True:
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter Pin: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login successful")
        break
    else:
        print("Invalid credentials!")
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance()
    elif option == "2":
        balance = account.deposit(balance)
        print("Current Balance: $" + str(balance))
    elif option == "3":
        balance = account.withdraw(balance)
        print("Current Balance: $" + str(balance))
    else:
        account.logout(name)
        break
