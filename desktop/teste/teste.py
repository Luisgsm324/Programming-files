def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Construir um max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrair elementos um a um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def calcular_multiplicacao_maxima(arr):
    heapsort(arr)
    return arr[-1] * arr[-2]

# Entrada de exemplo
entrada = input()
numeros = list(map(int, entrada.split(',')))

resultado = calcular_multiplicacao_maxima(numeros)
print("R${}".format(resultado))