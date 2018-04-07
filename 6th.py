X = [1,6,3,4,8,9,4,2,5,7,60,10]
y = []
for i in range(0, len(X)):
    if X[i]%2 == 0:
        y.append(X[i])
print y
y.sort(reverse=True)
print y
