#questão 01

nome = input("Digite seu primeiro nome: ").strip()
sobrenome = input("Digite seu sobrenome: ").strip()
print(f"Bem-vinda, {nome} {sobrenome}!")

#questão 02

frase = input("Digite a frase: ")
cont = 0
for caractere in frase:
    if caractere == " ":
        cont = cont + 1
print("Espaços em branco:", cont)

#questão 03

nome = input("Digite seu nome: ")
escada = ""
for letra in nome:
    escada = escada + letra
    print(escada)
