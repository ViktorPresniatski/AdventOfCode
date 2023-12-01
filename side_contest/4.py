def main():
    N = int(input())
    string = input()

    ans = 0
    balance = 0
    for c in string:
        if c == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0 and c == ')':
            ans += 1

    if balance != 0:
        print('-1')
    else:
        print(ans * 2)

main()