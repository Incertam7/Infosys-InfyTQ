#DSA-Assgn-20

class Item:
    def __init__(self, item_name, author_name, published_year):
        self.__item_name = item_name
        self.__author_name = author_name
        self.__published_year = published_year
        
    def get_item_name(self):
        return self.__item_name
        
    def get_author_name(self):
        return self.__author_name
        
    def get_published_year(self):
        return self.__published_year
        
    def __str__(self):
        return(self.__item_name + " by " + self.__author_name + " published in " + str(self.__published_year))

class Library:
    def __init__(self, item_list):
        self.__item_list = item_list
        
    def get_item_list(self):
        return self.__item_list
        
    def sort_item_list_by_author(self, new_item_list):
        for i in range(0, len(new_item_list) - 1):
            swapped = False
            for j in range(0, len(new_item_list) - 1 - i):
                author1 = new_item_list[j].get_author_name()
                author2 = new_item_list[j + 1].get_author_name()
                if author1 > author2:
                    temp = new_item_list[j]
                    new_item_list[j] = new_item_list[j + 1]
                    new_item_list[j + 1] = temp
                    swapped = True
            if not swapped:
                break

        #Python's in built sorter with complex lambda expressions
        #new_item_list.sort(key = lambda x : ''.join(e for e in x.get_author_name() if e.isalnum()))
        
        return new_item_list
        
    def sort_items_by_published_year(self):
        item_list = self.__item_list
        for i in range(0, len(item_list) - 1):
            swapped = False
            for j in range(0, len(item_list) - i - 1):
                if item_list[j].get_published_year() > item_list[j + 1].get_published_year():
                    temp = item_list[j]
                    item_list[j] = item_list[j + 1]
                    item_list[j + 1] = temp
                    swapped = True
            if not swapped:
                break
        
        for i in range(0, len(item_list) - 1):
            same_year = False
            for j in range(i, len(item_list) - 1):
                if item_list[j].get_published_year() == item_list[j + 1].get_published_year():
                    same_year = True
                else:
                    if same_year:
                        self.sort_item_list_by_author(item_list[i : j])
                    else:
                        break
            
        return item_list
        
    def add_new_items(self, new_item_list):
        self.__item_list += new_item_list
        self.sort_item_list_by_author(self.__item_list)

#Use different values for item and test your program
item1 = Item("A Mission In Kashmir", "Andrew Whitehead", 1995)
item2 = Item("A Passage of India", "E.M.Forster", 2012)
item3 = Item("A new deal for Asia", "Mahathir Mohammad", 1999)
item4 = Item("A Voice of Freedom", "Nayantara Sehgal", 2001)
item5 = Item("A pair of blue eyes", "Thomas Hardy", 1998)

item_list = [item1, item2, item3, item4, item5]
library = Library(item_list)
print("The current items in the library are:")
library_item_list = library.get_item_list()
for item in library_item_list:
    print(item)

item11 = Item("Broken Wing", "Sarojini Naidu", 2012)
item12 = Item("Guide", "R.K.Narayanan", 2001)
item13 = Item("Indian Summers", "John Mathews", 2001)
item14 = Item("Innocent in Death", "J.D.Robb", 2010)
item15 = Item("Life of Pi", "Yann Martel", 2010 )
item16 = Item("Sustainability", "Johny", 2016)
item17 = Item("Look Ahead", "E.M.Freddy", 2012 )

new_item_list = [item11, item12, item13, item14, item15, item16, item17]
print()
print("The new items to be added are:")
for item in new_item_list:
    print(item)

new_item_list_sorted = library.sort_item_list_by_author(new_item_list)
print()
print("The new items after sorting based on the author name are:")
for item in new_item_list_sorted:
    print(item)

library.add_new_items(new_item_list_sorted)
print()
print("The final set of items after adding the new item list are:")
library_item_list = library.get_item_list()
for item in library_item_list:
    print(item)

library.sort_items_by_published_year()
print()
print("The items sorted based on the increasing order of their published year:")
for item in library.get_item_list():
    print(item)
