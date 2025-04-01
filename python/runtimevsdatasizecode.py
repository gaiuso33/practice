import time 
import numpy as np
import matplotlib.pyplot as plt

def generate_random_array(size):
    return np.random.rand(size)

def measure_runtime(size):
    start_time=time.time()
    array=generate_random_array(size)
    end_time=time.time()
    return end_time-start_time

#data sizes to test
data_sizes=[1000,5000,10000,15000,20000]

#measure runtime for each size
runtimes=[]
for size in data_sizes:
    runtime=measure_runtime(size)
    runtimes.append(runtime)

#plot the results
plt.plot(data_sizes, runtimes)
plt.xlabel("Data Size")
plt.ylabel("runtime")
plt.title("Graph of Data Size against Runtime")
