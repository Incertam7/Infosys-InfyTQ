#DSA-Assgn-21
class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0
        
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if (self.__rear + 1) >= self.get_max_size():
            return True
        else:
            return False
    
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data
    
    def is_empty(self):
        if self.__front > self.__rear:
            return True
        else:
            return False
            
    def dequeue(self, print_dequeued_element = False):
        if self.is_empty():
            print("Queue is empty")
        else:
            data = self.__elements[self.__front]
            if print_dequeued_element:
                print(data, "has been dequeued")
            self.__front += 1
            return data
    
    def display(self):
        index = self.__front
        while index <= self.__rear:
            print(self.__elements[index], end=" ")
            index += 1
        print()

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while(index <= self.__rear):
            msg.append(str(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg

class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if (self.__top + 1) >= self.get_max_size():
            return True
        else:
            return False

    def push(self, data):
        if self.is_full():
            print("Stack is full")
        else:
            self.__top += 1
            self.__elements[self.__top] = data
            
    def is_empty(self):
        if self.__top == -1:
            return True
        else:
            return False
            
    def pop(self, print_popped_element = False):
        if self.is_empty():
            print("Stack is empty")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            if print_popped_element:
                print(data, "has been popped")
            return data
            
    def display(self):
        index = self.__top
        while index > -1:
            print(self.__elements[index], end = " ")
            index -= 1
        print()
                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while index >= 0:
            msg.append(str(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg

#Global variables
flight_details = ["AI890:BAN:MUM:1400", "AI678:BAN:LON:1200", "AI345:BAN:CAN:1410", "AF780:BAN:AGF:1340", "AI001:BAN:AUS:1500", "AI404:BAN:NY:1220"]
 
passenger_details_dict = {"LW101":["Amanda","AI678","C7",25],\
"LW103":["John","AI345","A2",10],\
"LW107":["Alex","AI678","G5",12],\
"TW700":["Hary","AF780","D2",26],\
"LW167":["Kate","AI001","G3",25],\
"LT890":["Wade","AI404","G3",25],\
"TW677":["Preet","AF780","D3",25],\
"LA106":["Henry","AI001","B5",25.5],\
"LA104":["Ajay","AI001","A7",23],\
"LW202":["Amy","AI345","C3",24.5],\
"LT673":["Susan","AI404","J8",5],\
"TW709":["Tris","AF780","H5",22.5],\
"LA188":["Cameron","AI890","H4",22],\
"LA902":["Scofield","AI678","G4",23],\
"TW767":["Pom","AF780","H4",2],\
"LW787":["Burrows","AI890","B4",29],\
"LW898":["Sara","AI678","E4",14],\
"LW104":["Williams","AI890","C4",10] }

def find_flights(flight_time):
    ready_flights = []
    for flight in flight_details:
        flight_detail = flight.split(":")
        if flight_time <= int(flight_detail[3]) <= (flight_time + 200):
            ready_flights.append(flight)
    return ready_flights

def sort_flight_list(flight_list):
    for i in range(0, len(flight_list) - 1):
        swapped = False
        for j in range(0, len(flight_list) - 1 - i):
            flight_detail1 = flight_list[j].split(":")[3]
            flight_detail2 = flight_list[j + 1].split(":")[3]
            if flight_detail1 > flight_detail2:
                temp = flight_list[j]
                flight_list[j] = flight_list[j + 1]
                flight_list[j + 1] = temp
                swapped = True
        if not swapped:
            break
    return flight_list

def get_passenger_details(flight_detail):
    pnr_list = []
    for key, value in passenger_details_dict.items():
        if value[1] == flight_detail.split(":")[0]:
            pnr_list.append(key)
    return pnr_list

def security_check(passenger_pnr_list):
    cleared_passengers = []
    for passenger in passenger_pnr_list:
        if 0 <= passenger_details_dict[passenger][3] <= 25:
            cleared_passengers.append(passenger)
    return cleared_passengers

def sort_passengers(passenger_pnr_list):
    for i in range(0, len(passenger_pnr_list) - 1):
        swapped = False
        for j in range(0, len(passenger_pnr_list) - 1 - i):
            passenger1 = passenger_details_dict[passenger_pnr_list[j]]
            passenger2 = passenger_details_dict[passenger_pnr_list[j + 1]]
            if passenger1[2] > passenger2[2]:
                temp = passenger_pnr_list[j]
                passenger_pnr_list[j] = passenger_pnr_list[j + 1]
                passenger_pnr_list[j + 1] = temp
                swapped = True
        if not swapped:
            break
    return passenger_pnr_list

def boarding(passenger_pnr_list):
    passenger_queue = Queue(len(passenger_pnr_list))
    for passenger in passenger_pnr_list:
        passenger_queue.enqueue(passenger)
    return passenger_queue

def seating(passenger_queue):
    passenger_stack = Stack(passenger_queue.get_max_size())
    while not passenger_queue.is_empty():
        passenger_stack.push(passenger_queue.dequeue())
    return passenger_stack

print("The flight details:")
print(flight_details)
print()
print("The passenger details at the airport:")
print(passenger_details_dict)
print()
time = 1130
print("Details of the flight between the timings", time, "and", time + 200, "are:")
flight_list = find_flights(time)
flight_list = sort_flight_list(flight_list)
print(flight_list)
print()
print("Details of the passengers boarding the flights between the timings", time, "and", (time + 200), "are:")
print()
for i in range(0, len(flight_list)):
    flight_data = flight_list[i].split(':')
    flight_name = flight_data[0]
    
    passenger_pnr_list = get_passenger_details(flight_list[i])
    print("PNR details of the passengers boarding the flight", flight_name, ":")
    print(passenger_pnr_list)
    
    print()
    updated_passenger_pnr_list = security_check(passenger_pnr_list)
    print("PNR details of the passengers of flight", flight_name, "whose baggage has been cleared:")
    print(updated_passenger_pnr_list)
    
    sorted_passenger_pnr_list = sort_passengers(updated_passenger_pnr_list)
    print("PNR details of the passengers of flight", flight_name, "sorted based on seating number:")
    print(sorted_passenger_pnr_list)
    
    print()
    print("The PNR details of the passengers at the queue", flight_name, ":")
    passenger_queue = boarding(updated_passenger_pnr_list)
    passenger_queue.display()
    
    print()
    seating_stack = seating(passenger_queue)
    print("The PNR details of the passengers in the flight", flight_name, ":")
    seating_stack.display()