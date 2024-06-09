import random
from collections import Counter

def simulate_dice_rolls(rolls):
    sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(rolls)]
    counts = Counter(sums)
    probabilities = {sum_: count / rolls for sum_, count in counts.items()}
    return probabilities

num_rolls = 1000000

probabilities = simulate_dice_rolls(num_rolls)

print("Сума  |Ймовірність")
for sum_, prob in sorted(probabilities.items()):
    print(f"{sum_:<6}|{prob:<20}")

