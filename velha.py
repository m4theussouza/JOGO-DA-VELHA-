# -*- coding: utf-8 -*-

#cria novo tabuleiro\jogo
def novo_jogo():
	
	space = ' '
	tabuleiro = [
		[space, space, space],
		[space, space, space],
		[space, space, space],
	]
	jogador = 'X'
	return (tabuleiro, jogador)

#imprime tabuleiro
def imprime_tab(tabuleiro): 
	for linha in tabuleiro:
		print('[{a}][{b}][{c}]'.format(a= linha[0],b=linha[1],c=linha[2]))

#verifica se existe espaço para se jogar
def faz_jogada(tabuleiro, coordenadas, jogador):
	(x, y) = coordenadas
	if tabuleiro[x][y] == ' ':
		tabuleiro[x][y] = jogador
		return True
	else:
		print 'Jogue novamente!'
		return False

#recebe jogadas 
def recebe_input(jogador):
	(x, y) = (None, None)
	while x is None and y is None: 
		(x, y) = input('Jogador {j} '.format(j = jogador))
	if x > 2 or x < 0 or y > 2 or y < 0:
		print 'Jogada Invalida'
		return recebe_input(jogador)
	return (x, y)

#verifica se alguem ganhou
def verificar_final_de_jogo(tabuleiro):
	vitoria = 'VITORIA'
	empate = 'EMPATE'
	nada = 'NADA'
	# Vertical e Horizontal
	for i in range(0, 3):
		if tabuleiro[i][i] != ' ':	
			# Horizontal
			if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][0] == tabuleiro[i][2]:
				return vitoria 
			# Vertical
			if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]:
				return vitoria
	if tabuleiro[1][1] != ' ':	
		# Diagonal Principal
		if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]:
			return vitoria
		# Diagonal Secundária
		if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
			return vitoria
	# Se ainda tem jogo
	for i in range(0, 3):
		for j in range(0, 3):
			if tabuleiro[i][j] == ' ':
				return nada
	return empate

#loop de jogo
def game():
	tabuleiro, jogador = novo_jogo()
	imprime_tab(tabuleiro)
	estiver_em_andamento = True	
	while estiver_em_andamento:
		coordenadas = recebe_input(jogador)
		while not faz_jogada(tabuleiro, coordenadas, jogador):
			pass			
		imprime_tab(tabuleiro)
		resposta = verificar_final_de_jogo(tabuleiro)
		if resposta == 'VITORIA':
			print('{} VENCEU !!'.format(jogador))
			estiver_em_andamento = False 
		elif resposta == 'EMPATE':
			print('EMPATOU !!')
			estiver_em_andamento = False
		elif resposta == 'NADA':
			jogador = 'O' if jogador == 'X' else 'X'
	return

if __name__ == '__main__':
	game()
	