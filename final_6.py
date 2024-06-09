def greedy(items, budget):
    sorted_food = sorted(items.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse=True)
    total_calories = 0
    result = []

    for i in sorted_food:

        if budget >= i[1]['cost']:
            budget -= i[1]['cost']
            total_calories += i[1]['calories']
            result.append(i[0])
    
    return result, total_calories

def dynamic(items, budget):
    n=len(items)
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i-1] <= w:
                dp_table[i][w] = max(dp_table[i-1][w], calories[i-1] + dp_table[i-1][w-costs[i-1]])
            else:
                dp_table[i][w] = dp_table[i-1][w]

    result = []
    w = budget
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i-1][w]:
            result.append(item_names[i-1])
            w -= costs[i-1]

    total_calories = dp_table[n][budget]
    return result[::-1], total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = [113, 312, 231, 80, 40, 67, 105]
functions = [greedy, dynamic]

for amount in budget:
    for function in functions:
        result=function(items, amount)
        print(f"Для суми {amount}: Алгоритм: {function.__name__}; Результат: {result}")