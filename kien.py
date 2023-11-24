n = int(input(">> Nhập giá trị của n :"))
b = [n]


def sangsonguyento():
    b = 1 * n
    b[1] = b[0] = 0
    for i in range(2, n):
        if b[i]:
            for j in range(i * i, n, i):
                b[j] = 0


def insosang(n):
    sangsonguyento()
    for i in range(n + 1):
        if b[i]:
            print(i, end=" ")
