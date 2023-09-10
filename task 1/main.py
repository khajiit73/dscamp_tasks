import numpy as np

#Cramer's method
def determinants(a_matrix, b_matrix):
    arr_size = np.size(a_matrix, 1)
    result = np.empty(arr_size)
    for col in range(arr_size):
        a_copy = a_matrix.copy()
        a_copy[:, col] = b_matrix
        result[col] = np.linalg.det(a_copy)
    return result
    
def solve_equation(coeff_matrix: list, const_matrix: list):
    a_matrix = np.array(coeff_matrix)
    b_matrix = np.array(const_matrix)

    det = np.linalg.det(a_matrix)
    if (det == 0):
        print("No solutions")
        return None
    
    return determinants(a_matrix, b_matrix) / det

if __name__ == "__main__":
    example = solve_equation([[1, 2, 3],
                    [0, 1, 2],
                    [2, 0, 0]], 
                    [1, 1, 0])
    print(example)

#[ 0. -1.  1.]