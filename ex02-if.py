# Entre com a temperatura
# Se for menor que 20, imprima frio
# Se for maior igual a 20 e menor que 30, imprima agradável
# Se for mario igual a 30, imprima quente 
temperatura = float(input("Digite a temperatura"))

if temperatura < 20:
    print("Frio")
elif temperatura < 30:
    print("Agradável")
else:
    print("Quente")
    
