n = int(input("Enter building floors: "))
e = int(input("Enter egg quantity: "))
m = 0

dp = [0] * (e + 1)

while dp[e] < n:
    m += 1
    for k in range(e, 0, -1):
        dp[k] = dp[k] + dp[k - 1] + 1

print("Minimum number of drops:", m)