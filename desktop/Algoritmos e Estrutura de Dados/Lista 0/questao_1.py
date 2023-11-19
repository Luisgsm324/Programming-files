import math

class Computador():
    def __init__(self, nome_comp, capacidade, nome_algo, complexidade):
        self.nome_comp = nome_comp
        self.capacidade = capacidade
        self.nome_algo = nome_algo
        self.complexidade = complexidade
    
    def calcularTempo(self, qtd_instrucoes):
        if self.complexidade == "2n^2":
            calculo = (2 * (qtd_instrucoes**2))/self.capacidade
            return calculo
        elif self.complexidade == "n.logn":
            calculo = (qtd_instrucoes * math.log10(qtd_instrucoes))/self.capacidade
            return calculo
        elif self.complexidade == "n":
            calculo = qtd_instrucoes/self.capacidade
            return calculo
        elif self.complexidade == "2^n":
            calculo = (2**qtd_instrucoes)/self.capacidade
            return calculo
    

def main():
    qtd_intrucoes = int(input())
    
    comp1_input = input().split(" - ")
    comp1 = Computador(comp1_input[0],int(comp1_input[1]),comp1_input[2],comp1_input[3])
    vel1 = comp1.calcularTempo(qtd_intrucoes)
    print(f"Velocidade do {comp1.nome_comp}: {vel1:.2f} segundos")
    
    comp2_input = input().split(" - ")
    comp2 = Computador(comp2_input[0],int(comp2_input[1]),comp2_input[2],comp2_input[3])
    vel2 = comp2.calcularTempo(qtd_intrucoes)
    print(f"Velocidade do {comp2.nome_comp}: {vel2:.2f} segundos")

    if vel1 > vel2:
        print(f"O {comp2.nome_comp} foi mais rápido!")
    else:
        print(f"O {comp1.nome_comp} foi mais rápido!")

main()
