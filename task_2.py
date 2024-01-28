import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        population = range(min, max+1)
        lot_numb = random.sample(population, quantity)
        lot_numb.sort()

        return lot_numb
    else:
        print(f"Введіть значення в діапазоні від 1-1000")


res = get_numbers_ticket(1, 1000, 1001)
print("Ваші лотерейні числа:", res)






# min = 1
# max = 49

# population = range(min, max)
# population2 = range(min, max + 1)

# population = list(population)


# print(population)
# print(list(population2))