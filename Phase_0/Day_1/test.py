def add(a, b):
    return a + b


def func(x, y, z):
    if x > y and y > z:
        print("x is greatest")
    else:
        print("not greatest")


numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(i, numbers[i])


data = [("alice", 20), ("bob", 25), ("charlie", 30)]
for n, age in enumerate(data):
    print(n, age)

