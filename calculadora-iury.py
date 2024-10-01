print("Escolha uma operação")
print('m = multiplicação')
print('d = divisão')
print('a = adição')
print('s = subtração')

escolha = str(input('Digite uma das operações desejadas entre m,d,a,s'))
digite_um_numero = int(input("Digite um Número: "))
digite_mais_um = int(input("Digite um Número: "))
m = digite_um_numero*digite_mais_um
d = digite_um_numero/digite_mais_um
a = digite_um_numero+digite_mais_um
s = digite_um_numero-digite_mais_um
print('a multiplicação é: {}, a divisão é: {}, a adição é: {}, a subtração é: {}'.format(m, d, a, s))
