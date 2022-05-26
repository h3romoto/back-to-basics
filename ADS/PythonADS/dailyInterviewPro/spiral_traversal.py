def matrix_spiral_print(matrix):
  first = 0
  last = 0
  rows = len(matrix)
  row_len = len(matrix[0])
  i = 0
  while (i < len(matrix[0])):
    print(matrix[0][i])
    i+=1

  # print all last elements, row[-1]
  j = 1
  while (j < rows-1):
    print(matrix[j][-1])
    j+=1

  # print last row, matrix[-1]
  last_row = len(matrix)-1
  i = -1
  while(i >= -row_len ):
    print(matrix[last_row][i])
    i-=1

  # print all first elements [0] except first row's first element
  first_element = matrix[j][0]
  while (j > 1):
    j-=1
    print(matrix[j][0])

  exit()
  
  # print rest of spiral
  i = 1
  while (j > 0 & j < rows-1):
    if (j%2 == 0):
      while (i > 0 & i < row_len-1):
        print(matrix[j][i])
        i+=1
    if (j%2 == 1):
      while (i > 0 & i < row_len-1):
        print(matrix[j][i])
        i+=1
    j+=1

grid = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12