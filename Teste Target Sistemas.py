'EXERCÍCIO 1 - Sequência de Fibonacci'
number_user = int(input("Digite um número inteiro"))

previous1 = 1
previous2 = 0

for n_element in range(1, number_user + 1, 1):

    current = previous1 + previous2
    previous1 = previous2
    previous2 = current

    if number_user == current:
        print("O número digitado está na sequência de Fibonacci!")
        break

    elif number_user < current:
        print("O número digitado  NÃO está na sequência de Fibonacci!")
        break

'EXERCÍCIO 2 - String'

letra = str(input("Digite a letra que você deseja verificar se existe na palavra!"))

original_string = str(input("Digite uma palavra!"))
lowercase_string = original_string.lower()

number_x = 0

for letter in lowercase_string:
    if letter == letra:
        number_x = number_x + 1

if number_x > 0:
    print("A letra: " + letra + " aparece na palavra " + str(number_x) + " vezes")


else:
    print("A letra: " + letra + " NÃO aparece na palavra")

'EXERCÍCIO 3 - INDICE'

indice = 12
soma = 0
K = 1

while K < indice:
    K = K + 1

soma = soma + K

print(soma)

