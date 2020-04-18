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
    merged_stack = Stack(stack1.get_max_size() + stack2.get_max_size())
    merged_list = []
    while not stack1.is_empty():
        merged_list.append(stack1.pop())
    while not stack2.is_empty():
        merged_list.append(stack2.pop())
    merged_list.sort()
    for num in merged_list:
        merged_stack.push(num)
    return merged_stack

#Pass different values to the function and test your program
stack2 = Stack(3)
stack2.push(8)
stack2.push(11)
#stack2.push(101)
  
stack1 = Stack(4)
stack1.push(4)
stack1.push(18)
stack1.push(33)
#stack1.push(67)
  
print("The elements in stack1 are:")
stack1.display()
print("The elements in stack2 are:")
stack2.display()
print()
output_stack = merge_stack(stack1, stack2)
print("The elements in the output stack are:")
output_stack.display()
