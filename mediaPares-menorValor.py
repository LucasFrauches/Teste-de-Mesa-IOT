# exercicio simples que recebe numeros e imprime o menor, além de calcular a média dos Num pares

# Inicializando as variáveis
menor_valor = None
soma_pares = 0
contador_pares = 0
a = None

# entrada
while a < 0:
    a = int(input("Digite um valor inteiro (digite 0 para encerrar): "))
    
#processamento
    if a != 0:
        if menor_valor is None or a < menor_valor:
            menor_valor = a
        
        if a % 2 == 0:
            soma_pares += a
            contador_pares += 1

media_pares = soma_pares / contador_pares if contador_pares > 0 else 0

# saída
print(f"Menor valor: {menor_valor}")
print(f"Média dos valores pares: {media_pares}")
