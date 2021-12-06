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

    remaining_cards = cards.copy()

    pending_numbers = numbers.copy()

    played_numbers = []

    last_card = None

    for _ in numbers:
        played_numbers.append(pending_numbers.pop(0))

        remaining_cards = remove_winning_cards(remaining_cards, played_numbers)


        if len(remaining_cards) == 1:
            last_card = remaining_cards[0]

        if len(remaining_cards) == 0:
            played_numbers.append(pending_numbers.pop(0))
            return win(last_card, played_numbers)


def remove_winning_cards(cards, played_numbers):
    for i in range(0, len(cards)):
        if is_winning_card(cards[i], played_numbers):
            cards.pop(i)
            return remove_winning_cards(cards, played_numbers)

    return cards


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
    return int(current_number) * sum_missing(card, played_numbers)


with open('bingo_2.txt', 'r') as file:
    print(play(file.read()))
