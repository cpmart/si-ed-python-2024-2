#7. Escrever um algoritmo que lê um conjunto de 4 valores i, a, b, c, onde i é um valor inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva. A seguir: 

#a) Se i=1 escrever os três valores a, b, c em ordem crescente. 
#b) Se i=2 escrever os três valores a, b, c em ordem decrescente. 
#c) Se i=3 escrever os três valores a, b, c de forma que o maior entre a, b, c fique dentre os dois.

print("[1] escrever os três valores a, b, c em ordem crescente.")
print("[2] escrever os três valores a, b, c em ordem decrescente.")
print("[3] escrever os três valores a, b, c - maior no meio.")
i = int(input("Escolha uma opção: "))
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

if i == 1:
    if a <= b <= c:
        print(f"{a} - {b} - {c}")
    elif a<=b and a<=c and c<=b:
        print(f"{a} - {c} - {b}")
    elif b<=a and b<=c and a<=c:
        print(f"{b} - {a} - {c}")
    elif b<=a and b<=c and c<=a:
        print(f"{b} - {c} - {a}")
    elif c<=a and c<=b and a<=b:
        print(f"{c} - {a} - {b}")
    else:
        print(f"{c} - {b} - {a}")
elif i == 2:
    if a>=b and a>=c and b>=c:
        print(f"{a} - {b} - {c}")
    elif a>=b and a>=c and c>=b:
        print(f"{a} - {c} - {b}")
    elif b>=a and b>=c and a>=c:
        print(f"{b} - {a} - {c}")
    elif b>=a and b>=c and c>=a:
        print(f"{b} - {c} - {a}")
    elif c>=a and c>=b and a>=b:
        print(f"{c} - {a} - {b}")
    else:
        print(f"{c} - {b} - {a}")

elif i == 3:
    if a>=b and a>=c and b>=c:
        print(f"{b} - {a} - {c}")
    elif a>=b and a>=c and c>=b:
        print(f"{c} - {a} - {b}")
    elif b>=a and b>=c and a>=c:
        print(f"{a} - {b} - {c}")
    elif b>=a and b>=c and c>=a:
        print(f"{c} - {b} - {a}")
    elif c>=a and c>=b and a>=b:
        print(f"{a} - {c} - {b}")
    else:
        print(f"{b} - {c} - {a}")

else:
    print("Opção inválida!!!")