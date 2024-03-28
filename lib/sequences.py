def print_fibonacci(n):
    # Initialize the first two numbers of the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    
    # Check if n is 0 or 1 and handle accordingly
    if n == 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    
    # Generate the Fibonacci sequence up to the specified length
    for i in range(2, n):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)
    
    # Print the generated Fibonacci sequence
    print(fibonacci_sequence)
