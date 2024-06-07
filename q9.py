marcas_de_carros = [
    "Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen",
    "BMW", "Mercedes-Benz", "Audi", "Nissan", "Hyundai",
    "Tesla", "Subaru", "Porsche", "Lexus", "Kia",
    "Mazda", "Fiat", "Jaguar", "Land Rover", "Volvo"
]

def procurar_carro(nome_carro):
    for marca in marcas_de_carros:
        if marca == nome_carro:
            return True
    return False

def avaliacao_carro(preco):
    if preco < 10000:
        return "mal estado"
    elif preco < 30000:
        return "conservado"
    elif preco < 60000:
        return "seminovo"
    else:
        return "novo"

while True:
    
    nome_do_carro = input("Por favor, digite o nome do carro: ")
    
    preco_do_carro = float(input("Por favor, digite o preço do carro: "))
    
    if procurar_carro(nome_do_carro):
      
        qualidade_carro = avaliacao_carro(preco_do_carro)
       
        print(f"O usuário gostaria de um carro {nome_do_carro} na qualidade de {qualidade_carro}.")
    else:
        print("Carro não encontrado na lista!")
    
    
    continuar = input("Deseja continuar? (Digite 'sim' para continuar ou qualquer outra tecla para sair): ")
    if continuar != 'sim':
        break
