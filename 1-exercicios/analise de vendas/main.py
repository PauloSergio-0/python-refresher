vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "quantidade": 2, "preco": 3500},
    {"produto": "Mouse", "categoria": "Periféricos", "quantidade": 10, "preco": 80},
    {"produto": "Teclado", "categoria": "Periféricos", "quantidade": 5, "preco": 150},
    {"produto": "Monitor", "categoria": "Eletrônicos", "quantidade": 3, "preco": 1200},
    {"produto": "Notebook", "categoria": "Eletrônicos", "quantidade": 1, "preco": 3500},
    {"produto": "Mouse", "categoria": "Periféricos", "quantidade": 15, "preco": 80},
    {"produto": "Headset", "categoria": "Periféricos", "quantidade": 4, "preco": 250},
]


def faturamento(individual=False):
    if individual == False:
        faturamento = 0
        for item in vendas:
            faturamento += (item['quantidade'] * item['preco'])
            
        
        print(f"Faturamento Total: R$ {round(float(faturamento),2)}")
    else:
        faturamentoIndividual = 0
        for item in vendas:
                faturamentoIndividual += (item['quantidade'] * item['preco'])
                    
                
                print(f"Produto: {item["produto"]} Faturamento: {faturamentoIndividual}")

def quantidade():
    qtd = 0
    for item in vendas:
        qtd += item['quantidade']
    
    print(f"Quantide de itens vendidos: {qtd}")


def produtoMaisVendido():

    maisVendido = sorted(vendas,key= lambda v: v["quantidade"], reverse=True)
    
    print(f"Produto mais vendido: {maisVendido[0]["produto"]}")
    
def produtoMaiorFaturamento():
    maiorFaturamento = sorted(vendas,key= lambda v: (v["quantidade"] * v["preco"]), reverse=True)
    
    print(f"Maior faturamento por produto: {maiorFaturamento[0]["quantidade"] * maiorFaturamento[0]["preco"]}")
    
def cincoVendas():
    for i in vendas:
        if i["quantidade"]>5:
            print(i)

def faturamentoCategoria(opcao = 1):
    categoria = []

    for i in vendas:
        
        encontrada = False
        for c in categoria:
            
            if i["categoria"] == c["categoria"]:
                c["faturamento"] += (i['quantidade'] * i['preco'])
                encontrada = True
                break
                
        if not encontrada:
            categoria.append({"categoria": i["categoria"], "faturamento": (i['quantidade'] * i['preco'])})
                
    if opcao == 1:
        for item in categoria:
            print(f"Categoria: {item['categoria']} Faturamento: {item["faturamento"]}")
            
    elif opcao == 2: # todas as categorias em listra
        print(sorted(faturamentoCategoria(False), key= lambda c : c["faturamento"], reverse=True)[0])

def percentualCategoria():
    percentual = faturamentoCategoria(1)
    
    faturamentoTotal = 0
    
    for p in percentual:
        faturamentoTotal += p["faturamento"]
    
    for p in percentual:
        print(f"Categoria: {p["categoria"]} Faturamento: {p["faturamento"]} Percentual: {(round(p["faturamento"]/faturamentoTotal ,2))* 100}%")
        


def relatorio():
    print(("="*5)+" RELATÓRIO DE VENDAS "+("="*5))
    print("\n")
    faturamento()
    quantidade()
    print("\n")
    
    produtoMaisVendido()
    produtoMaiorFaturamento()

    print("\n")
    print(("="*5)+" Categorias "+("="*5))
    
    faturamentoCategoria(1)
    print("\n")
    
relatorio()
