# iterative
def calculate_fibonacci_series(n):
    a, b = 0, 1
    step_count = 0
    fibonacci_series = []

    for i in range(n):
        step_count += 1
        fibonacci_series.append(a)
        a, b = b, a+b

    return fibonacci_series, step_count

# Input from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Calculate the Fibonacci series and step count
fibonacci_series, step_count = calculate_fibonacci_series(n)

print(f"Fibonacci Series for the first {n} terms: {fibonacci_series}")
print(f"Step count: {step_count}")

# recursive
def recursive_fibonacci(n, step_count):
    if n <= 0:
        return [], step_count
    if n == 1:
        return [0], step_count
    if n == 2:
        return [0, 1], step_count

    step_count += 1
    fib_series, step_count = recursive_fibonacci(n - 1, step_count)
    fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series, step_count

# Input from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate the Fibonacci series and get the step count
fibonacci_series, step_count = recursive_fibonacci(n,0)

print(f"Fibonacci Series for the first {n} terms: {fibonacci_series}")
print(f"Step count: {step_count}")
