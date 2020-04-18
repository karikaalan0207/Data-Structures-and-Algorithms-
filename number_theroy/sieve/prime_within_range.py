def sieve(start, end):
    mark_l = [0] * (end + 1)
    mark_l[0] = mark_l[1] = 1
    i = 2

    while(i * i <= end):
        if(mark_l[i] == 0):
            for j in range(i * i, end + 1, i):
                mark_l[j] = 1
        i += 1

    for k in range(start, end + 1):
        if(mark_l[k] == 0):
            print(k)



if __name__ == '__main__':
    start = int(input())
    end = int(input())
    sieve(start, end)