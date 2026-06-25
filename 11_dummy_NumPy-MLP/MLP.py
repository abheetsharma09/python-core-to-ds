import numpy

print("Enter the Matrix Dimensions...[Press ENTER to +][q to EXIT]")
dimension_list = [] # 2 3 4 5
while True:
    try:
        inp_dim = input()
        if inp_dim == "q":
            break
        dimension_list.append(int(inp_dim))
    except ValueError as e:
        print("ERROR!!...{e}")

matrix_init = numpy.random.randn(dimension_list[0], dimension_list[1])#base matrix

for i in range(1 ,len(dimension_list)-1):
    current_rows = dimension_list[i]
    current_cols = dimension_list[i + 1]

    current_matrix = numpy.random.randn(current_rows, current_cols) #initialize as loop forward
    result_matrix = numpy.dot(matrix_init, current_matrix)

    result_matrix[result_matrix < 0] = 0 #ReLu
    matrix_init  = result_matrix #update

print(matrix_init)