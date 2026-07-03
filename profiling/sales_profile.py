import random
import cProfile
import pstats


def generate_sales_data(n):
    products = ["Laptop", "Phone", "Tablet", "Watch"]
    data = []
    for _ in range(n):
        row = {
            "product": random.choice(products),
            "quantity": random.randint(1, 5),
            "price": random.randint(1000, 80000)
        }
        data.append(row)
    return data


def clean_data(data):
    cleaned = []
    for row in data:
        if row["quantity"] > 0 and row["price"] > 0:
            cleaned.append(row)
    return cleaned


def compute_sales_slow(data):
    products = list(set(row["product"] for row in data))
    result = {}
    for product in products:
        total = 0
        for row in data:
            if row["product"] == product:
                total += row["quantity"] * row["price"]
        result[product] = total
    return result


def compute_sales_fast(data):
    result = {}
    for row in data:
        product = row["product"]
        sale = row["quantity"] * row["price"]
        result[product] = result.get(product, 0) + sale
    return result


def main():
    data = generate_sales_data(300000)
    cleaned = clean_data(data)
    slow_result = compute_sales_slow(cleaned)
    fast_result = compute_sales_fast(cleaned)
    print("Slow:", slow_result)
    print("Fast:", fast_result)


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumtime")
    stats.print_stats(15)