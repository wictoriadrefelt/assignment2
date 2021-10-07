

def filter_nums(given_list):
    result = list(filter(lambda x: (x < 42), given_list))
    return result


def main():
    list_of_nums = [60, 91, 38, 13, 18, 34, 15, 74]
    print(filter_nums(list_of_nums))


if __name__ == '__main__':
    main()
