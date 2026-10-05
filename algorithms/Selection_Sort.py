def sort(lst):
    for i in range(len(lst)):
        mn = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[mn]:
                mn = j
        lst[i], lst[mn] = lst[mn], lst[i]
    return lst

a = [1, 20, 3, 12, 0, 6]
k = sort(a)
print(k)