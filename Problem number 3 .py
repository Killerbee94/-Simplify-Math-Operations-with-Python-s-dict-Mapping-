def arithmetic(a, b, operator):
# Define a dictionary mapping operator names to corresponding functions
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }
    return operations[operator]

# Examples
print(arithmetic(5, 2, "add"))
print(arithmetic(5, 2, "subtract"))
print(arithmetic(5, 2, "multiply"))
print(arithmetic(5, 2, "divide")) 