
def splitter(n_list):
    n = str(n_list)
    n.split()
    x = [list(n) for n in n_list]
    return x


def main():
    n = ['cherry', 'banana', 'apple']
    print(splitter(n))


if __name__ == '__main__':
    main()
