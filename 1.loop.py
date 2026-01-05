#Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times).
import random

rolls = []
count_6 = 0
count_1 = 0
two_6s_in_row = 0

previous_roll = None

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6s_in_row += 1

    if roll == 1:
        count_1 += 1

    previous_roll = roll

print("Dice rolls:", rolls)
print("Number of times rolled a 6:", count_6)
print("Number of times rolled a 1:", count_1)
print("Number of times two 6s in a row:", two_6s_in_row)