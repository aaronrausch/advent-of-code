
with open('inputs/2020-12-05.txt') as raw_ticket_data:
    tickets = raw_ticket_data.read().splitlines()


def ticket_data(ticket):

    # Once I solved the "trick" of each seat being a binary representation of the seat ID,
    # implementing the solution wasn't too much trouble.
    row_characters = ticket[:7].replace('B', '1').replace('F', '0')
    column_characters = ticket[7:].replace('R', '1').replace('L', '0')

    row = int(row_characters, 2)
    column = int(column_characters, 2)

    return (row, column)


def seat_id(ticket):

    row, column = ticket_data(ticket)
    seat_id = (row * 8) + column
    return seat_id


# PART 1
seat_ids = [seat_id(ticket) for ticket in tickets]
highest_seat = max(seat_ids)


# PART 2
def your_seat(seat_list):

    your_seat = -1
    seat_list = sorted(seat_list)

    for i, seat in enumerate(seat_list):
        try:
            if seat_list[i + 1] != seat + 1:
                your_seat = seat + 1
        except IndexError:
            print('Reached end of seating chart.')

    return your_seat
