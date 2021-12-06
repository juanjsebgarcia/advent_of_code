def input_to_bingo(input_):
    lines = input_.split('\n')
    numbers = lines.pop(0).split(',')

    lines.pop(0)  # Remove leading seperator

    if lines[-1] == '':
        lines.pop()

    cards = []
    card = []
    for line in lines:
        if line == '':
            cards.append(card)
            card = []
            continue

        card.append(line.split())

    cards.append(card)

    return numbers, cards


def play(input_str):
    numbers, cards = input_to_bingo(input_str)
    played_numbers = []
    for _ in numbers:
        played_numbers.append(numbers.pop(0))
        if len(played_numbers) < 5:
            continue

        for card in cards:
            if is_winning_card(card, played_numbers):
                return win(card, played_numbers)



def is_winning_card(card, played_numbers):
    for i in range(0, len(card[0])):
        if is_winning_row(card, i, played_numbers):
            return True

    for i in range(0, len(card[0][0])):
        if is_winning_column(card, i, played_numbers):
            return True


def is_winning_row(card, index, played_numbers):
    return all([number in played_numbers for number in card[index]])


def is_winning_column(card, index, played_numbers):
    column_vals = []
    for row in card:
        column_vals.append(row[index])

    return all([number in played_numbers for number in column_vals])


def sum_missing(card, played_numbers):
    total = 0
    for row in card:
        for num in row:
            if num not in played_numbers:
                total += int(num)

    return total


def win(card, played_numbers):
    current_number = played_numbers[-1]
    result = int(current_number) * sum_missing(card, played_numbers)
    return result


with open('bingo_1.txt', 'r') as file:
    contents = file.read()
    print(play(contents))
