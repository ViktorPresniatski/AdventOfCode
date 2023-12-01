from collections import defaultdict


def main():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    summ = sum(arr)
    if summ % 3 != 0:
        print(0)
        return

    s = summ // 3

    if s == 0:
        cur_summ = 0
        cnt_of_zeros = 0
        for a_i in arr:
            cur_summ += a_i
            if cur_summ == 0:
                cnt_of_zeros += 1
        n = cnt_of_zeros - 1
        ans = n * (n - 1) // 2
        # ans => (4 * 3) / 2 = 6
        print(ans)
        return

    ans = 0
    cur_summ = 0
    cnt_of_s = 0
    for a_i in arr:
        cur_summ += a_i
        if cur_summ == s:
            cnt_of_s += 1
        elif cur_summ == (s + s):
            ans += cnt_of_s

    print(ans)

    # cur_summ = 0
    # ans = 0
    # for a_i in arr:
    #     cur_summ += a_i
    #     dic[cur_summ] -= 1
    #     if cur_summ == s:
    #         ans += dic[s + s]

    print(ans)

main()