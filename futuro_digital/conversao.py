class unidadeMedida:
    def __init__(self,):
        pass
def converterValor(sistema, valor, unidade_inicial, unidade_destino):
    match sistema:
        case "comprimento":
            
        case "massa":
        
tipo = int(input("Digite o numero da unidade deseja:\n1 - Comprimento\n2 - Massa\n3 - Capacidade\n4 - Superficie\n5 - Volume\n"))
valor = 0
unidade_inicial = 0
unidade_destino = 0
valor_convertido = 0
match tipo:
    case 1:
        valor = int(input("1 - km\n2 - m\n3 - cm\n4 - mm\nDigite o valor que será convertido: "))
        
    case 2:
        valor = int(input("1 - Kg\n2 - g\n3 - mg\nDigite o valor que será convertido: "))
    
    case 3:
        valor = int(input("1 - l\n2 - ml\nDigite o valor que será convertido: "))
    
    case 4:
        valor = int(input("1 - km²\n2 - m²\n3 - cm²\nDigite o valor que será convertido: "))
    
    case 5:
        valor = int(input("1 - m³\n2 - cm³\nDigite o valor que será convertido: "))
        
unidade_inicial = int(input("Agora escolha a unidade de medida deste valor: "))
unidade_destino = int(input("Para qual unidade deseja converter: "))

match tipo:
    case 1:
        valor_convertido = converterValor("comprimento", valor, unidade_inicial, unidade_destino)
    case 2:
        valor_convertido = converterValor("massa", valor, unidade_inicial, unidade_destino)
    case 3:
        valor_convertido = converterValor("capacidade", valor, unidade_inicial, unidade_destino)
    case 4:
        valor_convertido = converterValor("superficie", valor, unidade_inicial, unidade_destino)
    case 5:
        valor_convertido = converterValor("volume", valor, unidade_inicial, unidade_destino)

print(f"O resultado da conversão de {valor}[unidade_inicial] para [unidade_destino] é {valor_convertido}[unidade_destino]")