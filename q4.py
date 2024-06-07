marcas_de_carros = [
    "Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen",
    "BMW", "Mercedes-Benz", "Audi", "Nissan", "Hyundai",
    "Tesla", "Subaru", "Porsche", "Lexus", "Kia",
    "Mazda", "Fiat", "Jaguar", "Land Rover", "Volvo"
]
nome_do_carro = input("Digite o nome do carro procurado: ")


for marca in marcas_de_carros:
    if marca == nome_do_carro:
        print("Carro encontrado")
        break
else:
    print("Carro não encontrado!")

