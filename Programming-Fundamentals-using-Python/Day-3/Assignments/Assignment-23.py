#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount = 0
    
    #Write your logic here
    for gem in reqd_gems:
        if gem in gems_list:
            cost_of_gem = price_list[gems_list.index(gem)]
            qty_of_gem = reqd_quantity[reqd_gems.index(gem)]
            bill_amount += cost_of_gem * qty_of_gem
        else:
            bill_amount = -1
            break
    
    if bill_amount > 30000:
        bill_amount *= 0.95
        
    return bill_amount

#List of gems available in the store
gems_list=["Amber", "Aquamarine", "Opal", "Topaz"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[4316, 1342, 8734, 6421]

#List of gems required by the customer
reqd_gems=["Amber", "Topaz"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[1, 4]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)

'''
reqd_quantity-[1, 4],price_list-[4316, 1342, 8734, 6421],reqd_gems-['Amber', 'Topaz'],gems_list-['Amber', 'Aquamarine', 'Opal', 'Topaz']	
'''

print(bill_amount)
