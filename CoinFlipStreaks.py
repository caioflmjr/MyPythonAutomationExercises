import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    
    # Code that creates a list of 100 'heads' or 'tails' values
    list = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            list.append('H')
        else:
            list.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(list)):
        if list[i:i + 6] == ['H', 'H', 'H', 'H', 'H', 'H'] or list[i:i + 6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            number_of_streaks += 1
print('Chance of streak: %s%%' % (number_of_streaks / 10000))