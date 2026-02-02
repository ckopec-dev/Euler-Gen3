
import time

start_time = time.perf_counter()

# Do something that takes a while...

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Executed in {elapsed_time:.4f} seconds")