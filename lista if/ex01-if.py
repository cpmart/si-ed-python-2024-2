n1 = int(input("Digite o 1o: "))
n2 = int(input("Digite o 2o: "))
n3 = int(input("Digite o 3o: "))

quem = "n1"
maior = n1
if(n2 > maior):
    quem = "n2"
    maior = n2
if(n3 > maior):
    quem = "n3"
    maior = n3

print("O maior é o ",quem," - ",maior)