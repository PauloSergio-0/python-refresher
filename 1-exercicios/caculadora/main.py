from service.calculos import Calculos
from numbers import Number

def adcionarNumero(tipoOperacao = ': '):
    while(True):
        numero = input(f"Digite número{tipoOperacao}")
        try:
            if '.' in numero:
                return float(numero)
            else:
                return int(numero)
        except:
            print("Apenas números")

if __name__ == "__main__":
    while(True):
        print("""
        ==Calculadora==
        1. Adição
        2. Subtração
        3. Multiplicação
        4. Divisão
        5. Raiz quadrada
        0. Sair
        """)
        try:
            opcao = int(input("Escolha uma opção: "))
        except Exception as e:
            print("\nOperação não permitida\nDigitar apenas números\n")
            continue
        
        if(opcao == 1):
            Calculos.adicao(adcionarNumero(tipoOperacao="A: "), adcionarNumero(tipoOperacao="B: "))
        elif(opcao == 2):
            Calculos.subtracao(adcionarNumero(tipoOperacao="A: "), adcionarNumero(tipoOperacao="B: "))
        elif(opcao == 3):
            Calculos.multiplicacao(adcionarNumero(tipoOperacao="A:"), adcionarNumero(tipoOperacao="B: "))
        elif(opcao == 4):
            Calculos.divisao(adcionarNumero(tipoOperacao="A: "), adcionarNumero(tipoOperacao="B: "))
        elif(opcao == 5):
            Calculos.raizQuadrada(adcionarNumero())
        elif(opcao == 0):
            print('Saindo...')
            break
        else:
            print("Operação não encontrada")