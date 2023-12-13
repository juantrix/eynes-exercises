def transpose(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with the number of columns and rows flipped
    new_matrix = [[0 for x in range(rows)] for y in range(cols)]

    # Iterate through the rows and columns of the original matrix
    for i in range(rows):
        for j in range(cols):
            # Set the value in the new matrix to the value in the original matrix
            new_matrix[j][i] = matrix[i][j]

    return new_matrix
