def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    stepscount = 0
    while True:
        if number == 1:
            return stepscount
        elif number % 2 == 0:
            stepscount = stepscount + 1
            number = number // 2
        elif number % 2 != 0:
            stepscount = stepscount + 1
            number = (number * 3) + 1
