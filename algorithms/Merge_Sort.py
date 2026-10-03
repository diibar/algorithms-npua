def Merge(lst, left, mid, right):
    lft = lst[left:mid]
    rgt = lst[mid:right]
    i = j = 0
    k = left
    while i < len(lft) and j < len(rgt):
        if lft[i] <= rgt[j]:
            lst[k] = lft[i]
            i += 1
        else:
            lst[k] = rgt[j]
            j += 1
        k += 1

    while i < len(lft):
        lst[k] = lft[i]
        i += 1
        k += 1

    while j < len(rgt):
        lst[k] = rgt[j]
        j += 1
        k += 1


def MergeSort(lst, left=0, right=None):
    if right is None:
        right = len(lst)
    if right - left > 1:
        m = (right + left) // 2
        MergeSort(lst, left, m)
        MergeSort(lst, m, right)
        Merge(lst, left, m, right)


a = [6, 5, 12, 10, 9, 1]
MergeSort(a)
print(a)