import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


with open('a.us.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        



