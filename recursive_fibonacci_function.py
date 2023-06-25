fibonacci_cache={}

def fibonacci(n):
    if (n in fibonacci_cache): return fibonacci_cache[n]

    if n==1:
        val=1
    elif n == 2:
        val=1
    elif n > 2:
        val = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = val

    return val

# Example usage
for x in range(1,10):
    print(f"input {x}, ouput {fibonacci(x)}")