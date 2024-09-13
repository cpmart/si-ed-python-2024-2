idadeDias = int(input("Digite sua idade: "))
anos = idadeDias//365
meses = idadeDias%365//30
dias = idadeDias%365%30

print(f"{anos}anos, {meses}meses e {dias}dias")
