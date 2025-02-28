import re

def safe_calculator(func):
    def wrapper(expression):
        if not re.match(r'^[\d+\-*/().\s]+$', expression):
            raise ValueError("Expression contains invalid characters!")
        return func(expression)
    return wrapper

safe_calculator
def calculate(expression):
    return eval(expression)

def calculator():
    while True:
        expression = input("Enter expression: ").strip()
        if expression.lower() == 'exit':
            print("exiting")
            break
        try:
            result = calculate(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


calculator()
