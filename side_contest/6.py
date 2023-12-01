
class Fenvik:
    def __init__(self, N):
        self.arr = [0] * (N + 1)
        self.n = N

    def set(self, pos, val):
        print("set ", pos,  " val ", val)
        while pos <= self.n:
            self.arr[pos] = max(self.arr[pos], val)
            pos |= pos + 1

    def get(self, pos):

        res = 0
        p = pos
        while pos >= 0:
            res = max(res, self.arr[pos])
            pos &= pos + 1
            pos -= 1
        print("get ", p, " res: ", res)
        return res

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = []
    dp.append([0] * N)
    dp.append([0] * N)

    order = [dict()] * 2
    index = 0
    for val in set(arr):
        order[0][val] = index
        index += 1
    index = 0
    for val in reversed(set(arr)):
        order[1][val] = index
        index += 1


    print(order)

    dp[0][0] = dp[1][0] = 1
    if arr[0] < arr[1]:
        dp[0][1] = 2
        dp[1][1] = 1
    elif arr[0] > arr[1]:
        dp[0][1] = 1
        dp[1][1] = 2
    else:
        dp[0][1] = 1
        dp[1][1] = 1
    f = [Fenvik(N), Fenvik(N)]

    for i in range(2):
        for fl in range(2):
            f[fl].set( order[fl][arr[i]] , dp[fl][i] )

    for i in range(2, N):
        for fl in range(2):
            pos = order[fl][arr[i]]

            dp[fl][i] = f[fl ^ 1].get()
        pos0 = order[0][arr[i]]
        pos1 = order[1][arr[i]]

        dp[0][i] = f[1].get( pos1 - 1 ) + 1
        dp[1][i] = f[0].get( pos0 - 1 ) + 1
        f[0].set(pos0, dp[0][i])
        f[1].set(pos1, dp[1][i])

    print(dp)
    res = N - max(max(dp[0]), max(dp[1]))
    print(res)


main()
