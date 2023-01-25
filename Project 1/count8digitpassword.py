#An 8-digit password is required to have three 0’s and five 1’s. You will determine how many unique passwords are possible.
# count = 0
# passlen = 8

# for i in range(1, passlen+1):
#     for j in range(1, passlen+1):
#         if j != i:
#             for k in range(1, passlen+1):
#                 if k != j and k != i:
#                     print (i, j, k)
#                     count += 1

# print (count)

#An 8-digit password is required to have exactly three 0’s. The other 5 digits can be any number 1-7, but numbers 1-7 may not be repeated.
# count = 0
# arr = []
# nums = [1, 2, 3, 4, 5, 6, 7]
# N = len(nums)

# for a in range(1, N+1):
#     for b in range(1, N+1):
#         if b != a:
#             for c in range(1, N+1):
#                 if c != b and c != a:
#                     for i in range(1, N+1):
#                         for j in range(1, N+1):
#                             if j != i:
#                                 for k in range(1, N+1):
#                                     if k != j and k != i:
#                                         for l in range(1, N+1):
#                                             if l not in [i, j, k]:
#                                                 for m in range(1, N+1):
#                                                     if m not in [i, j, k, l]:
#                                                         arr = []
#                                                         arr.insert(i, i)
#                                                         arr.insert(j, j)
#                                                         arr.insert(k, k)
#                                                         arr.insert(l, l)
#                                                         arr.insert(m, m)
#                                                         arr.insert(a, 0)
#                                                         arr.insert(b+1, 0)
#                                                         arr.insert(c+2, 0)
#                                                         # print(i, j, k, l, m)
#                                                         print(arr)
#                                                         arr = []
#                                                         count += 1
# print (count)

# Take 2
count = 0
arr = []
nums = [1, 2, 3, 4, 5, 6, 7]
N = len(nums)

for a in range(0, N+1):
    for b in range(a+1, N+1):
        if b != a:
            for c in range(b+1, N+1):
                if c != b and c != a:
                    for i in range(N):
                        for j in range(N):
                            if j != i:
                                for k in range(N):
                                    if k != j and k != i:
                                        for l in range(N):
                                            if l not in [i, j, k]:
                                                for m in range(N):
                                                    if m not in [i, j, k, l]:
                                                        arr = []
                                                        arr.insert(i, i)
                                                        arr.insert(j, j)
                                                        arr.insert(k, k)
                                                        arr.insert(l, l)
                                                        arr.insert(m, m)
                                                        arr.insert(a, 0)
                                                        arr.insert(b+1, 0)
                                                        arr.insert(c+2, 0)
                                                        print(arr)
                                                        arr = []
                                                        count += 1
print (count)