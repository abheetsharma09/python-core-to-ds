#CLI based Matrices Calculator
class Matrix:
    #CLASS CONSTRUCTOR
    def __init__(self , rows ,coloumns) -> None:
        #Defines the Structure of a matrix
        self.rows = rows
        self.coloumns = coloumns
        #Basic Blank List Structure
        self.structure = []
        #Calling the constructor method
        self.__matrices_constructor()

    #MATRIX CONSTRUCTOR
    def __matrices_constructor(self): 
        count = 1
        #Creating the Matrix based on the No. of Rows
        for A in range(self.rows):
            self.structure.append([])
        for j in self.structure:
            for k in range(self.coloumns):
                y = int(input(f'Enter value for {k+1} Row and {count} Coloumn = '))
                self.structure[k].append(y)
            count += 1
        print(f'Value Assinged Sucessfully for {self.rows} X {self.coloumns} Matrix {self.structure}')
       
    #HANDLE IF PRINT STATEMENT
    def __str__(self):
        return(str(self.structure))
    
    #ADDS TWO MATRICES
    def __add__(first_mat , sec_mat):
        new_matrix = []
        if len(first_mat.structure) == len(sec_mat.structure):
            for i in range(len(first_mat.structure)):
                new_matrix.append([])
                for j in range(len(sec_mat.structure)):
                    new_matrix[i].append(first_mat.structure[i][j] + sec_mat.structure[i][j])

            return(new_matrix)
        else:
            print("Can't Add")
    
    #SUBTRACTING TWO MATRICES
    def __sub__(first_mat,sec_mat):
        new_matrix = []
        if len(first_mat.structure) == len(sec_mat.structure):
            for i in range(len(first_mat.structure)):
                new_matrix.append([])
                for j in range(len(sec_mat.structure)):
                    new_matrix[i].append(first_mat.structure[i][j] - sec_mat.structure[i][j])
                    
            return(new_matrix)
        else:
            print("Can't Subtract")
            
    #DIVIDE TWO MATRICES
    def __truediv__(first_mat,sec_mat):
        new_matrix = []
        if len(first_mat.structure) == len(sec_mat.structure):
            for i in range(len(first_mat.structure)):
                new_matrix.append([])
                for j in range(len(sec_mat.structure)):
                    new_matrix[i].append(first_mat.structure[i][j] / sec_mat.structure[i][j])
                    
            return(new_matrix)
        else:
            print("Can't Divide")
    

# User interaction
user_row_inp = int(input("Enter...How many rows are in? ")) #m
user_col_inp = int(input("Enter...How many coloumns are in? ")) #n
print("-" * 50)
print(f'Matrices is Created for {user_row_inp} X {user_col_inp}...NOW Start Putting Value..')
print("-" * 50)

#Creating the Matrix
mat1 = Matrix(user_row_inp,user_col_inp)
mat2 = Matrix(user_row_inp,user_col_inp)

print("-" * 50)
user_operation_inp = input(f'What performance you want to Perform for {user_row_inp} X {user_col_inp} Matrix??[+ , - ,/]')
print("-" * 50)

# Call the Classes and Methods
if user_row_inp <= 0 and user_col_inp <= 0:
    print("Please Enter a Valid Number")
else:
    if type(user_operation_inp) == str and user_operation_inp == "+":
        print(mat1+mat2)
    elif type(user_operation_inp) == str and user_operation_inp == "-":
        print(mat1-mat2)
    elif type(user_operation_inp) == str and user_operation_inp == "/":
        print(mat1/mat2)
    else:
        print("Choose a Valid Operations")
