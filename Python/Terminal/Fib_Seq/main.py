from functools import cache


user_input = int(input('Meddig menjen?: '))


@cache
def fib(num):
    if num<= 1:
        return num
    return fib(num - 1) + fib(num-2)


fib_var = 0
for i in range(user_input):
    fib_var = fib(i)


print(fib_var)
