def hash_table_process(array, days_array):
    prov_array = [] # Uma array provisória criada para adicionar os elementos que em seguida serão adicionadas na array de dias
    value = 0 # O valor do somatório que será definido inicialmente como zero (ele pegará os valores ASCII)
    
    for element in array:
        if element not in prov_array: 
            value += ord(element)
            prov_array.append(element)
        else: # Se o elemento já estiver sido adicionado (cria-se um novo grupo)
            index = value % 10
            count = 0
            while days_array[index] != "vago" and count != 10:
                count += 1
                index += 1
                if index >= 10:
                    index = 0      
            
            days_array[index] = prov_array
            prov_array = []
            value = 0
            value += ord(element)
            prov_array.append(element)
    
    index = value % 10
    count = 0
    while days_array[index] != "vago" and count != 10:
        count += 1
        index += 1
        if index >= 10:
            index = 0      
    days_array[index] = prov_array
    
    return days_array


days = []
for _ in range(10):
    days.append("vago")

question = input()

array = list(question)

print(hash_table_process(array, days))

