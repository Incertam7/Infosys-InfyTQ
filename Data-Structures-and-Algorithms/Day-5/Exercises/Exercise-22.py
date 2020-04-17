#DSA-Exer-22

def quick_sort(list1, list2, start, end):
    if start >= end:
        return
    pivot = partition(list1, list2, start, end)
    quick_sort(list1, list2, start, pivot - 1)
    quick_sort(list1, list2, pivot + 1, end)
    
def partition(list1, list2, start, end):
    pivot = list2[start]
    i = start + 1
    j = end
    done = False
    
    while True:
        while i <= j and list2[i] <= pivot:
            i += 1
        
        while j >= i and list2[j] >= pivot:
            j -= 1
            
        if j < i:
            break
        else:
            swap(list1, list2, i, j)
            
    swap(list1, list2, j, start)
    return j
        
def swap(list1, list2, pos1, pos2):
    temp1 = list1[pos1]
    temp2 = list2[pos1]
    
    list1[pos1] = list1[pos2]
    list2[pos1] = list2[pos2]
    
    list1[pos2] = temp1
    list2[pos2] = temp2

def order_heights(student_list, height_list):
    quick_sort(student_list, height_list, 0, len(height_list) - 1)
    return [student_list, height_list]

#Pass different values to the function and test your program
student_list = ["Santa", "Tris", "Arun", "Rachel", "John"]
height_list = [132.7, 129.2, 135, 130.6, 140]
print("Initial student details :")
print("The students:", student_list)
print("Their heights:", height_list)
print()
result = order_heights(student_list, height_list)
print("After arranging the students in the order of their height:")
print("The students:", result[0])
print("Their heights:", result[1])
