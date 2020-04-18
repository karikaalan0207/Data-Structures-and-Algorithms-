def sieve(n):
    mark_l = [0] * (n + 1)
    mark_l[0] = mark_l[1] = 1
    i = 2

    while(i * i <= n):
        if(mark_l[i] == 0):
            for j in range(i * i, n + 1, i):
                mark_l[j] = 1
        i += 1

    for k in range(2,n + 1):
        if(mark_l[k] == 0):
            print(k)





if __name__ == '__main__':
    n = int(input())
    sieve(n)