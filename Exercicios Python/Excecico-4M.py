def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 +nota3) / 2
    return media

n1 = float(input (" Digite a primeira nota"))
n2 = float(input (" Digite a primeira nota"))
n3 = float(input (" Digite a primeira nota"))

Resultado_media = calcular_media (n1, n2, n3)
print(f"a media final é : {Resultado_media: .2f}")
if Resultado_media >=7:
    print ("Situação: aprovada!")
else:
    print("Situação: Reprovado")
