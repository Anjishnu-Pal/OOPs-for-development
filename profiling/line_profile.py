@profile
def process_data():
    numbers = list(range(1_000_000))

    squares = []
    for n in numbers:
        squares.append(n * n)

    total = sum(squares)
    return total

process_data()