def repetir_string(string, vezes):
    return string * vezes

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

resultado = repetir_string(string, numero)
print(resultado)