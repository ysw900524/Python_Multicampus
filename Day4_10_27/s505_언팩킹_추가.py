def add(a, b):
    return a + b

print(add(1,2))

def add(a, b, c=0):
    return a + b + c

print(add(1,2,3))
print(add(1,2))

def add(numbers):
    for num in numbers:
        num += num
    return num

print(add([10, 20, 30, 40]))
print(add(10, 20, 30, 40))

def add(*numbers):
    for num in numbers:
        num += num
    return num

print(add(10, 20, 30, 40))