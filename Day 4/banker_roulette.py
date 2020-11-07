import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")


num_items = len(names)
# Generate random number between 0 and last index
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to buy the meal today!")

# Using .choice():
# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} is going to buy the meal today!")
