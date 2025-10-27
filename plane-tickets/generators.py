"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ["A","B", "C", "D"]
    for i in range(number):
        yield letters[i % 4]



def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    contador = 1
    letter = generate_seat_letters(number)
    for i in letter:
        if contador == 13:
            contador += 1
        generateseats = str(contador) + i
        if i == "D":
            contador += 1
        yield generateseats
    
seats = generate_seats(10)
print(next(seats))
print(next(seats))
print(next(seats))
print(next(seats))
print(next(seats))
print(next(seats))
print(next(seats))
print(next(seats))
print(next(seats))



def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    dictionary = {}
    quantity = len(passengers)
    seats = generate_seats(quantity)

    for passenger in passengers:
        seat = next(seats)
        dictionary[passenger] = seat
    
    return dictionary



def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket = (seat + flight_id)
        while len(ticket) < 12:
            ticket += "0"
        yield ticket
        
