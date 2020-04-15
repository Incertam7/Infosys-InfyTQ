#DSA-Assgn-16

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

def separate_boxes(box_stack):
    temp_queue = Queue(box_stack.get_max_size())
    temp_stack = Stack(box_stack.get_max_size())
    
    primary_colors = ['Red', 'Green', 'Blue']
    
    while not box_stack.is_empty():
        data = box_stack.pop()
        if data in primary_colors:
            temp_stack.push(data)
        else:
            temp_queue.enqueue(data)
            
    while not temp_stack.is_empty():
        box_stack.push(temp_stack.pop())
        
    return temp_queue

#Use different values for stack and test your program
box_stack = Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result = separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()
