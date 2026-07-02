def slow_function():
    total = 0
    for i in range(5_000_000):
        total += i
    return total


def medium_function():
    data = []
    for i in range(100_000):
        data.append(i * i)
    return data


def fast_function():
    return sum(range(1000))

def mid_fast_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total    

def main():
    slow_function()
    medium_function()
    fast_function()


if __name__ == "__main__":
    main()