temp = input().split(" ")
n = int(temp[0])
c = int(temp[1])
temp = input().split(" ")
points = []
for i in range(n):
    points.append(int(temp[i]))

counter = 0

# triangles = []

for i in range(n):
    p1 = points[i]
    for j in range(i+1, n):
        p2 = points[j]

        if(p1 == p2):
            continue

        c2 = round(c/2, 1)
        if(p1 >= c2):
            d1 = p1 - c2
        else:
            d1 = c2 + p1
        if(p2 >= c2):
            d2 = p2 - c2
        else:
            d2 = c2 + p2

        if(abs(d1-d2) < c2):
            if(d1 < d2):
                for k in range(j+1, n):
                    if(points[k] > d1 and points[k] < d2):
                        counter += 1
                        # triangles.append((i+1, j+1, k+1))
            elif(d1 > d2):
                for k in range(j+1, n):
                    if(points[k] > d2 and points[k] < d1):
                        counter += 1
                        # triangles.append((i+1, j+1, k+1))
        elif(abs(d1-d2) > c2):
            if(d1 < d2):
                for k in range(j+1, n):
                    if(points[k] > d2 or points[k] < d1):
                        counter += 1
                        # triangles.append((i+1, j+1, k+1))
            elif(d1 > d2):
                for k in range(j+1, n):
                    if(points[k] > d1 or points[k] < d2):
                        counter += 1
                        # triangles.append((i+1, j+1, k+1))

print(counter)
# print(triangles)