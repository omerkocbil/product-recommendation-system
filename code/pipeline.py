import os
import time

print("Cleaning is in progress on raw data...")
os.system('python preparation/cleaning.py')
time.sleep(1)

print("Creating word vector...")
os.system('python preparation/prep_product_vector.py')
time.sleep(1)

print("word2vec model is being trained...")
os.system('python training/word2vec.py')
time.sleep(1)

print("All is done! Model saved under model folder.")
time.sleep(1)