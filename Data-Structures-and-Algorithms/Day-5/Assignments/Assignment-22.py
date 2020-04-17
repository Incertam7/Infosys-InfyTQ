#DSA-Assgn-22
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

def merge_stack(stack1, stack2):
    temp_list = []
    merged_stack = Stack(stack1.get_max_size() + stack2.get_max_size())
    
    data1 = stack1.pop()
    data2 = stack2.pop()
    
    while not stack1.is_empty() and not stack2.is_empty():
        if data1 > data2:
            temp_list.append(data1)
            data1 = stack1.pop()
        else:
            temp_list.append(data2)
            data2 = stack2.pop()
            
    while not stack1.is_empty():
        temp_list.append(stack1.pop())
        
    while not stack2.is_empty():
        temp_list.append(stack2.pop())
        
    for i in range(len(temp_list) - 1, -1, -1):
        merged_stack.push(temp_list[i])
        
    return merged_stack

#Pass different values to the function and test your program
stack2 = Stack(3)
stack2.push(9)
stack2.push(11)
stack2.push(15)
  
stack1 = Stack(4)
stack1.push(3)
stack1.push(7)
stack1.push(10)
stack1.push(21)
  
print("The elements in stack1 are:")
stack1.display()
print("The elements in stack2 are:")
stack2.display()
print()
output_stack = merge_stack(stack1, stack2)
print("The elements in the output stack are:")
output_stack.display()
