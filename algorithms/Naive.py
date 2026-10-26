def naive_match(T, P):
    n, m = len(T), len(P)
    shifts = []
    for s in range(n - m + 1):
        j = 0
        while j < m and T[s + j] == P[j]:
            j += 1
        if j == m:
            shifts.append(s)
    return shifts

T = "acaabcaccaab"
P = "aab"
res = naive_match(T, P)

print(f"Text: {T}")
print(f"Pattern: {P}")
print(f"Pattern positions: {res}")