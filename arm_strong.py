def is_arm_strong(number):
    num = list(map(int, str(number)))
    n = len(num)
    return number == sum([x**n for x in num])