def heapify(lst, n, i):
    lft = 2 * i + 1
    rgt = 2 * i +  2
    mx = i
    if lft < n and lst[lft] > lst[mx]:
        mx = lft
    if rgt < n and lst[rgt] > lst[mx]:
        mx = rgt
    if i != mx:
        lst[i], lst[mx] = lst[mx], lst[i]
        heapify(lst, n, mx)

def build_max_heap(lst):
    n = len(lst)
    for i in range(n//2 - 1, -1, -1):
        heapify(lst, n, i)

def heap_sort(lst):
    n = len(lst)
    build_max_heap(lst)
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)
    return lst

a = [1, 20, 3, 12, 0, 6]
b = heap_sort(a)
print(b)