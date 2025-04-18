li=[[1,2,2,7,8,9,10],[14],[7,9]]
max = li[0][0]
min = li[0][0]
for i in li:
    for j in i:
        if j>max:
           max=j
        if j<min:
           min=j

print(max)
print(min)
