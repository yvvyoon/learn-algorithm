from collections import Counter

data = ['red', 'yellow', 'purple', 'green', 'pink', 'black',
        'white', 'skyblue', 'red', 'yellow', 'black', 'black']
counter = Counter(data)

print(counter)
# Counter({'black': 3, 'red': 2, 'yellow': 2, 'purple': 1, 'green': 1, 'pink': 1, 'white': 1, 'skyblue': 1})
print(dict(counter))
# {'red': 2, 'yellow': 2, 'purple': 1, 'green': 1, 'pink': 1, 'black': 3, 'white': 1, 'skyblue': 1}
print(counter['red'])
# 2
print(counter['blue'])
# 0
