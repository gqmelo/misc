

def rotate_matrix(matrix):
    start_j = 0
    end_j = len(matrix) - 1
    max_i = len(matrix) // 2 - 1
    for i in range(max_i + 1):
        for j in range(start_j, end_j):
            temp = matrix[i][j]
            matrix[i][j] = matrix[end_j - j + start_j][i]
            matrix[end_j - j + start_j][i] = matrix[end_j][end_j - j + start_j]
            matrix[end_j][end_j - j + start_j] = matrix[j][end_j]
            matrix[j][end_j] = temp
        start_j += 1
        end_j -= 1
        if start_j >= end_j:
            break
