import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min

    num = random.random() * (max - min) + min

    return round(num)
print(randInt())                  # 0 to 100
print(randInt(max=50))            # 0 to 50
print(randInt(min=50))            # 50 to 100
print(randInt(min=50, max=500))   # 50 to 500