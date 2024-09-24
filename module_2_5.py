
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        string_ = []
        matrix.append(string_)
        for j in range(m):
            string_.append(value)
    return matrix
result = get_matrix(2,2,10)
print(result)