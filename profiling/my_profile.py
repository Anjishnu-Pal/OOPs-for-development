import random


def find_common_slow(a, b):
    common = []
    for item in a:
        if item in b:      # slow when b is a large list
            common.append(item)
    return common


def find_common_fast(a, b):
    b_set = set(b)        # convert list to set once
    common = []
    for item in a:
        if item in b_set: # fast membership check
            common.append(item)
    return common


def main():
    a = [random.randint(1, 200000) for _ in range(50000)]
    b = [random.randint(1, 200000) for _ in range(50000)]

    find_common_slow(a, b)
    find_common_fast(a, b)


if __name__ == "__main__":
    main()