def calculate_structure_sum(args):
    tot = 0
    for x in args:
        if isinstance(x, dict):
            x = list(x.keys()) + list(x.values())
        if (not isinstance(x, list) and not isinstance(x, set) and not isinstance(x, tuple)
                and not isinstance(x, dict)):
            if isinstance(x, str):
                tot += len(x)
            else:
                tot += x
        else:
                tot += calculate_structure_sum(x)
    return tot


if __name__ == "__main__":
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

    result = calculate_structure_sum(data_structure)
    print(result)
