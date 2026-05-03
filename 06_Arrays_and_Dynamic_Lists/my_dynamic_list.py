#Dynamic Array Working
import ctypes #A module in pyhton which gives access to c type array to create and modifiy at a lower level

class MyList:
    # construct a basic list with size, no. of items and then create a array
    def __init__(self) -> None:
        self.size = 1 #Size of the Array
        self.n = 0 #Number of items
        self.A = self.__make_array(self.size) #this __make_array function returns a array with size self.size and store it in a Variable A
        
    #Can access this function using len(name of the Obj.) return no. of items[self.n]
    def __len__(self):
        #Here self.n return the no. of item in our list[currently it is 0]
        return self.n
    
    #As we try to append the array, size get fulls...this methods add more boxes in array
    def __resize(self,new_capacity):
        # here it calls the function __make_array but with a new capacity that is needed and sufficient to append more items in array
        B = self.__make_array(new_capacity) #and that new array is stored in B

        self.size = new_capacity #updates the size of the new array
        for i in range(self.n):
            # copy the content of self.A to B
            B[i] = self.A[i]
            # reassing A
        self.A= B
    
    #this method add items in the array and increment self.n by 1
    def append(self, item):
        if self.n == self.size: #this, if statement means that the space is full
            self.__resize(self.size*2) #so here we are going to create more space[2X the space]
            
        self.A[self.n] = item #setting the value in the array at the n'th position
        self.n = self.n+1 #incrementing the value of n

    #Removes the last item from array
    def pop(self):
        if self.n <= 0:
            print("Error!!")
        else:
            self.n = self.n -1

    #restores the array to the initial part means L = []
    def clear(self):
        self.n = 0
        self.size =1

    #find the item in the array one by one if find return its index position
    def find(self,item_query):
        for i in range(self.n):
            if self.A[i] == item_query:
                return i
                break
        else:
            return "Not in List"
        
    #Insert at the place of the {index_query} as {item_query} item
    #It act as same as same as the append function just it append somewhere as user want
    def insert(self, index_query , item_query):
        if self.n == self.size: #if the array is already full it call the resize function
            self.__resize(self.size*2)

            for i in range(self.n , index_query+1): #it runs a reverse loop to change the data [ex. 5 to 4, 4 to 3]
                self.A[i] = self.A[i-1] # 5 to 4
        self.A[index_query] = item_query #finally update that variable
        self.n = self.n +1 #update the n as the item has increased
        

    def __delitem__(self,index_query):
        if index_query >= self.n:
            return "ERROR!!"
        else:
            for i in range(index_query , self.n-1 ): 
                self.A[i] = self.A[i+1] 
            self.n = self.n -1

    #It searches the array for that item if found then call the __delitem__ method that deletes that item with that specific index no.
    def remove(self, del_item):
        for i in range(self.n):
            if self.A[i] == del_item:
                self.__delitem__(i)
        return "ERROR!!"

    def __add__(self , other):
        new_array = MyList() #Created a new object which then creates a array then append items one by one
        for i in range(self.n):
            new_array.append(self.A[i])
        for j in range(other.n):
            new_array.append(other.A[j])
        return new_array
    
    #reverse the array and save it to the orignal one[return nothing]
    def reverse(self): #return None
        new_array = MyList()
        for i in range(self.n, 0 ,-1):
            new_array.append(self.A[i - 1])
        self.A = new_array

    #return the array in list format when someone uses print() object
    def __str__(self):
        print_item = str()
        for i in range(self.n):
            print_item = print_item + str(self.A[i]) + "," + " "
        return f'[{print_item[:-2]}]'
    
    #this method return the item at that index value
    def __getitem__(self,index):
        if index >= self.n or index < 0: #throw error if the given index item doenot exist
            return "INDEX ERROR!!"
        else:
            return self.A[index]

    def __make_array(self,capacity):
        #Create a c type array(referencial,static) with size capacity
        return (capacity*ctypes.py_object)() #returns a array with given size
