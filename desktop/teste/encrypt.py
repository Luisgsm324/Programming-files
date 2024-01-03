class System:
    def encrypt(self, message):
        return_string = ""    
        for letter in message:
            value = ord(letter) - 63
            if value > 9:
                if value > 18: # Maior que 18 (obrigatoriamente menor ou igual a 90)
                    value -= 18
                    return_string += str(value) + "99"
                else: # Maior que 9 e menor que 18
                    value -= 9
                    return_string += "0" + str(value) + "9"
            else:
                return_string += "00" + str(value)
        return return_string
    
    def decrypt(self, message):
        count = 1
        return_string = ""
        prov_string = ""
        for number in message:
            prov_string += number
            if count < 3:       
                count += 1
            else:
                prov_string = list(prov_string) 
                prov_list = [eval(element) for element in prov_string]
                sum_list = sum(prov_list) + 63
                return_string += chr(sum_list)
                count = 1
                prov_string = "" 
        
        if len(message) % 3 != 0:
            prov_string = list(prov_string) 
            prov_list = [eval(element) for element in prov_string]
            sum_list = sum(prov_list) + 63
            return_string += chr(sum_list)
        
        return return_string      

string = "Oi"
formated_string = ""
for letter in string:
    if letter != " ":
        formated_string += letter
print(formated_string)
system = System()
element = system.encrypt(formated_string.upper())
print(element)
print(system.decrypt(element))