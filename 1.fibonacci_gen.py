


def fib_gen():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


def main():
    func = fib_gen()
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))


if __name__ == '__main__':
    main()
