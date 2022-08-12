
import random

#Iniciando Loop do Jogo

while True:
    jogador = input("\nMake your choice: \n1 - Rock[r] \n2 - Paper[p]\n3 - Scissor[s]\n")

    #Trantando Dados do Input

    jogador = jogador.lower()

    if jogador == 'r' or jogador == 'p' or jogador == 's' or jogador == '1' or jogador == '2' or jogador == '3':
        computador = random.choice(['Rock','Paper','Scissor'])

        if jogador == 'r' or jogador == '1':
            jogador = 'Rock'
        elif jogador == 'p' or jogador == '2':
            jogador = 'Paper'
        elif jogador == 's' or jogador == '3':
            jogador = 'Scissor'

        #Decidindo Empate/Ganhador/Perdedor

        if jogador == computador:
            print (f"Draw! You and Computer chose {jogador}")
        elif (jogador == 'Rock' and computador == 'Scissor') or (jogador == 'Scissor' and computador == 'Paper') or (jogador == 'Paper' and computador == 'Rock'):
            print (f"You Win! You chose {jogador} and Computer chose {computador}")
        elif (computador == 'Rock' and jogador == 'Scissor') or (computador == 'Scissor' and jogador == 'Paper') or (computador == 'Paper' and jogador == 'Rock'):
            print (f"You Lose! You chose {jogador} and Computer chose {computador}")
        else:
            print("Ops! Anything went wrong")
    else:
        print("Try Again!")
    
    #Reinicia ou Finaliza o Jogo

    try_again = input("\nWanna play again? (Y/N)\n")
    try_again = try_again.upper()

    if try_again == 'Y':
        pass
    else:
        break
