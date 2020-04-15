#DSA-Assgn-13
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

def change_smallest_value(number_stack):
    temp_stack = Stack(number_stack.get_max_size())
    small = None
    count = 0
    
    while not number_stack.is_empty():
        data = number_stack.pop()
        
        if small is None:
            small = data
            count = 1
        elif small > data:
            small = data
            count = 1
        elif small == data:
            count += 1

        temp_stack.push(data)
    
    print(small, "is the smallest and occurs", count, "times")
    
    while count > 0:
        number_stack.push(small)
        count -= 1
        
    while not temp_stack.is_empty():
        data = temp_stack.pop()
        if data == small:
            pass
        else:
            number_stack.push(data)
    
    return number_stack   

#Add different values to the stack and test your program
number_stack = Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()
                                                    
