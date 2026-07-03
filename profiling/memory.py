from memory_profiler import profile

@profile
def create_big_list():
    data = []
    for i in range(2_000_000):
        data.append(i)
    return sum(data)

create_big_list()