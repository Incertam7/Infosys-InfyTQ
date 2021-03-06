
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



queue = Queue(5)
#Enqueue all the required element(s).
queue.enqueue("Tom")
queue.enqueue("Dick")
queue.enqueue("Harry")
queue.enqueue("Jack")
queue.enqueue("Maria")
queue.enqueue("Leah")
#Display all the elements in the queue.
queue.display()

queue.dequeue()
queue.display()
