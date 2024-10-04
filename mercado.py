print("Hello World")

nome = input("Digite o primeiro nome: ")
CPF = input("Digite o seu CPF: ")

print("-----------Mercadinho do Gás--------------")
print("Olá cliente, seja bem-vindo ao nosso mercadinho")
print('Temos duas categorias: '
      'A - Frutas\n'
      'B - Alimentação')

carrinho = {}
escolha_alimentacao = ""
escolha_frutas = ""
desejo = input("O que você deseja? (Digite A para Frutas ou B para Alimentação): ")

frutas = {"maçã": 2.00, 'banana': 3.00, 'laranja': 4.00, 'melancia': 10.00, 'abacaxi': 8.00}
alimentacao = {'arroz': 10.00, 'feijao': 8.00, 'macarrão': 5.00, 'leite': 4.00, 'carne': 17.00}

if desejo == 'A':
    print("Frutas disponíveis:")
    for fruta,preco in frutas.items():
        print(f"{fruta.capitalize()}: R$ {preco:.2f}")

    escolha_frutas = input('Selecione o produto: ').lower()

    if escolha_frutas in frutas:
        quantidade = int(input(f"Quantas unidades de {escolha_frutas} você deseja adicionar? "))
        carrinho[escolha_frutas] = carrinho.get(escolha_frutas, 0) + quantidade * frutas[escolha_frutas]
        print(f"{quantidade} unidade(s) de {escolha_frutas.capitalize()} adicionada(s) ao carrinho.")
    else:
        print("Produto não disponível.")

elif desejo == 'B':
    print("Alimentação disponível:")
    for item, preco in alimentacao.items():
        print(f"{item.capitalize()}: R$ {preco:.2f}")

    escolha_alimentacao = input('Selecione o produto: ').lower()

    if escolha_alimentacao in alimentacao:
        quantidade = int(input(f"Quantas unidades de {escolha_alimentacao} você deseja adicionar? "))
        carrinho[escolha_alimentacao] = carrinho.get(escolha_alimentacao, 0) + quantidade * alimentacao [escolha_alimentacao]
        print(f"{quantidade} unidade(s) de {escolha_alimentacao.capitalize()} adicionada(s) ao carrinho.")
    else:
        print("Produto não disponível.")

else:
    print("Categoria inválida.")

print("Seu carrinho de compras:")
total = 0
for item, valor in carrinho.items():
    print(f"{item.capitalize()}: R$ {valor:.2f}")
    total += valor

print(f"Total: R$ {total:.2f}")

with open("NotaFiscal.txt", "w") as arquivo:
    arquivo.write(f"\n------------------------CUPOM FISCAL-------------------------:")
    arquivo.write(f"\n Nome:  {nome} ")
    arquivo.write(f"\n CPF do consumidor: {CPF}")
    arquivo.write(f"\n item código descrição qtd.un.vl unit R$ st a/t vl item R$")
    arquivo.write(f"\n--------------------------------------------------------------")
    arquivo.write(f"\n                  TOTAL da compra: {total} R$ ")
    arquivo.write(f"\n                  Foi comprado: {escolha_frutas}")
    arquivo.write(f"\n--------------------------------------------------------------")
    arquivo.write(f"\n                Tenha um bom dia, volte sempre!!! ")
