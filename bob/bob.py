def response(hey_bob):
    mensaje = hey_bob.strip()

    if not mensaje:
        return "Fine. Be that way!"

    elif mensaje[-1] == "?" and mensaje.isupper():
        return "Calm down, I know what I'm doing!"

    elif mensaje.isupper():
        return "Whoa, chill out!"

    elif mensaje[-1] == "?":
        return "Sure."

    else:
        return "Whatever."