import math


def sieve(n):
    l = [True] * (n+1)
    prime = []
    start = 2
    end   = int(math.sqrt(n))
    while(start <= end):
        if l[start] == True:
            prime.append(start)
            for i in range(start*start, n+1, start):
                if l[i] == True:
                    l[i] = False
        start += 1

    for j in range(end+1,n+1):
        if l[j] == True:
            prime.append(j)

    return prime

def main():
    n = int(input("Enter n: "))
    print(sieve(n))

if __name__ == '__main__':
    main()

