def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    lista = list(range(1, number + 1))
    for i in lista:
        grains = 2 ** (i - 1)
    return grains


        

def total():
    grains = 0
    for i in range(1, 65):
        grains += 2 ** (i - 1)
    return grains
