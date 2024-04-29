nome = "Junior"
idade = 28
altura = 1.76
peso = 99
imc = peso / (altura ** 2)
imc < 18.5 + "Abaixo do peso"
18.5 <= IMC < 25: Peso normal
25 <= IMC < 30: Acima do peso
IMC >= 30: Obesidade

print(imc )
print(nome + " tem " + str(idade) + " anos e seu IMC é " + str(imc))

