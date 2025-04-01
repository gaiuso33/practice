import time 
import numpy as np

start_time=time.time()

random_array= np.random.rand(1000)
print(random_array)

end_time=time.time()
elasped_time=end_time-start_time
print (elasped_time) 