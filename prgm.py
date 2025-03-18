
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


n = int(input("Enter the number of Fibonacci terms you want: "))


print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")
