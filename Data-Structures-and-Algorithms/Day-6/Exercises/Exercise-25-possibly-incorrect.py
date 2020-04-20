#DSA-Exer-25

def find_maximum_activities(activity_list, start_time_list, finish_time_list):
    for i in range(0, len(activity_list) - 1):
        swapped = False
        for j in range(0, len(activity_list) - 1 - i):
            if start_time_list[j] > start_time_list[j + 1]:
                temp = start_time_list[j]
                start_time_list[j] = start_time_list[j + 1]
                start_time_list[j + 1] = temp
                
                temp = finish_time_list[j]
                finish_time_list[j] = finish_time_list[j + 1]
                finish_time_list[j + 1] = temp
                
                temp = activity_list[j]
                activity_list[j] = activity_list[j + 1]
                activity_list[j + 1] = temp
                
                swapped = True
        
        if not swapped:
                break
            
    #print(*activity_list, sep = ' : ', end = '\n\n')
    #print(*start_time_list, sep = ' : ')
    #print(*finish_time_list, sep = ' : ')
            
    activities_done = []
    time_right_now = 0
    
    for i in range(0, len(activity_list)):
        if time_right_now <= start_time_list[i]:
            activities_done.append(activity_list[i])
            time_right_now = finish_time_list[i] + 1
        
    return activities_done

#Pass different values to the function and test your program
activity_list = [11, 12, 32, 44, 53, 62]
start_time_list = [12, 14, 21, 31, 16, 18]
finish_time_list = [20, 16, 25, 35, 17, 20]

print("Activities:", activity_list)
print("Start time of the activities:", start_time_list)
print("Finishing time of the activities:", finish_time_list)

result = find_maximum_activities(activity_list, start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:", result)
