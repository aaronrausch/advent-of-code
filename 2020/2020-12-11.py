
with open('inputs/2020-12-11.txt') as seating_chart_data:

    seating_chart = [[seat for seat in row]
                     for row in seating_chart_data.read().splitlines()]
    rows = len(seating_chart)
    columns = len(seating_chart[0])  # Check length of first row

    # Adding 1-cell of padding to entire border of seating chart
    columns_padding = ['@'] * columns
    seating_chart.insert(0, columns_padding)
    seating_chart.insert(len(seating_chart), columns_padding)

    for row in seating_chart:
        row.insert(0, '@')
        row.insert(len(row), '@')


# CURRENTLY BROKEN
def calculate_seats(chart):

    modified_chart = chart.copy()

    for i, row in enumerate(chart[1:rows - 1], 1):
        for j, seat in enumerate(row[1:columns - 1], 1):

            conditions = (
                (chart[i - 1][j - 1] in '@.L'),
                (chart[i - 1][j] in '@.L'),
                (chart[i - 1][j + 1] in '@.L'),

                (chart[i][j - 1] in '@.L'),
                (chart[i][j + 1] in '@.L'),

                (chart[i + 1][j - 1] in '@.L'),
                (chart[i + 1][j] in '@.L'),
                (chart[i + 1][j + 1] in '@.L'),
            )

            if all(conditions):
                modified_chart[i][j] = '#'

    return modified_chart
