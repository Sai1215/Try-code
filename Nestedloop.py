a_mat = [[10, 20, 10],
         [4, 5, 6],
         [2, 3, 5]]

b_mat = [[3, 2, 4],
         [3, 3, 9],
         [4, 4, 2]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for row in range(3):
    for col in range(3):
        sum_of_element = 0
        for k in range(3):  
            sum_of_element += a_mat[row][k] * b_mat[k][col]
        result[row][col] = sum_of_element
print("Multiplication:")
for row in result:
    print(row)
    
a_mat = [[10, 20, 10],
         [4, 5, 6],
         [2, 3, 5]]

b_mat = [[3, 2, 4],
         [3, 3, 9],
         [4, 4, 2]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for row in range(3):
    for col in range(3):
        result[row][col] = a_mat[row][col]+b_mat[row][col]

print("Addtion:")
for row in result:
    print(row)