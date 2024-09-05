# Imagine que você está em uma viagem para os Estados Unidos e precisa converter o valor em reais para dólares. Crie um programa que receba o valor em reais e a taxa de câmbio atual, e exiba o valor equivalente em dólares.
v_reais = float(input('Digite o valor em reais '))
t_cambio = float(input('Digite a taxa de câmbio atual '))

conversao = v_reais/t_cambio

print(f'O valor do real em dólares é {conversao}')