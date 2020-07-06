#PF-Tryout

account_list=[1001,1002,1003,1004,1005]
balance_list=[2500,10000,7000,1500,500]


def bank(account_number, transaction_type, amount = "0"):
    if transaction_type == "Withdraw":
        withdraw(account_number, amount)
    elif transaction_type == "Deposit":
        deposit(account_number, amount)
    elif transaction_type == "Balance Enquiry":
        balance_enquiry(account_number)
    else:
        print("Invalid Transaction Type")

def withdraw(account_number, amount):
    if account_number in account_list:
        index = account_list.index(account_number)
        balance = balance_list[index]
        new_balance = balance - amount
        if(new_balance >= 500):
            balance_list[index]=new_balance
            print("Transaction completed successfully")
            print("Balance Amount :", new_balance)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Account number")


def deposit(account_number, amount):
    if account_number in account_list:
        index = account_list.index(account_number)
        balance = balance_list[index]
        new_balance = balance + amount
        balance_list[index]=new_balance
        print("Transaction completed successfully")
        print("Balance Amount :", new_balance)
    else:
        print("Invalid Account number")

def balance_enquiry(account_number):
    if account_number in account_list:
        index = account_list.index(account_number)
        balance = balance_list[index]
        print(balance)
    else:
        print("Invalid Account number")
        
bank(1003, "Withdraw", 1000)
