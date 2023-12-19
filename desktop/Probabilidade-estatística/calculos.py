dicionario = {}
valores = [25, 32, 20, 28, 22, 36, 19, 31, 24, 27, 35, 29, 26, 21, 23, 37, 30, 18, 34, 39, 38, 33, 40, 25,
19, 28, 22, 31, 36, 20, 27, 33, 35, 24, 26, 30, 38, 29, 32, 23, 37, 21, 34, 18, 39, 40, 19, 22,
25, 28]
print(len(valores))
valores.sort()
print(valores[0:24])

print("---------------------")
for number in valores:
    if number not in dicionario.keys():
        dicionario[number] = 1
    else:
        dicionario[number] += 1

print(dicionario)

if len(valores) % 2 == 0:
    mediana = (valores[(len(valores)//2) - 1 ] + valores[(len(valores)//2)])/2
else:
    mediana = valores[len(valores)//2]

media = sum(valores)/len(valores)

moda = [0, 0] # Primeiro item, quantas vezes repetidas e o segundo qual o número mais repetido. 
moda_items = [] # Me dará os outros elementos que tem a mesma frequência que a Moda (que será determinada como a primeira)
for value in dicionario:
    if dicionario.get(value) >= moda[0]:
        if dicionario.get(value) == moda[0]:
            moda_items.append(value)
        else:
            moda[0] = dicionario.get(value)
            moda[1] = value
print(moda_items)

print(f"Medidas centrais obtidas:\nMédia: {media:.2f}\nMediana: {mediana}\nModa: {moda[1]} (repetiu-se {moda[0]} vezes)")

string_list = [str(elem) for elem in valores]
print("+".join(string_list))
print("Classe -- Frequência")
for key, value in dicionario.items():
    print(f"{key}    |     {value}")




