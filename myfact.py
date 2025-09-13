def my_factorial(n):
    if n < 0:
        raise ValueError("Без негатива (негативных чисел), пожалуйста")
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a

print(my_factorial(int(input())))
