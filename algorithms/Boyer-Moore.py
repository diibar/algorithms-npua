P = "abacab"
S = set()
M = len(P)
d = {}

for i in range(M-2, -1, -1):
    if P[i] not in S:
        d[P[i]] = M-i-1
        S.add(P[i])

if P[M-1] not in S:
    d[P[M-1]] = M
d['*'] = M

print(d)

T = "abacaabadcabacabaabb"
N = len(T)

if N >= M:
    i = M-1

    while i < N:
        k = 0

        for j in range(M-1, -1, -1):
            if T[i-k] != P[j]:
                c = T[i-k]

                if c == P[M-1]:
                    off = 1
                else:
                    off = max(1, d.get(c, d['*']) - k)

                i += off
                break

            k += 1
        else:
            print(f"Pattern found at index {i-k+1}")
            break
    else:
        print("Pattern not found")
else:
    print("Pattern not found")