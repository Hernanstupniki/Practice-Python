def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    contador = 1
    total = 0
    lista = []
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    while contador < number:
        if number % contador == 0:
            lista.append(contador)
        contador +=1
    for x in lista:
        total += x
    if number == total:
        return ("perfect")
    elif number < total:
        return ("abundant")
    elif number > total:
        return ("deficient")

    pass

classify(12)
