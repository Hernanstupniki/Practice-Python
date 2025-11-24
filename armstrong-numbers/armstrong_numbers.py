def is_armstrong_number(number):
    strnumber = str(number)
    lennumber = len(strnumber)
    numberpoint = 0
    contador = 0
    for i in strnumber:
        value = int(i) ** int(lennumber)
        contador += 1
        numberpoint += value
    if numberpoint == number:
        return True
    else:
        return False
        



is_armstrong_number(9)