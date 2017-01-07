#!/usr/bin/python
'''
Write an algorithm such that if an element in an M*N matrix is 0, its entire row and column are set to 0.
'''

def set_zeros(matrix, n, m):
    row_dict = {}
    column_dict = {}
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row_dict[i] = 1
                column_dict[j] = 1


    for i in range(n):
        for j in range(m):
            if i in row_dict or j in column_dict:
                matrix[i][j] = 0

    print matrix


def main():
    matrix = [[1,0,2,0], [1,1,0,1], [1,1,1,1]]
    set_zeros(matrix, 3, 4)


if __name__ == "__main__":
    main()
