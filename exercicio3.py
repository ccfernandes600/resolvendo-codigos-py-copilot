# Prompt the user for two numbers
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Perform the four basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Print the results
print("Adição:", round(addition,2))
print("Subtração:", round(subtraction,2))
print("Multiplicação:", round(multiplication,2))
print("Divisão:", round(division,2))