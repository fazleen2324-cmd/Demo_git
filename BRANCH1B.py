"""
BRANCH1B Python file
"""

def function_b():
    """Simple function in BRANCH1B"""
    print("This is BRANCH1B.py")
    return "Hello from BRANCH1B"

def calculate_product(numbers):
    """Calculate product of a list of numbers"""
    product = 1
    for num in numbers:
        product *= num
    return product

if __name__ == "__main__":
    print(function_b())
    result = calculate_product([2, 3, 4])
    print(f"Product: {result}")
