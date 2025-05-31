# Python Math Operators

This repository contains implementations of various useful mathematical operators in Python.

## Features

*   Factorial: Calculates the factorial of a non-negative integer.
*   Fibonacci: Calculates the nth Fibonacci number.
*   Is Prime: Checks if a number is a prime number.
*   GCD: Calculates the Greatest Common Divisor (GCD) of two integers.
*   LCM: Calculates the Least Common Multiple (LCM) of two integers.
*   Is Perfect Square: Checks if a number is a perfect square.

## Installation

To use the functions in this project, you can either:

1.  **Copy and paste:** Copy the contents of `lib/math.py` into your own project.
2.  **Import as a module:** Place `lib/math.py` in a directory within your Python path and import the desired functions:

```python
from lib.math import factorial, is_prime
```

## Usage Example

```python
from math_operators import factorial, fibonacci, gcd

# Calculate the factorial of 6
result = factorial(6)
print(result)  # Output: 720

# Find the 10th Fibonacci number
fib_number = fibonacci(10)
print(fib_number)  # Output: 55

# Calculate the GCD of 96 and 64
greatest_divisor = gcd(96, 64)
print(greatest_divisor)  # Output: 32
```

## Contributing

We welcome contributions to improve and expand this collection of math operators. If you have new functions or find improvements to existing ones, please follow these steps:

1.  Fork the repository.
2.  Create a new branch.
3.  Make your changes, including clear comments and tests (if applicable).
4.  Submit a pull request for review.

## License

This code is released under the MIT License. See the LICENSE file for details.
Current date: 2025-05-31
