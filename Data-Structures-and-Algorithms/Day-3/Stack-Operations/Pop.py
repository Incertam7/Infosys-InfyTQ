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

stack = Stack(5)
#Push all the required element(s).
stack.push("Shirt1")
stack.display()
stack.push("Shirt2")
stack.display()
stack.push("Shirt3")
stack.display()
stack.push("Shirt4")
stack.display()
stack.push("Shirt5")
stack.display()
stack.push("Shirt6")
stack.display()

stack.pop()
stack.pop()
stack.display()
