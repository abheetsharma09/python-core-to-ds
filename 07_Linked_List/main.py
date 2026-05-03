#Performing CRUD Operations on Linked 
class Node:
    #Initialize a blank Node
    def __init__(self , value) -> None:
        self.data = value
        self.next_address = None
'''
Condition for empty linked list is self.head node is none...
'''
class Linked_List:
    #Initialize a empty Linked List
    def __init__(self) -> None:
        self.head = None #first Node
        self.n = 0 #number of nodes in LL

    def __len__(self):#returns the length of the LL
        return self.n
    
    #Add node in LL at the first position
    def insert_head(self , value):
        new_node = Node(value)#Create a new node with value given
        new_node.next_address = self.head #insert it at the place of node
        self.n = self.n +1 #increment the no. of nodes by 1
        self.head = new_node #update the before head(self.head) with new head

    def insert_at_last(self , value): #apppend node as the tail of LL
        if not self.head == None: #Check if the LL is empty or not
            new_node = Node(value)#Create a new node with value given
            current = self.head #Stores the current head in a variable
            for i in range(self.n): #loop to all the items in the LL
                if current.next_address == None: #check if the Node is last or not
                    current.next_address = new_node #Default the last node points towards the None but this time it points towards the new node
                    self.n = self.n+1 #increment the node count by 1
                current = current.next_address#it helps keep moving to the next node
        else:
            self.insert_head(value)#If the LL is blank append the item as head.

    def insert_at_index(self,index, value):
        new_node = Node(value)#Create a new node with value given
        current = self.head #Stores the current head in a variable
        count = 0 
        while count != index: #loops till the index
            current = current.next_address #update the head till i reach the index node
            count += 1
        if not current == None: #Check if there something after the list or not
            new_node.next_address = current.next_address #Here the new_node.nextaddress is going equal to the next node of the index 
            current.next_address = new_node #update the current node address with new_node
            self.n = self.n +1
        else:
            print("ERROR!!")

    def insert_after(self,after, value):

        new_node = Node(value)#Create a new node with value given
        current = self.head #Stores the current head in a variable

        while current != None: #loops till the LL ends
            if current.data == after: #if the item found in the LL then breaks
                break
            current = current.next_address #update the head till i reach the index node

        if not current == None: #Check if there something after the list or not
            new_node.next_address = current.next_address #Here the new_node.nextaddress is going equal to the next node to that node 
            current.next_address = new_node #update the current node address with new_node
            self.n = self.n +1
        else:
            print("ERROR!!..Not Found")
        
    def clear(self): #Empty the LL(as default point)
        self.head = None
        self.n =0

    def del_head(self):#It delete the head of the LL
        if self.head ==None: #Check if the LL is empty or not
            print("ERROR!!")
        self.head = self.head.next_address #Change the head to the next Node
        self.n = self.n -1
            
    def del_tail(self):#Delete the tail of the Node
        current = self.head
        if current == None: #If blank LL
            print("ERROR!!...Empty LL")
        if self.n != 1 : #If LL has only 1 item or not
            while current.next_address.next_address != None: #Loops to the second last
                current = current.next_address
            current.next_address = None# Cut the connection between the last node(Tail) to the 2nd last
            self.n = self.n -1

        else:
            self.clear() 
    
    def del_value(self , value):#value as parameter then find and delete that node in which node.data
        current = self.head
        if current == None: #If blank
            print("ERROR!!")
        if self.head.data == value: #If the first value is what we are finding
            self.del_head() #Call the del_head function
        while current.next_address != None: #loops till the last node
            if current.next_address.data == value: #we want to stop 1before the destination
                break
            current = current.next_address #Continue the loop
        current.next_address = current.next_address.next_address #update data with the one before we want tot delete to the next node we want to delete
        self.n = self.n -1 #decrement the self.n
        
    def search(self,value): #Takes a value and return its index position
        current = self.head
        count = 0
        while current != None:
            if current.data == value:
                break
            count += 1
            current = current.next_address
        if current == None:
            print("ERROR!!")
        else:
            print(count)

    def max(self):
        if self.head == None:
            return "ERROR!!"
        gretest_num = 0
        while self.head != None:
            try:
                if self.head.data > gretest_num:
                    gretest_num = self.head.data
            except ValueError as e:
                return f'ERROR!!..{e}'
            self.head = self.head.next_address

        return gretest_num

    def reverse(self):
        prev = None
        current = self.head

        while current != None:
            next_node = current.next_address
            current.next_address = prev
            prev = current
            current = next_node
            
        self.head = prev
        
        
    def __getitem__(self , value): #Takes the [index number] as parameter and returns its value
        current = self.head #Store current node in a variable
        count = 0
        if value >= self.n:
            return "ERROR!"
        while count != value:
            current = current.next_address
            count += 1
        return current.data
            

    def __str__(self):#Returns the nodes in LL as print()
        current = self.head #Store current node in a variable
        result = ''
        while current != None: #Loops till it the Last node of LL
            result = result+ f'{current.data} --> ' #Extract the Node data
            current = current.next_address
        return result[:-4] #returns the result by removing the last 4 letter.
