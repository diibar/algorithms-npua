def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(0, i):
            if a[i] > a[j]:
                k = a[i]
                a[i] = a[j]
                a[j] = k
    return a
a = [1, 10, 56, 20, 14, 3]
sorted_a = insertion_sort(a)
print(sorted_a)