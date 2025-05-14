def calculate(operation: str, x: float, y: float) -> float:
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If the operation is invalid or division by zero is attempted.
    """
    operation = operation.lower()

    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    else:
        raise ValueError(f"Invalid operation: {operation}")
