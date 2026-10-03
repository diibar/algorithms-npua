def part(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quick_sort(lst, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if low < high:
        pi = part(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)


a = [6, 5, 12, 10, 9, 1]
quick_sort(a)
print(a)