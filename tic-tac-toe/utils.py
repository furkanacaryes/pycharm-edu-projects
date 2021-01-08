def list_to_str(split_string: list) -> str:
    return str().join(split_string)


def str_to_int_list(user_coordinates: str) -> list[int]:
    return list(map(int, user_coordinates.split()))


def filter_match(_list, match):
    return list(filter(lambda item: item == match, _list))


def assert_every(_list, fn):
    return len(list(filter(fn, _list))) == len(_list)


def print_row_list(rows):
    for row in rows:
        print(row)
