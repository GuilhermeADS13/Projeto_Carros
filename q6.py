marcas_de_carros = [
    "Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen",
    "BMW", "Mercedes-Benz", "Audi", "Nissan", "Hyundai",
    "Tesla", "Subaru", "Porsche", "Lexus", "Kia",
    "Mazda", "Fiat", "Jaguar", "Land Rover", "Volvo"
]

def procurar_carro(nome_carro):
    for marca in marcas_de_carros:
        if marca == nome_carro:
            return "Carro encontrado"
    return "Carro não encontrado"
nome_do_carro = input("Por favor, digite o nome do carro a ser procurado: ")

resultado = procurar_carro(nome_do_carro)

print(resultado)
