

def zero_matrix(matrix):
    rows_to_zero = set()
    columns_to_zero = set()

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                rows_to_zero.add(i)
                columns_to_zero.add(j)

    for i in rows_to_zero:
        row = matrix[i]
        for j in range(len(row)):
            row[j] = 0

    for j in columns_to_zero:
        for i in range(len(matrix)):
            matrix[i][j] = 0
