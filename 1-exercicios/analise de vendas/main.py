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
            
        
        print(f"Faturamento: {faturamento}")
    else:
        faturamentoIndividual = 0
        for item in vendas:
                faturamentoIndividual += (item['quantidade'] * item['preco'])
                    
                
                print(f"Produto: {item["produto"]} Faturamento: {faturamentoIndividual}")

def quantidade():
    qtd = 0
    for item in vendas:
        qtd += item['quantidade']
    
    print(f"Quantidade: {qtd}")


def produtoMaisVendido():

    maisVendido = sorted(vendas,key= lambda v: v["quantidade"], reverse=True)
    
    print(maisVendido[0])
    
def produtoMaiorFaturamento():
    maiorFaturamento = sorted(vendas,key= lambda v: (v["quantidade"] * v["preco"]), reverse=True)
    
    print(maiorFaturamento[0])
    
def cincoVendas():
    for i in vendas:
        if i["quantidade"]>5:
            print(i)

def faturamentoCategoria( str = True):
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
                
    if str:
        for item in categoria:
            print(item)
    return categoria
            
            
# print(sorted(faturamentoCategoria(False), key= lambda c : c["faturamento"], reverse=True)[0])

def percentualCategoria():
    percentual = faturamentoCategoria(False)
    
    faturamentoTotal = 0
    
    for p in percentual:
        faturamentoTotal += p["faturamento"]
    
    for p in percentual:
        print(f"Categoria: {p["categoria"]} Faturamento: {p["faturamento"]} Percentual: {(round(p["faturamento"]/faturamentoTotal ,2))* 100}%")
        
percentualCategoria()



