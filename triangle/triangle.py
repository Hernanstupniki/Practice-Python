def equilateral(sides):
    a, b, c = sides
    # No puede haber lados de longitud cero
    if min(sides) <= 0:
        return False
    # Todos los lados iguales
    return a == b == c


def isosceles(sides):
    a, b, c = sides
    # Verificar validez del triángulo
    if min(sides) <= 0 or (a + b < c or a + c < b or b + c < a):
        return False
    # Al menos dos lados iguales
    return a == b or a == c or b == c


def scalene(sides):
    a, b, c = sides
    # Verificar validez del triángulo
    if min(sides) <= 0 or (a + b < c or a + c < b or b + c < a):
        return False
    # Todos los lados distintos
    return a != b and a != c and b != c
