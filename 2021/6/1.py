def tick():
    next_gen = []
    for age in fishes:
        if age > 0:
            next_gen.append(age - 1)
        else:
            next_gen.append(8)
            next_gen.append(6)

    return next_gen


with open('in_1.txt', 'r') as file:
    initial = file.read().replace('\n', '').split(',')
    fishes = [int(days) for days in initial]
    for i in range(0, 80):
        fishes = tick()

    print(len(fishes))
