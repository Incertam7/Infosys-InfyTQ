#PF-Assgn-16
def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    five_needed = int(rupees_to_make / 5)
    if(five_needed > no_of_five):
        five_needed = no_of_five
    
    one_needed = rupees_to_make - (five_needed * 5)
    if(one_needed > no_of_one):
        one_needed = no_of_one

    if(five_needed * 5 + one_needed < rupees_to_make):
        print(-1)
    else:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(57, 8, 5)
