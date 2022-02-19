x = int(input()) # number of constraints that say people need to be togehter
together = []
for i in range(x):
    temp = input()
    together.append(temp.split(" "))
y = int(input()) # number of constraints that say people need to be separated
separated = []
for i in range(y):
    temp = input()
    separated.append(temp.split(" "))
g = int(input())
groups = []
for i in range(g):
    temp = input()
    groups.append(temp.split(" "))

counter = 0

for i in range(x):
    for j in range(g):
        if(together[i][0] in groups[j]):
            if(together[i][1] not in groups[j]):
                counter += 1
            break

for i in range(y):
    for j in range(g):
        if(separated[i][0] in groups[j]):
            if(separated[i][1] in groups[j]):
                counter += 1
            break
        
print(counter)