x = int(input())
cnt = 0

while x != 1:
    if x % 3 == 0:
        x = x/3
        cnt += 1
    elif x % 2 == 0:
        if (x-1) % 3 == 0 or (x-2) % 3 == 0:
            x = x-1
            cnt += 1

        else:
            x = x/2
            cnt += 1
    else:
        x = x-1
        cnt += 1

print(cnt)
