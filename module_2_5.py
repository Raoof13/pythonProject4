
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        string_ = []
        if m <= 0:
            continue
        matrix.append(string_)
        for j in range(m):
            string_.append(value)
    return matrix
result1 = get_matrix(0,3,7)
result2 = get_matrix(2,0,42)
result3 = get_matrix(4,2,0)
print(result1)
print(result2)
print(result3)