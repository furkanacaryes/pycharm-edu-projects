def list_to_str(split_string: list) -> str:
    """Converts given list to string"""
    return str().join(split_string)


def str_to_int_list(text: str) -> list[int]:
    """Converts spaced numerics to a list[int]"""
    return list(map(int, text.split()))


def filter_match(match, collection: list) -> list:
    """Filters exact matched items of the given list"""
    return list(filter(lambda item: item == match, collection))


def assert_every(predictable, collection: list) -> bool:
    """Asserts whether EVERY item in given list passes given prediction"""
    return all(list(map(predictable, collection)))


def assert_any(predictable, collection: list) -> bool:
    """Asserts whether ANY item in given list passes given prediction"""
    return any(list(map(predictable, collection)))


def print_row_list(rows):
    """Just prints given list[str]"""
    for row in rows:
        print(row)
