#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=("Veg Roll", "Noodles", "Fried Rice", "Soup")
quantity_available=[2,200,3,0]

def place_order(*item_tuple):
    for i in range(0, len(item_tuple)):
        if i % 2 == 0:
            item = item_tuple[i]
            if item in menu:
                index = menu.index(item)
                if check_quantity_available(index, item_tuple[i + 1]):
                    print(item, "is available")
                else:
                    print(item, "stock is over")
            else:
                print(item, "is not available")
        else:
            continue

def check_quantity_available(index, quantity_requested):
    if quantity_requested <= quantity_available[index]:
        quantity_available[index] -= quantity_requested
        return True
    else:
        return False


#Provide different values for items ordered and test your program
place_order("Fried Rice", 2, "Soup", 1)
