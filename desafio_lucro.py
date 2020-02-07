acoes = [] # Armazena todos os valores de ações, na sequência dos dias
maior_lucro = 0 # Armazena o maior lucro possível
dia_compra = 0 # Armazena o dia de compra que gera o maior lucro possível
dia_venda = 0 # Armazena o dia de venda que gera o maior lucro possível
valor_compra = 0 # Armazena o valor de compra que gera o maior lucro possível
valor_venda = 0 # Armazena o dia de venda que gera o maior lucro possível
dia = 1 # Especifica a qual dia corresponde o valor inserido pelo usuário

print("Bem-vindo à calculadora de lucros de ações!\n")

# Inserção de dados
while True:
	valor = input(f'Insira o valor da ação do {dia}º dia ou digite "p" se quiser parar: ')
	if valor == 'p' or valor == 'P':
		break
	else:
		try:
			acoes.append(float(valor))
			dia += 1
		except ValueError:
			print('Opção inválida.')

# Análise de dados
print("\nAs ações registradas são: ")
for i, acao_compra in enumerate(acoes[0:], start = 1):
	print(f"{i}º Dia: {acao_compra}")
	for j, acao_venda in enumerate(acoes[i:], start = i + 1):
		if acao_venda - acao_compra > maior_lucro:
			maior_lucro = acao_venda - acao_compra
			dia_compra = i
			dia_venda = j
			valor_compra = acao_compra
			valor_venda = acao_venda

# Resposta
if maior_lucro > 0:
	print(f'\nO maior lucro será obtido se forem compradas ações no {dia_compra}º dia, pelo valor {valor_compra}, e vendidas no {dia_venda}º dia, pelo valor {valor_venda}, gerando um lucro de {maior_lucro}.')
else:
	print('\nNão há operações que gerem lucro no período estipulado.')
