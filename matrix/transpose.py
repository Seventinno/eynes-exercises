def transpose(matrix):
    fila = len(matrix)
    columnas = len(matrix[0])

    transpuesta = [[0] * fila for i in range(columnas)]
    
    for i in range(fila):
        for j in range(columnas):
            transpuesta[j][i] = matrix[i][j]
    return transpuesta
