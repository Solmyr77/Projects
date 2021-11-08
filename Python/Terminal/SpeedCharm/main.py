import time

print('Test')

input('Press Enter')

start = time.time()

for i in range(0, 1000000):
    print(i)

end = time.time()

print(end-start)

