#Write code using for loops that lists AND counts all the possible book orders. It should display a list of all the possibilities, and it should provide a final count at the end.
count = 0
classes = ['astronomy', 'calculus', 'chemistry', 'french', 'history', 'literature', 'physics']
N = len(classes)

for i in range(0,N-3):
    for j in range(i+1,N-2):
        if i != j:
            for k in range(j+1,N-1):
                if k != i and k != j:
                    for l in range(k+1,N):
                        if l != i and l != j and l != k:
                            print(classes[i], classes[j], classes[k], classes[l], sep=", ")
                            count += 1
print (count)