def prostoe_sostavnoe(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Введи число от 0 до 1000: "))

if num == 1:
    print("Единица")
else:
    if num == 0:
        print("Ноль")
    else:
        if prostoe_sostavnoe(num):
            print("Простое число")
        else:
            print("Составное число")