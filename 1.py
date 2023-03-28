x = int(input("Введите число A: "))
y = int(input("Введите число B: "))

def pov(a, n):
    if (n == 1):
        return a
    else:
        return a * pow(x, n - 1)
print(pov(x, y))