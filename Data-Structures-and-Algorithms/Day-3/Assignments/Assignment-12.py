#DSA-Assgn-12
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
    def __init__(self, color, name):
        self.__color = color
        self.__name = name
        
    def __str__(self):
        return (self.__color + " " + self.__name)
    
    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name
             
class Game:
    def __init__(self, ball_stack):
        self.ball_container = ball_stack
        self.red_balls_container = Stack(2)
        self.green_balls_container = Stack(2)
        self.blue_balls_container = Stack(2)
        self.yellow_balls_container = Stack(2)
        
    def grouping_based_on_color(self):
        balls_list = []
        while not self.ball_container.is_empty():
            ball = self.ball_container.pop()
            if ball.get_color() == "Red":
                self.red_balls_container.push(ball)
            elif ball.get_color() == "Green":
                self.green_balls_container.push(ball)
            elif ball.get_color() == "Blue":
                self.blue_balls_container.push(ball)
            elif ball.get_color() == "Yellow":
                self.yellow_balls_container.push(ball)
            else:
                print("Invalid color")
                
    def rearrange_balls(self, color):
        ball_stack = None
        if color == "Red":
            ball_stack = self.red_balls_container
        elif color == "Green":
            ball_stack = self.green_balls_container
        elif color == "Blue":
            ball_stack = self.blue_balls_container
        elif color == "Yellow":
            ball_stack = self.yellow_balls_container
        else:
            print("Invalid color")
            
        if not ball_stack.is_empty():
            temp_ball1 = ball_stack.pop()
        
            if temp_ball1.get_name() == 'A':
                ball_stack.push(temp_ball1)
            elif temp_ball1.get_name() == 'B':
                temp_ball2 = ball_stack.pop()
                ball_stack.push(temp_ball1)
                ball_stack.push(temp_ball2)
            else:
                print("Invalid ball name")
            
    def display_ball_details(self, color):
        ball_stack = None
        if color == "Red":
            ball_stack = self.red_balls_container
        elif color == "Green":
            ball_stack = self.green_balls_container
        elif color == "Blue":
            ball_stack = self.blue_balls_container
        elif color == "Yellow":
            ball_stack = self.yellow_balls_container
        else:
            print("Invalid color")

        while not ball_stack.is_empty():
            print(ball_stack.pop())
    
#Use different values to test your program
ball1 = Ball("Red","A")
ball2 = Ball("Blue","B")
ball3 = Ball("Yellow","B")
ball4 = Ball("Blue","A")
ball5 = Ball("Yellow","A")
ball6 = Ball("Green","B")
ball7 = Ball("Green","A")
ball8 = Ball("Red","B")
ball_list = Stack(8)
ball_list.push(ball1)  
ball_list.push(ball2) 
ball_list.push(ball3) 
ball_list.push(ball4) 
ball_list.push(ball5) 
ball_list.push(ball6) 
ball_list.push(ball7) 
ball_list.push(ball8)   

game = Game(ball_list)
game.grouping_based_on_color()

game.rearrange_balls("Red")

game.display_ball_details("Red")
game.display_ball_details("Green")
game.display_ball_details("Blue")
game.display_ball_details("Yellow")
