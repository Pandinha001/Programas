#questão 1 lab9

nome = input("Digite seu primeiro nome: ").strip()
sobrenome = input("Digite seu sobrenome: ").strip()
print(f"Bem-vinda, {nome} {sobrenome}!")

#questão 2

frase = input("Digite a frase: ")
cont = 0
for caractere in frase:
    if caractere == " ":
        cont = cont + 1
print("Espaços em branco:", cont)

#questão 3

nome = input("Digite seu nome: ")
escada = ""
for letra in nome:
    escada = escada + letra
    print(escada)


#questão 4
num = input("Número: ")
if len(num) == 9:
    if num[0] == "9":  
        print(f"Número Completo: {num[:5]}-{num[5:]}")
    else:
        print("Número Incorreto!")
elif len(num) == 8:
    print(f"Número Completo: 9{num[:4]}-{num[4:]}")
else:
    print("Número Incorreto!")

#questão 5
txt = input("Frase: ")
ind = []
qnt = 0
for i, letra in enumerate(txt):
    if letra in "AEIOUaeiou":
        ind.append(i)
        qnt += 1
print(f"Índices: {", ".join(ind)}")
print("Total:",qnt)
