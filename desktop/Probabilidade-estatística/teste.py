dicionario = {"Canadá": 280.9,
"Reino Unido": 55.9,
"México": 198.4,
"Japão": 65.7,
"Alemanha":49.2,
"Coreia do Sul": 43.4,
"Taiwan": 25.9,
"Cingapura":31.2,
"Holanda":42.4,
"França": 27.8,
"China":  103.9,
"Brasil": 42.9,
"Austrália":27.5,
"Bélgica":29.9,
"Malásia":14.2,
"Itália": 16.0,
"Suíça":  24.4,
"Tailândia":10.9,
"Arábia Saudita": 13.8,
"Índia": 21.5}

print(len(dicionario)//2)

string = ""
total = 0
for value in dicionario.values():
    total += value
    string += str(value) + " + "
print(string)

print(total/len(dicionario)) # Será a média

sorted_dictionary = sorted(dicionario.items(), key=lambda x:x[1])
print(sorted_dictionary)

print(sorted_dictionary[len(sorted_dictionary)//2])

