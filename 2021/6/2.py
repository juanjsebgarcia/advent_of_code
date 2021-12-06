FISH_LIFECYCLE_DAYS = 9


def tick(current_ages):
    next_gen = [0] * FISH_LIFECYCLE_DAYS
    spunky_fish = 0

    for x in range(0, FISH_LIFECYCLE_DAYS):
        if x == 0:
            spunky_fish += current_ages[0]
        else:
            next_gen[x-1] = current_ages[x]

    next_gen[6] += spunky_fish  # Old boys
    next_gen[8] += spunky_fish  # New boys

    return next_gen


with open('in_1.txt', 'r') as file:
    initial = file.read().replace('\n', '').split(',')
    ages = [int(days) for days in initial]

    current_gen_ages = [0]*FISH_LIFECYCLE_DAYS

    for age in ages:
        current_gen_ages[age] += 1

    for i in range(0, 256):
        current_gen_ages = tick(current_gen_ages)

    print(sum(current_gen_ages))
