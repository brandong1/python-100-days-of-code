# Add all even numbers between 1 and 100:

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

for number in range(1, 101):
    if number % 2 == 0:
        total + -= number
print(total)
