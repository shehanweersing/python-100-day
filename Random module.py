import random

random_number = random.randint(1,12)

random_float = random.random()
print(random_number)
print(random_float)



random_head_or_tail = random.randint(0,1)

print(random_head_or_tail)
if random_head_or_tail == 1:
    print("Head")
else:
    print("Tail")
        