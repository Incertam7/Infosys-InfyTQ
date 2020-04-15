#DSA Exer-7

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

class Ball:
    def __init__(self, manufacturer, color):
        self.__color = color
        self.__manufacturer = manufacturer
    
    def __str__(self):
        return(self.__color + " " + self.__manufacturer)
    
    def get_color(self):
        return self.__color
    
    def get_manufacturer(self):
        return self.__manufacturer
    
class Box:
    def __init__(self, ball_stack):
        self.ball_stack = ball_stack
        self.manufacturer1_stack = Stack(2) # consider "Penn" to be manufacturer1
        self.manufacturer2_stack = Stack(2) # consider "Wilson" to be manufacturer2

    def group_balls(self):
        while not self.ball_stack.is_empty():
            ball = self.ball_stack.pop()
            if ball.get_manufacturer() == "Penn":
                self.manufacturer1_stack.push(ball)
            elif ball.get_manufacturer() == "Wilson":
                self.manufacturer2_stack.push(ball)
            else:
                print("Manufacturer not found")
                
    def display_ball_details(self, manufacturer):
        if manufacturer == "Penn":
            self.manufacturer1_stack.display()
        elif manufacturer == "Wilson":
            self.manufacturer2_stack.display()
        else:
            print("Manufacturer not found")
    
ball1 = Ball("Penn","Yellow")
ball2 = Ball("Wilson","White")
ball3 = Ball("Penn","Red")
ball4 = Ball("Wilson","Yellow")

ball_stack = Stack(4)
ball_stack.push(ball1)
ball_stack.push(ball2)
ball_stack.push(ball3)
ball_stack.push(ball4)

box = Box(ball_stack)
box.group_balls()
box.display_ball_details("Penn")
