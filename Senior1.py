n = int(input())

counter = 0

for i in range(int(n/4)+1):
    m = i*4
    if((n - m)%5 == 0):
        counter += 1

print(counter)