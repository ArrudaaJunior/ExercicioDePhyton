#Francisco Eudes Arruda Vieira Junior
#Matricula:20171143000017

import random

num_certo = random.randrange(1,50)
jogada = 0

print("Voce tem 6 tentativas para acerta")

while(jogada < 7):

	tentativa = int(input("Digite o numero entre 1 e 50: "))
	if(tentativa < 1 or tentativa >100):
		
		print("Erro seu valor nao estar entre 1 e 50")
		tentativa = int(input("Digite novamente: "))

	certo = tentativa == num_certo
	maior = tentativa > num_certo
	menor = tentativa < num_certo

	if(certo):
		
		print("MUITO BEM VOCE ACERTOU !!!")
		break

	else:
		
		if(maior):
			print("\n Nao foi dessa vez, voce errou! O numero {} foi maior".format(tentativa))

		elif(menor):
			print("\n Nao foi dessa vez, voce errou! O numero {} foi menor".format(tentativa))
	
	jogada= jogada+1
	print("\n Numero de jogada: {} ".format(jogada))

print("O numero certo era {}, Obrigado!".format(num_certo))		