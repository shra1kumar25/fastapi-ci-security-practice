import ast
import os

password = os.getenv("APP_PASSWORD")

if not password:
    raise ValueError("APP_PASSWORD is not configured")

user_input = input("Enter a Python literal: ")

result = ast.literal_eval(user_input)

print(result)
