import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
print("Axes3D imported successfully!")

df = pd.read_csv('insurance.csv')
df.head()