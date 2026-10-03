def sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

a = [1,20,3,12,0,6]
k = sort(a)
print(k)