def verificar_letra_a(string):
    # Converte a string para minúsculas para contar 'a' e 'A' como iguais
    string_lower = string.lower()

    # Conta a quantidade de vezes que 'a' aparece na string
    quantidade_a = string_lower.count('a')

    # Verifica se a letra 'a' está presente na string
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

# Solicita a entrada da string ao usuário
string = input("Digite uma string: ")
verificar_letra_a(string)
