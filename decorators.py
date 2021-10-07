
"""
Takes a string and returns said string in lowercase.
"""

def lower_output(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper


@lower_output
def get_string(new_string):
    return new_string


def main():
    print(get_string('SOMEBODY HELP'))


if __name__ == '__main__':
    main()
