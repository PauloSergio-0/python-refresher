nome = None
idade = 0
altura = 0.0

nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))
altura = float(input("Qual a sua altura: "))

if(idade >= 18):
    print(f"\nSeu nome é {nome}\nSua idade é {idade}\nSua altura é {altura}\nVocê é maior de idade")
else:
       print(f"\nSeu nome é {nome}\nSua idade é {idade}\nSua altura é {altura}\nVocê é menor de idade")