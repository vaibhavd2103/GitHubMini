def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a+b
            a = b
            b = c

            if c % 2 == 0 and c <= 4000000:
                print(c)


fib(4000000)


# hey there
