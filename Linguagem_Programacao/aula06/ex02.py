numeros = [1, 2, 3]
[x, y, z] = numeros

print('x', x)
print('y', y)
print('z', z)

def func():
    return x + y

num = func()
print("num:", num)

for nums in numeros:
    print(nums)

print("\n")

for nums in range(len(numeros)):
    print(numeros[nums])