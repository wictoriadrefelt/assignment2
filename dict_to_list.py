
def dict_to_list(mydict):
    """ Uses list comprehension to loop through values in
    key/value in dict

    :param mydict:
    :return: a list of dicts.
    """

    result = [dict(**v, name=k) for k, v in mydict.items()]
    return result


def main():
    my_dict = {
        "john": {
            "age": 2,
            "favourite_color": "pink"
        },
        "sarah": {
            "age": 22,
            "favourite_color": "red"
        },
        "my": {
        "age": 12,
        "favourite_color": "red"
        },
        "potato": {
            "age": 78,
            "favourite_color": "dirt-brown"

        }

    }

    new = dict_to_list(my_dict)

    sorted_list = sorted(new, key=lambda k: k['age'])
    print(sorted_list)

if __name__ == '__main__':
    main()
