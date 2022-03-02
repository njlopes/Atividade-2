lados = int(input("Digite a quantidade de lados:"))
lado = float(input("Digite a medida do lado:"))

if lados == 3:
    area= lado ** 2 * 3 ** (1/2) / 4
    print("A figura é um triângulo.")
    print("A área é: %.2fcm2"%area)
    
elif lados == 4:
    area = lado ** 2
    print("A figura é um quadrado.")
    print("A área é: %.2fcm2"%area)
    
elif lados ==5:
    print("A figura é um pentágono.")
    
