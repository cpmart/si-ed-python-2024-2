#2. Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".

n1 = int(input("Informe o 1o: "))
n2 = int(input("Informe o 2o: "))


if not n1%n2 or not n2%n1:
    print("São múltiplos!")
else:
    print("Não são múltiplos!")
    
   
   