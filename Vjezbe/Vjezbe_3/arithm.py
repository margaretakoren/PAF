import math

# aritmetička sredina
def aritmeticka_sredina(lista):
    return sum(lista) / len(lista)

# standardna devijacija
def standardna_devijacija(lista):
    mean = aritmeticka_sredina(lista)
    squared_diff = sum((x - mean) ** 2 for x in lista)
    variance = squared_diff / len(lista)
    return math.sqrt(variance)

def main():
    tocke = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

    print("Ulazne točke:", tocke)
    print("Aritmetička sredina:", aritmeticka_sredina(tocke))
    print("Standardna devijacija:", standardna_devijacija(tocke))

main()
