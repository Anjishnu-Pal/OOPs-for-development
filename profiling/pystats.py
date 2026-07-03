import pstats

stats = pstats.Stats("result.prof")
stats.strip_dirs()
stats.sort_stats("cumtime")
stats.print_stats(10)