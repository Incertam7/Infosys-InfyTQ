#DSA-Exer-23

def quick_sort(tickets_list, start, end):
    if start >= end:
        return
    pivot = partition(tickets_list, start, end)
    quick_sort(tickets_list, start, pivot - 1)
    quick_sort(tickets_list, pivot + 1, end)
    
def partition(tickets_list, start, end):
    pivot = int(tickets_list[start][1:])
    i = start + 1
    j = end
    done = False
    
    while True:
        while i <= j and int(tickets_list[i][1:]) <= pivot:
            i += 1
        
        while j >= i and int(tickets_list[j][1:]) >= pivot:
            j -= 1
            
        if j < i:
            break
        else:
            swap(tickets_list, i, j)
            
    swap(tickets_list, j, start)
    return j
        
def swap(tickets_list, pos1, pos2):
    temp = tickets_list[pos1]
    tickets_list[pos1] = tickets_list[pos2]
    tickets_list[pos2] = temp

def arrange_tickets(tickets_list):
    quick_sort(tickets_list, 0, len(tickets_list) - 1)
    
    for i in range(0, 10):
        ticket = "T" + str(i + 1)
        if ticket not in tickets_list:
            tickets_list.insert(i, "V")
    
    #print(tickets_list[0 : 10])
    
    j = 0
    for i in range(0, 10):
        if tickets_list[i] == "V":
            tickets_list[i] = tickets_list[j + 10]
            j += 1
            
    #print(tickets_list[0 : 10])
    
    return tickets_list[0 : 10]

tickets_list = ['T20', 'T5', 'T10', 'T1', 'T2', 'T8', 'T16', 'T17', 'T9', 'T4', 'T12', 'T13', 'T18']
print("Ticket ids of all the available students :")
print(tickets_list)
result = arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
