# -*- coding: utf-8 -*-
# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(matrix):
    print len(matrix)
    transpose_matrix = []
    column_list = []
    for i in range(len(matrix)):
        for row_list in matrix:
            column_list.append(row_list[i])
        transpose_matrix.append(column_list)
        column_list = []
    #print transpose_matrix
#判断每一行每一列是否都只有一个值
    #参考行选择第一行
    #先判断第一行是否有重复的元素
    for i in range(len(matrix)):
        j = i + 1
        if matrix[0][i] not in range(1,len(matrix)+1):
            return False
        while j < len(matrix):
            if matrix[0][j] == matrix[0][i]:
                return False
            j = j + 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[0][i] not in matrix[j] or matrix[0][i] not in transpose_matrix[j]:
                return False
    return True
#还可以采用一种遍历所有行和列的方法，如果某个数字在某一行或者一列个数不等于一，说明不是数独



    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


