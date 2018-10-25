# 중첩 for 문
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for x in range(3):
    for y in range(3):
        # print('matrix[', x, '][', y, ']:', matrix[x][y], end =' \t')
        print('matrix[%d][%d]:'%(x,y), matrix[x][y], end = '\t')
    else:
        print("")



        # matrix[0][0]: 1
        # matrix[0][1]: 2
        # matrix[0][2]: 3
        # matrix[1][0]: 4
        # matrix[1][1]: 5
        # matrix[1][2]: 6
        # matrix[2][0]: 7
        # matrix[2][1]: 8
        # matrix[2][2]: 9
