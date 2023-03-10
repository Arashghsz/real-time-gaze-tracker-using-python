import tracemalloc
import pandas as pd
import dask.dataframe as dd
import time


def tracing_start():
    tracemalloc.stop()
    print("nTracing Status : ", tracemalloc.is_tracing())
    tracemalloc.start()
    print("Tracing Status : ", tracemalloc.is_tracing())


def tracing_mem():
    first_size, first_peak = tracemalloc.get_traced_memory()
    peak = first_peak/(1024*1024)
    print("Peak Size in MB - ", peak)


tracing_start()
start = time.time()
sq_list = []
for elem in range(1,1000):
    sq_list.append(elem + elem**2)
#print(sq_list)
end = time.time()
print("time elapsed {} milli seconds".format((end-start)*1000))
tracing_mem()