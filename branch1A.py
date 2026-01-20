"""
Branch1A Python file
"""

def function_a():
    """Simple function in branch1A"""
    print("This is branch1A.py")
    return "Hello from branch1A"

def calculate_sum(numbers):
    """Calculate sum of a list of numbers"""
    return sum(numbers)

if __name__ == "__main__":
    print(function_a())
    result = calculate_sum([1, 2, 3, 4, 5])
    print(f"Sum: {result}")
