class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data
    
    def get_next(self):
        return self.__next
    
    def set_next(self, next_node):
        self.__next = next_node
    
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self, data):
        new_node = Node(data)
        if(self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
    
    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()
    
    def find_node(self, data):
        if self.__head == None:
            return None
        else:
            temp = self.get_head()
            while temp is not None:
                if temp.get_data() == data:
                    return temp
                elif temp.get_next() is None:
                    return None
                else:
                    temp = temp.get_next()
                    
    def insert(self, data, data_before):
        new_node = Node(data)
        
        if data_before is None:
            new_node.set_next(self.get_head())
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node
        else:
            prev_node = self.find_node(data_before)
            if prev_node is None:
                print("Data not found")
                return
            else:
                new_node.set_next(prev_node.get_next())
                prev_node.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
           msg.append(str(temp.get_data()))
           temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


list1 = LinkedList()
list1.add("Sugar")
list1.add("Teabags")
list1.add("Milk")
list1.add("Biscuits")
#Insert the element in the required position
list1.insert("Eggs", "Sugar")
list1.display()
                                              
