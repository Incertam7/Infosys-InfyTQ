#PF-Assgn-20

def calculate_loan(account_number, salary, account_balance, loan_type, loan_amount_expected, customer_emi_expected):
    eligible_loan_amount = 0
    bank_emi_expected = 0
    eligible_loan_amount = 0
    
    eligible = False
    
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected
    if account_number > 999 and account_number < 2000:
        if account_balance >= 100000:
            if salary > 25000 and loan_type == 'Car':
                if loan_amount_expected <= 500000 and customer_emi_expected <= 36:
                    eligible_loan_amount = 500000
                    bank_emi_expected = 36
                    eligible = True
                else:
                    print("The customer is not eligible for the loan")
            
            elif salary > 50000 and loan_type == 'House':
                if loan_amount_expected <= 6000000 and customer_emi_expected <= 60:
                    eligible_loan_amount = 6000000
                    bank_emi_expected = 60
                    eligible = True
                else:
                    print("The customer is not eligible for the loan")
            
            elif salary > 75000 and loan_type == 'Business':
                if loan_amount_expected <= 7500000 and customer_emi_expected <= 84:
                    eligible_loan_amount = 7500000
                    bank_emi_expected = 84
                    eligible = True
                else:
                    print("The customer is not eligible for the loan")
            
            else:
                print("Invalid loan type or salary")
                
        else:
            print("Insufficient account balance")
                
    else:
        print("Invalid account number")
        
    
    if eligible:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)

calculate_loan(
    account_number = 1005,
    salary = 55000,
    account_balance = 255000,
    loan_type = "House",
    loan_amount_expected = 5500000,
    customer_emi_expected = 60)
