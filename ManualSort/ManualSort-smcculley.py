import random

unordered = random.sample(range(10), 10)
random.shuffle(unordered)

print(unordered)
ordered = []

while len(unordered) > 0:
    lowest = unordered[0]
    for i in unordered:
        if(i < lowest):
            lowest = i
    ordered.append(lowest)
    unordered.remove(lowest)

print(ordered)
