import time
import os
import sys
start_time = time.time()
#to get the absolute path of the src directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
#training the model
print("Training the model...")
train_status = os.system(f"python {os.path.join(src_dir, 'train_model.py')}")
if train_status != 0:
    print("Error: Training failed. Exiting...")
    sys.exit(1)
#Ranking candidates
print("Ranking candidates...")
rank_status = os.system(f"python {os.path.join(src_dir, 'rank_candidates.py')}")
if rank_status != 0:
    print("Error: Ranking failed. Exiting...")
    sys.exit(1)

print("Process completed successfully!")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Processing Time: {elapsed_time:.2f} seconds")