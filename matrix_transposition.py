"""
You're given 2D array of integers, matrix. Write a function that returns the transpose of the matrix.
The transpose of a matrix is a flipped version of the original matrix accross its main diagonal (which runs
from top-left to bottom-right); it switches the row and column indices of the original matrix.
You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

Test 1: {
  "matrix": [
    [1]
  ]
}
Output: [1]

Test 2: {
  "matrix": [
    [1],
    [-1]
  ]
}
Output: [1,-1]

Test 3: {
  "matrix": [
    [1, 2, 3]
  ]
}
Output: [
  [1],
  [2],
  [3]
]

Test 4: {
  "matrix": [
    [1],
    [2],
    [3]
  ]
}
Output: [
  [1, 2, 3]
]

Test 5: {
  "matrix": [
    [1, 2, 3],
    [4, 5, 6]
  ]
}
Output: [
  [1, 4],
  [2, 5],
  [3, 6]
]

Test 6: {
  "matrix": [
    [0, 0, 0],
    [1, 1, 1]
  ]
}
Output: [
  [0, 1],
  [0, 1],
  [0, 1]
]

Test 7: {
  "matrix": [
    [0, 1],
    [0, 1],
    [0, 1]
  ]
}
Output: [
  [0, 0, 0],
  [1, 1, 1]
]

Test 8: {
  "matrix": [
    [0, 0, 0],
    [0, 0, 0]
  ]
}
Output: [
  [0, 0],
  [0, 0],
  [0, 0]
]

Test 9: {
  "matrix": [
    [1, 4],
    [2, 5],
    [3, 6]
  ]
}
Output: [
  [1, 2, 3],
  [4, 5, 6]
]

Test 10: {
  "matrix": [
    [-7, -7],
    [100, 12],
    [-33, 17]
  ]
}
Output: [
  [-7, 100, -33],
  [-7, 12, 17]
]

Test 11: {
  "matrix": [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
}
Output: [
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]

Test 12: {
  "matrix": [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
  ]
}
Output: [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Test 13: {
  "matrix": [
    [5, 6, 3, -3, 12],
    [-3, 6, 5, 2, -1],
    [0, 0, 3, 12, 3]
  ]
}
Output: [
  [5, -3, 0],
  [6, 6, 0],
  [3, 5, 3],
  [-3, 2, 12],
  [12, -1, 3]
]

Test 14: {
  "matrix": [
    [0, -1, -2, -3],
    [4, 5, 6, 7],
    [2, 3, -2, -3],
    [42, 100, 30, -42]
  ]
}
Output: [
  [0, 4, 2, 42],
  [-1, 5, 3, 100],
  [-2, 6, -2, 30],
  [-3, 7, -3, -42]
]

Test 15: {
  "matrix": [
    [1234, 6935, 4205],
    [-23459, 314159, 0],
    [100, 3, 987654]
  ]
}
Output: [
  [1234, -23459, 100],
  [6935, 314159, 3],
  [4205, 0, 987654]
]
"""
#solution 1

def transposeMatrix(matrix):
    transposed_matrix=[]
    for i in range(len(matrix[0])):
        the_vector=[]
        for j in range(len(matrix)):
            the_vector.append(matrix[j][i])
        transposed_matrix.append(the_vector)
    return transposed_matrix

#solution 2
def transposeMatrix(matrix):
  transposed_matrix=[]
  transposed_matrix=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
  return transposed_matrix