def reverse_string(string):
    new_string = ""
    for index in range(len(string)):
        new_string += string[-(index + 1)]
    return new_string

print(reverse_string("We will conquere COVID-19"))
