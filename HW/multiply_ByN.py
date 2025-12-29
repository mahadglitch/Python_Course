# Introduction:
# Time complexity: measures how the runtime of an algorithm grows as input grows.
# Space complexity: measures how much memory an algorithm uses as input grows.

# Approach 1: Using 1 iteration (direct multiplication)
def multiply_single_iteration(n, m):
    return n * m

# Approach 2: Using N iterations (repeated addition)
def multiply_n_iterations(n, m):
    result = 0
    for i in range(n):
        result += m  # add m, n times
    return result

# Main program
N = int(input("Enter N: "))
M = int(input("Enter M: "))

# Using single iteration
single_iter_result = multiply_single_iteration(N, M)
print(f"Multiplication using 1 iteration: {single_iter_result}")

# Using N iterations
n_iter_result = multiply_n_iterations(N, M)
print(f"Multiplication using N iterations: {n_iter_result}")
