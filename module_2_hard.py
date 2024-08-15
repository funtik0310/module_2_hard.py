def password(numbers):
    password_1 = ""
    for i in range(1, numbers):
        for j in range(i + 1, numbers):
            if numbers % (i + j) == 0:
                password_1 += str(i) + str(j)
    return password_1
print('Введите число: ')
print(password(int(input())))