def diamond_star_pattern_optimized(n):
    result = []
    for i in range(1, n + 1):
        result.append(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        result.append(" " * (n - i) + "*" * (2 * i - 1))
    print("\n".join(result))

# Input size of the diamond
size = int(input("Enter the number of rows for the diamond: "))
diamond_star_pattern_optimized(size)