print ("Bem - Vindo ao Show do Milhao! ")


inicio = input("Vamos comecar? ")
questoes = 0

if inicio.lower() != "sim":
    print("Saindo do jogo, volte depois! ")
    quit()


print("Ok, Vamos comecar ! ")

#Primeira pergunta
resposta =  input("Quanto é 2 + 2? ")
if resposta == "4":
    print("A resposta esta correta")
    questoes += 1
else:
    print("A resposta esta incorreta")

#Segunda pergunta
resposta = input("Qual o maior time do Brasil? ")
if resposta.lower() == "corinthians":
          print ("Correto! Vamos para proxima pergunta!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")

#Terceira pergunta
resposta = input("Quantos mundiais o palmeiras tem? ")
if resposta.lower() == "0":
          print ("Correto! Vamos para proxima pergunta!")
          questoes += 1
else: 
    print ("Errou Feio! Tente novamente")

#Quarta pergunta
resposta = input("Quanto é 4x4? ")
if resposta.lower() == "16":
          print ("Correto! Vamos para proxima pergunta!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")

#Quinta pergunta
resposta = input("Qual o planeta mais proximo ao sol? ")
if resposta.lower() == "mercurio":
          print ("Correto! Vamos para proxima pergunta!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")


#Sexta pergunta
resposta = input("Goku ou Power Rangers? ")
if resposta.lower() == "goku":
          print ("Correto! Vamos para proxima pergunta!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")


#Setima pergunta
resposta = input("Coca-Cola ou Pepsi? ")
if resposta.lower() == "coca-cola":
          print ("Correto! Vamos para proxima pergunta!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")


#Oitava pergunta
resposta = input("Android ou Apple? ")
if resposta.lower() == "android":
          print ("Correto! Vamos para proxima pergunta!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")


#Nona pergunta
resposta = input("Praia ou Neve? ")
if resposta.lower() == "praia":
          print ("Correto! Vamos para proxima e ultima pergunta!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")


#Decima pergunta
resposta = input("5 + 5? ")
if resposta.lower() == "10":
          print ("Acertou!")
          questoes += 1
else: 
    print ("Incorreto! Tente novamente")


print ("Total de questoes certas é : " + str(questoes))
print ("Voce Acertou " + str((questoes / 10) * 100) + "% MIZERAVI")