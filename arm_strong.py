def is_arm_strong(number):
    num = list(map(int, str(number)))
    n = len(num)
    return number == sum([x**n for x in num])

n = 153
print(is_arm_strong(n)) # True
n = 370
print(is_arm_strong(n)) # True
n = 9474
print(is_arm_strong(n)) # True
n = 123
print(is_arm_strong(n)) # False
n = 142
print(is_arm_strong(n)) # False