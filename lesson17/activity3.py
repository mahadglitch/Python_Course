def ONSquareTime(n):
    iteration = 0
    for i in range(0, n):  # rows
        for j in range(0, n):  # columns
            print("*", end=" ")
            iteration += 1
        print("")

    print("\nWhen n is ", n, " Iterations = ", iteration, "\n")


ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")
